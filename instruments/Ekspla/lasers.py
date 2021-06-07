from ctypes import c_int, c_double, c_char_p, byref, windll
import os
import time
import logging.config
import numpy
import platform
import win32com.client
import re
import asyncio

# Add location of EKSPLA REMOTECONTROL library to path
if platform.architecture()[0] == '64bit':
    os.environ['PATH'] = os.path.dirname(__file__) + os.path.sep + 'lib64' + ';' + os.environ['PATH']
    path = os.path.join(os.path.dirname(__file__), 'lib64', 'REMOTECONTROL64.dll')
    _lib = windll.LoadLibrary(path)
else:
    os.environ['PATH'] = os.path.dirname(__file__) + os.path.sep + 'lib' + ';' + os.environ['PATH']
    _lib = windll.LoadLibrary('REMOTECONTROL.dll')
# Constants
MINIMUM_WAVELENGTH = 190
MAXIMUM_WAVELENGTH = 2300


def list_available_devices():
    devices = []
    pattern = re.compile('USB\\\\.*\\\\(FTZ.*)')
    for device in win32com.client.GetObject("winmgmts:").InstancesOf("Win32_USBHub"):
        print(device.DeviceID)
        if pattern.match(device.DeviceID):
            devices.append(pattern.match(device.DeviceID).groups()[0])
    return devices


class NT230:
    """
    Ekspla NT230 OPO Laser control class.
    
    Interfaces to control the Ekspla NT230 OPO laser through the EKSPLA REMOTECONTROL library over USB
    """

    def __init__(self, connection_type=0, device_name='FTZ3O6AD', waittime=0.05, polltime=0.1, timeout=10):
        self.waittime = waittime
        self.polltime = polltime
        self.timeout = timeout
        self.measuring = False
        self.handle = c_int()
        self.connect(connection_type, device_name)

    @property
    def wavelength(self):
        """
            get/set wavelength of the EKSPLA laser in nm
                RANGE 190-2600 nm
                set wavelength : NT230.wavelength = 250.00
                get wavelength : wl = NT230.wavelength
        """

        dev = "MidiOPG:31"
        reg = "WaveLength"
        wavelength = self._get_register_double(dev, reg)
        return wavelength

    @wavelength.setter
    def wavelength(self, wl):
        """
        Sets the wavelength of the laser. 
        """
        if wl < MINIMUM_WAVELENGTH:
            wl = MINIMUM_WAVELENGTH
            logging.warning('Exceeded wavelength range when setting to {}.2f nm. Set to {}.2f nm'.format(
                wl, MINIMUM_WAVELENGTH))
        if wl > MAXIMUM_WAVELENGTH:
            wl = MAXIMUM_WAVELENGTH
            logging.warning('Exceeded wavelength range when setting to {}.2f nm. Set to {}.2f nm'.format(
                wl, MAXIMUM_WAVELENGTH))

        dev = "MidiOPG:31"
        reg = "WaveLength"
        self._set_register_double(dev, reg, wl)
        #        #TODO Set motor to calibrated position from maximal intensity
        #        dev = "PBP2:35"
        #        reg = "Motor position"
        #        mot_pos = np.interp(wl, self.ls_mot[:,0], self.ls_mot[:,1])
        #        try:
        #            self.set_register_double(dev, reg, mot_pos)
        #        except LaserError as e:
        #            logging.warning('Register {} not recognized'.format(reg))

    async def set_wavelength(self, wl):
        """
        This method will sleep for `waittime` to move laser components.
        """
        self.wavelength = wl
        # Wait for waittime to allow the laser to settle
        asyncio.sleep(self.waittime)      

    @property
    def use_spectral_cleaning_unit(self):
        """
        get/set status of the Spectrum Cleaning Unit
        """
        dev = "MidiOPG:31"
        reg = "Configuration"
        SCU = self._get_register_double(dev, reg)
        return bool(SCU)

    @use_spectral_cleaning_unit.setter
    def use_spectral_cleaning_unit(self, status):
        dev = "MidiOPG:31"
        reg = "Configuration"
        self._set_register_double(dev, reg, int(status))

    @property
    def energylevel(self):
        """
            get/set energy level of the laser 
                level           : OFF, Adjust or MAX
                set energylevel : NT2300.energylevel = OFF
                get energylevel : el = NT2300.energylevel
        """
        dev = "CPU8000:16"
        reg = "Output Energy level"
        k = ['Off', 'Adjust', 'Max']
        energylevel = k[int(self._get_register_double(dev, reg))]
        return energylevel

    @energylevel.setter
    def energylevel(self, level):
        dev = "CPU8000:16"
        reg = "Output Energy level"
        levels = ['Off', 'Adjust', 'Max']
        if level in levels:
            level = levels.index(level)
        else:
            level = 0
        self._set_register_double(dev, reg, level)

    @property
    def power(self):
        """
            get the power of laser in Watt
                pw = NT230.power
        """
        dev = "11PMK:56"
        reg = "Power"
        power = self._get_register_double(dev, reg)
        return power

    @property
    def status(self):
        """
            get the status of laser 
                [Off,Initiation,Tuning...,Ok.]
        """

        dev = "MidiOPG:31"
        reg = "Status"
        status = ['Off', 'Initiation', 'Tuning...', 'OK']
        status = status[int(self._get_register_double(dev, reg))]
        return status

    def _set_register_double(self, dev, reg, val):
        """
            Sets a register value
        """
        d = c_char_p(bytes(dev, 'utf-8'))
        r = c_char_p(bytes(reg, 'utf-8'))
        v = c_double(val)
        # Try, if we fail, try again
        e = _lib.rcSetRegFromDoubleA2(self.handle, d, r, v, c_int(0))
        if not e == 0:
            logging.warning('An error occurred during Laser communication, reattempting...')
            time.sleep(self.polltime)
            e = _lib.rcSetRegFromDoubleA2(self.handle, d, r, v, c_int(0))
        self._is_error(e)

    def _get_register_double(self, dev, reg):
        """Retrieves a register value
        """
        d = c_char_p(bytes(dev, 'utf-8'))
        r = c_char_p(bytes(reg, 'utf-8'))
        resp = c_double()
        # Try, if we fail, try again
        e = _lib.rcGetRegAsDouble2(self.handle, d, r, byref(resp),
                                   self.timeout, None)
        if not e == 0:
            logging.warning('An error occurred during Laser communication, reattempting...')
            time.sleep(self.polltime)
            e = _lib.rcGetRegAsDouble2(self.handle, d, r, byref(resp),
                                       self.timeout, None)
        self._is_error(e)
        return resp.value

    @staticmethod
    def _is_error(e):
        """Checks if e is a number associated with a laser error.
        Raises the appropriate error for each error value other than e==0 (no error).
        """
        if e == 0:
            return
        elif e == 7:
            raise ConnectionRefusedError(e)
        elif e in [17, 18]:
            raise ConnectionError(e)
        elif e in [11, 12, 13]:
            raise RangeError(e)
        elif e == 8:
            raise TimeoutError('Timeout waiting for laser answer')
        else:
            raise LaserError(e)

    def connect(self, connection_type=0, device_name='FTZ3O6AD'):
        """
        connect to laser
        """
        c_devicename = c_char_p(bytes(device_name, 'utf-8'))
        try:
            self._is_error(_lib.rcConnect2(byref(self.handle),
                                           connection_type, c_devicename, None))
        except ConnectionError:
            # The Laser is already connected to us, nothing to worry about
            logging.warning('Already connected to laser!')

    def close(self):
        """
            Turns the laser off and disconnects 
        """
        self.measuring = False
        self.energylevel = 'Off'
        self._is_error(_lib.rcDisconnect2(self.handle))

    def measure(self):
        """Measure the current values of the laser.
        A single measurement should last around 0.25 seconds.
        
        Returns: 
            | float: wavelength
            | str: energylevel
            | float: power
            | bool: stability of the laser
        """
        self.measuring = True
        logging.info('Measuring laser...')
        wavelength = self.wavelength
        energylevel = self.energylevel
        power = self.power
        stable = self.is_stable()
        self.measuring = False
        return wavelength, energylevel, power, stable

    def is_stable(self):
        """ Returns True if no fluctuation in Power higher than 5% occurs
        between now and 5 polltimes
        
        Returns:
            (bool): True/False depending on stability
        """
        p = []
        for _ in range(5):
            p.append(self.power)
            time.sleep(self.polltime)
        return numpy.std(p) / numpy.mean(p) < 0.05

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def __repr__(self):
        """
            get serial number + model number and configuration file creation date
        """
        dev = "id()"
        ID = self._get_register_double(dev, "")
        return ID


class LaserError(Exception):
    """Exception raised for errors caused within Laser communication

        Attributes:
            errorcode -- errorcode provided by laser
    """
    errorcodes = ["Comunication succeeded, no error",
                  "End of registers list",
                  "No config file found",
                  "Wrong CSV file",
                  "Application provided return buffer is too short",
                  "No such device name",
                  "No such register name",
                  "Failed to connect",
                  "Timeout waiting for device answer",
                  "Register is read only",
                  "Register is not NV",
                  "Attempt to set value above upper limit",
                  "Attempt to set value below bottom limit",
                  "Attempt to set not allowed value",
                  "Register is not being logged",
                  "Not enough memory",
                  "No data in the queue yet",
                  "Already connected, please disconnect first",
                  "Not connected, please connect first"]

    def __init__(self, errorcode):
        Exception.__init__(self, self.errorcodes[errorcode])


class RangeError(LaserError):
    """ Exception raised for errors caused within Laser communication """
    pass
