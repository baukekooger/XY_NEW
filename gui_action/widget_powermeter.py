from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer, pyqtSlot, QThread
from gui_design.powermeter import Ui_Form
import numpy as np
from instruments.Thorlabs.qpowermeter import QPowerMeter
import logging


class PowerMeterWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.logger_widget = logging.getLogger('gui.PowerMeter')
        self.logger_widget.info('init powermeter widget ui')
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.powermeter = QPowerMeter()

    def connect_signals_slots(self):
        self.powermeter.measurement_complete_multiple.connect(self.handle_measurement)
        self.powermeter.measurement_parameters.connect(self.update_parameters)
        self.powermeter.emit_parameters()
        self.ui.spinBox_wavelength_alignment.editingFinished.connect(self.handle_wavelength)
        self.ui.pushButton_zero.clicked.connect(self.powermeter.zero)

    def disconnect_signals_slots(self):
        self.powermeter.measurement_complete_multiple.disconnect(self.handle_measurement)
        self.powermeter.measurement_parameters.disconnect(self.update_parameters)
        self.ui.spinBox_wavelength_alignment.editingFinished.disconnect(self.handle_wavelength)
        self.ui.pushButton_zero.clicked.disconnect(self.powermeter.zero)

    @pyqtSlot(list, list)
    def handle_measurement(self, times, power):
        # set the right unit depending on the incoming power
        measurement = np.mean(power)
        if measurement >= 1:
            self.ui.label_power_value_unit.setText(f'{measurement:.2} W')
        elif measurement >= 0.1:
            self.ui.label_power_value_unit.setText(f'{measurement*1e3:.0f} mW')
        elif measurement >= 0.01:
            self.ui.label_power_value_unit.setText(f'{measurement*1e3:.1f} mW')
        elif measurement >= 0.001:
            self.ui.label_power_value_unit.setText(f'{measurement*1e3:.2f} mW')
        elif measurement >= 0:
            self.ui.label_power_value_unit.setText(f'{measurement * 1e6:.0f} \u03BCW')
        else:
            self.ui.label_power_value_unit.setText(f'zeroing required')

    @pyqtSlot(int, int)
    def update_parameters(self, wavelength, integration_time):
        self.ui.label_indicator_wavelength_alignment.setText(f'{wavelength} nm')

    @pyqtSlot()
    def handle_wavelength(self):
        wavelength = self.ui.spinBox_wavelength_alignment.value()
        self.powermeter.wavelength = wavelength
        QTimer.singleShot(0, self.powermeter.emit_parameters)

    # def closeEvent(self, event):
    #     self.powermeter.disconnect()
    #     event.accept()


if __name__ == '__main__':
    # set up logging if file called directly
    from pathlib import Path
    import yaml
    import logging.config
    import logging.handlers
    pathlogging = Path(__file__).parent.parent / 'loggingconfig.yml'
    with pathlogging.open() as f:
        config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)
    # setup pyqt app
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = PowerMeterWidget()
    window.show()
    sys.exit(app.exec_())
