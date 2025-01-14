import csv
import time
import numpy as np
import pyvisa as visa
import logging
import pyvisa.errors


def list_available_devices():
    return visa.ResourceManager().list_resources()


class PowerMeter:
    """
    Python Class for the Thorlabs PM100A powermeter with basic functionalities.
    """

    def __init__(self, name='USB0::0x1313::0x8079::P1002333::INSTR'):
        self.logger_instrument = logging.getLogger('ínstrument.PowerMeter')
        self.logger_instrument.info('init PowerMeter')
        self.name = name
        self.pm = None
        self.connected = False
        self.measuring = False

    def connect_device(self):
        try:
            self.logger_instrument.info('Attempting to connect powermeter')
            self.pm = visa.ResourceManager().open_resource(self.name)
            self.connected = True
            # Set spectrometer to power mode
            self.pm.write('conf:pow')
            self.logger_instrument.info('Connection to powermeter succesful')
        except pyvisa.errors.VisaIOError as error:
            self.logger_instrument.error('Could not connect powermeter')
            raise ConnectionError('No powermeter found')

    @property
    def wavelength(self):
        """ Current wavelength the powermeter is scanning on [nm]. """
        wavelength = self.pm.query_ascii_values("sense:corr:wav?")[0]
        self.logger_instrument.info(f'current wavelength = {wavelength}')
        return wavelength

    @wavelength.setter
    def wavelength(self, value):
        self.logger_instrument.info(f'setting the powermeter wavelength to {value}')
        self.pm.write(f'sense:corr:wav {value}')

    @property
    def averageing(self):
        """
        Return the number of measurements being averaged over.
        one measurement takes approximately 3 ms.
        """
        averaging = int(self.pm.query('sens:aver:coun?').strip())
        self.logger_instrument.info(f'averaging powermeter = {averaging}')
        return averaging

    @averageing.setter
    def averageing(self, value):
        """
        Set the number of values being averaged over
        one measurement takes approximately 3 ms
        timeout not automatically adjusted
        """
        self.logger_instrument.info(f'setting averageing to {value}')
        value = int(value)
        self.pm.write(f'sens:aver:coun {value}')

    @property
    def timeout(self):
        """ Return the timeout of the PM in ms. """
        self.logger_instrument.info('requesting timeout time from powermeter')
        return self.pm.timeout

    @timeout.setter
    def timeout(self, value):
        """ Set the value of the timeout, value in seconds. """
        self.logger_instrument.info(f'Setting powermeter timeout to {value}')
        value = int(value * 1000)
        self.pm.timeout = value

    @property
    def sensor(self):
        """ Return information about the connected sensor. """
        try:
            self.logger_instrument.info('Requesting sensor info powermeter')
            sensorinfo = self.pm.query('syst:sens:idn?').strip().split(',')
            model = sensorinfo[0]
            sn = sensorinfo[1]
            caldate = sensorinfo[2]
            sensor = {'Model': model, 'Serial_Number': sn, 'Calibration_Date': caldate}
        except pyvisa.errors.VisaIOError as e:
            self.logger_instrument.error(f'Error querying sensor - try power cycling PM100A : {e}')
            raise ConnectionError
        return sensor

    @property
    def device(self):
        """ Return the powermeter model. """
        self.logger_instrument.info('Requesting powermeter model')
        info = self.pm.query('*IDN?').strip().split(',')
        brand = info[0]
        model = info[1]
        sn = info[2]
        firmware = info[3]
        device_info = {'Brand': brand, 'Model': model, 'Serial_Number': sn, 'Firmware_Version': firmware}
        return device_info

    def read_power(self):
        """ Read the power from the powermeter."""
        self.logger_instrument.debug('Reading single power value')
        power = self.pm.query_ascii_values('read?')[0]
        return power

    def zero_device(self):
        """ Zero the current reading of the device. """
        self.logger_instrument.info('Zeroing powermeter')
        self.pm.write('sens:corr:coll:zero:init')
        while int(self.pm.query('sens:corr:coll:zero:stat?').strip()):
            time.sleep(0.2)

    def reset_default(self):
        """ Reset the device to default settings. """
        self.logger_instrument.info('Resetting default settings')
        self.pm.write('*RST')
        self.pm.write('*CLS')

    @property
    def sensitivity_photodiode(self):
        """ Query the photodiode sensor sensitivity at the current wavelength. """
        try:
            self.logger_instrument.info('Querying photodiode sensitivity')
            sensitivity = self.pm.query('sens:corr:pow:pdio:resp?').strip()
            return sensitivity
        except pyvisa.errors.VisaIOError:
            self.logger_instrument.error('Cannot read photodiode response, no thermopile connected')

    @property
    def sensitivity_thermopile(self):
        """ Query the thermopile sensor sensitivity at the current wavelength. """
        try:
            self.logger_instrument.info('Querying the thermopile sensitivity')
            sensitivity = self.pm.query('sens:corr:pow:ther:resp?').strip()
            return sensitivity
        except pyvisa.errors.VisaIOError:
            self.logger_instrument.error('Cannot read thermopile response, no thermopile connected')

    @property
    def autorange(self):
        """ Read autorange status. """
        self.logger_instrument.info('Reading autorange status.')
        autorange = int(self.pm.query('sens:pow:rang:auto?').strip())
        autorange = bool(autorange)
        return autorange

    @autorange.setter
    def autorange(self, value):
        """ Turn autorange on or off. """
        self.logger_instrument.info(f'Set autorange to {value}')
        integervalue = int(value)
        self.pm.write(f'sens:pow:rang:auto {integervalue}')

    @property
    def accelerator(self):
        """ Query if the accelerator circuit state. """
        try:
            self.logger_instrument.info('Querying accelerator state')
            acceleratorstatus = self.pm.query('inp:ther:acc:state?').strip()
            return bool(int(acceleratorstatus))
        except pyvisa.errors.VisaIOError:
            self.logger_instrument.error('Cannot read accelerator status, no thermopile connected')

    @accelerator.setter
    def accelerator(self, value):
        """ Set the accelerator circuit """
        self.logger_instrument.info(f'Setting the accelerator circuit to {value}')
        intvalue = int(value)
        try:
            self.pm.write(f'inp:ther:acc:state {intvalue}')
        except pyvisa.errors.VisaIOError:
            self.logger_instrument.error('Cannot set accelerator, no thermopile connected')

    @property
    def thermopile_timeconstant(self):
        """ Query the thermopile time constant. """
        try:
            self.logger_instrument.info('Querying the thermopile time constant')
            tau = self.pm.query('inp:ther:acc:tau?').strip()
            return tau
        except pyvisa.errors.VisaIOError:
            self.logger_instrument.error('Cannot read timeconstant, no thermopile connected')

    def set_sensitivity_correction(self, file):
        """
        Set the correction for the spectrometer sensitivity and all other optics within the used setup.
        The sensitivity file (.csv) is formatted as following:
        CREATION DATE: <<Date of calibration>>
        Wavelength (nm), Intensity (a.u.)
        wl_1, I_1
        ..., ...

        :param file: location of the correction file
        :return: dict: {'wavelengths': [...], 'intensity': [...]} a dict of the correction file
        """
        if not file:
            self.logger_instrument.warning('Tried setting sensitivity without sensitivity file.')
            self.sensitivity_correction = None
            return None
        self.logger_instrument.info('Setting custom sensor sensitivity')
        sensitivity_correction = {'wavelengths': [], 'intensity': []}
        with open(file) as correction_file:
            correction_reader = csv.reader(correction_file, delimiter=',')
            for nrow, row in enumerate(correction_reader):
                if nrow in [0, 1]:
                    continue
                sensitivity_correction['wavelengths'].append(row[0])
                sensitivity_correction['intensity'].append(row[1])
        return sensitivity_correction

    def disconnect(self):
        """ Disconnect the powermeter. """
        self.logger_instrument.info('Disconnecting powermeter')
        self.pm.close()
        self.connected = False

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.disconnect()

    def __repr__(self):
        return self.pm.query('*IDN?')


if __name__ == '__main__':
    # set up logging if file called directly
    from pathlib import Path
    import yaml
    import logging.config
    import logging.handlers
    pathlogging = Path(__file__).parent.parent.parent / 'logging/loggingconfig_testing.yml'
    with pathlogging.open() as f:
        config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)