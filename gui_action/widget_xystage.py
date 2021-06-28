from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal, pyqtSlot
from gui_design.xystage import Ui_Form
from instruments.Thorlabs.xystage import QXYStage


class XYStageWidget(QtWidgets.QWidget):

    move = pyqtSignal(float, float)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.xystage = QXYStage()
        self.ui.doubleSpinBox_x.clear()
        self.ui.doubleSpinBox_y.clear()

    def connect_signals_slots(self):
        self.xystage.measurement_complete.connect(self.set_position)
        self.xystage.homing_status.connect(self.set_homing)
        self.ui.doubleSpinBox_x.editingFinished.connect(self._handle_move_x)
        self.ui.doubleSpinBox_y.editingFinished.connect(self._handle_move_y)
        self.ui.pushButton_home_motors.clicked.connect(self.xystage.home)
        self.ui.doubleSpinBox_x.setMaximum(self.xystage.xmax)
        self.ui.doubleSpinBox_y.setMaximum(self.xystage.ymax)

    def _handle_move_x(self):
        self.xystage.x = self.ui.doubleSpinBox_x.value()
        self.ui.doubleSpinBox_x.clear()

    def _handle_move_y(self):
        self.xystage.y = self.ui.doubleSpinBox_y.value()
        self.ui.doubleSpinBox_y.clear()

    @pyqtSlot(float, float)
    def set_position(self, x, y):
        self.ui.label_x_value.setText(f'{x:.2f} mm')
        self.ui.label_y_value.setText(f'{y:.2f} mm')

    @pyqtSlot(bool, bool)
    def set_homing(self, xhome, yhome):
        self.ui.checkBox_homed_x.setChecked(xhome)
        self.ui.checkBox_homed_y.setChecked(yhome)


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = XYStageWidget()
    window.show()
    sys.exit(app.exec_())

