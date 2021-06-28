import seabreeze.spectrometers as sb
import time
import numpy as np
from PyQt5.QtCore import QObject, QMutexLocker, QMutex, pyqtSignal, pyqtSlot
import logging

logging.basicConfig(level=logging.INFO)


class QSpectrometer(QObject):
    """PyQt5 implementation of Spectrometer Instrument

    pyqtSignals:
        measurement_complete (list, list)
            the intensities and the times of the spectromter measurement
    """
    measurement_complete = pyqtSignal(np.ndarray, list)
    measurement_done = pyqtSignal()
    measurement_parameters = pyqtSignal(int, int)

    def __init__(self, integrationtime=100, average_measurements=1, polltime=0.01, timeout=30, parent=None):
        super().__init__(parent=parent)
        self.mutex = QMutex(QMutex.Recursive)
        self.measuring = False
        self.polltime = polltime
        self.timeout = timeout
        # Spectrometer
        self.spec = None
        self.connected = False
        self.measuring = False
        self.correct_dark_counts = False
        self.correct_nonlinearity = False
        self._integrationtime = integrationtime
        self._average_measurements = average_measurements
        self.dark = []
        self.min_integrationtime = None
        self.last_intensity = []
        self.last_times = []

    @property
    def name(self):
        """Name of the Instrument"""
        return type(self).__name__

    def connect(self, spec=None):
        if not spec:
            try:
                self.spec = sb.Spectrometer(sb.list_devices()[0])
            except IndexError as e:
                raise ConnectionError('No spectrometer found!')
        else:
            self.spec = spec
        self.min_integrationtime = self.spec.minimum_integration_time_micros / 1000
        self.integrationtime = self._integrationtime
        self.connected = True

    def disconnect(self):
        if not self.connected:
            return
        self.spec.close()
        self.connected = False

    @property
    def wavelengths(self):
        """The wavelengths this spectrometer can measure (Read-only) """
        wls = self.spec.wavelengths()
        return wls.tolist()

    @property
    def integrationtime(self):
        """ The spectrometer's integration time in [ms] """
        return self._integrationtime

    @integrationtime.setter
    def integrationtime(self, value):
        v = value * 1000
        min_v = self.min_integrationtime * 1000
        if v < min_v:
            logging.warning(f'{float(v) / 1000} ms is lower than the minimal '
                            'allowed integration time')
            logging.warning('Integration time set to mimimal value')
            v = min_v
        self.spec.integration_time_micros(v)
        self._integrationtime = v / 1000

    @property
    def average_measurements(self):
        """Average number of measurements. Stops any measurement upon setting."""
        return self._average_measurements

    @average_measurements.setter
    def average_measurements(self, value):
        self.measuring = False
        self._average_measurements = value

    @pyqtSlot()
    @pyqtSlot(list, list)
    def measure(self, *args):
        """Performs a mutex-locked measurement.

        Returns:
           | list: intensities [counts]
           | list: times measured over as
               [ [tstart0, tstart1,...], [tstop0, tstop1, ...] ]
        Emits:
            measurement_complete (list, list):
                | intensities [counts],
                | times measured over as
                    [ [tstart0, tstart1,...], [tstop0, tstop1, ...] ]
        """

        # logging.info('Measuring Spectrometer')
        #        print('Spectrometer: {}'.format(threading.currentThread()))
        # with(QMutexLocker(self.mutex)):
        #     # Perform 'fake' measurement if the integration times don't match
        #     # This clears the Spectrometer's cache
        #     cache_cleared = False
        #     self.measuring = True
        #     while self.measuring and not cache_cleared:
        #         t = [time.time()]
        #         intensity = (self.spec.intensities(
        #             self.correct_dark_counts,
        #             self.correct_nonlinearity) / self.average_measurements)
        #         t.append(time.time())
        #         mm = self._integrationtime / 1000
        #         cache_cleared = (mm * 0.9 < np.diff(t)[0] < mm * 1.1)
        #         # Cannot measure less than 30 ms time difference
        #         if mm * 1000 < 30:
        #             cache_cleared = True
        #         logging.info('Cache cleared? {}'.format(cache_cleared))
        with(QMutexLocker(self.mutex)):
            self.measuring = True
            t = []
            intensity = np.zeros(len(self.spec.wavelengths()))
            n = 1
            while self.measuring and n <= self.average_measurements:
                t.append(time.time())
                intensity += (1. / self.average_measurements *
                              self.spec.intensities(self.correct_dark_counts,
                                                    self.correct_nonlinearity))
                t.append(time.time())
                n += 1
            if any(self.dark):
                intensity = intensity - self.dark

        self.measuring = False
        logging.info('Spectrometer Done')
        self.last_intensity = intensity
        self.last_times = t
        self.measurement_complete.emit(intensity, t)
        self.measurement_done.emit()
        self.measurement_parameters.emit(self.integrationtime, self.average_measurements)
        return intensity, t

    @pyqtSlot()
    def measure_dark(self):
        """Performs a mutex-locked dark measurement.
        The result will be substracted from the reported intensities.
        """
        with(QMutexLocker(self.mutex)):
            self.dark, t = self.measure()
        self.measurement_complete.emit(self.dark, t)
        self.last_intensity = self.dark
        self.last_times = t
        return self.dark, t

    @pyqtSlot()
    def clear_dark(self):
        self.dark = np.zeros(len(self.spec.wavelengths()))



