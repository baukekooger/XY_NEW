# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'laser.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(304, 172)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_experiment = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.page_experiment.sizePolicy().hasHeightForWidth())
        self.page_experiment.setSizePolicy(sizePolicy)
        self.page_experiment.setObjectName("page_experiment")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.page_experiment)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.groupBox_laser = QtWidgets.QGroupBox(self.page_experiment)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_laser.sizePolicy().hasHeightForWidth())
        self.groupBox_laser.setSizePolicy(sizePolicy)
        self.groupBox_laser.setObjectName("groupBox_laser")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_laser)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_wavelength_start = QtWidgets.QLabel(self.groupBox_laser)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_wavelength_start.sizePolicy().hasHeightForWidth())
        self.label_wavelength_start.setSizePolicy(sizePolicy)
        self.label_wavelength_start.setMinimumSize(QtCore.QSize(60, 0))
        self.label_wavelength_start.setObjectName("label_wavelength_start")
        self.horizontalLayout_3.addWidget(self.label_wavelength_start)
        self.spinBox_wavelength_start = QtWidgets.QSpinBox(self.groupBox_laser)
        self.spinBox_wavelength_start.setMinimumSize(QtCore.QSize(20, 0))
        self.spinBox_wavelength_start.setMinimum(200)
        self.spinBox_wavelength_start.setMaximum(2300)
        self.spinBox_wavelength_start.setObjectName("spinBox_wavelength_start")
        self.horizontalLayout_3.addWidget(self.spinBox_wavelength_start)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_wavelength_stop = QtWidgets.QLabel(self.groupBox_laser)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_wavelength_stop.sizePolicy().hasHeightForWidth())
        self.label_wavelength_stop.setSizePolicy(sizePolicy)
        self.label_wavelength_stop.setMinimumSize(QtCore.QSize(60, 0))
        self.label_wavelength_stop.setObjectName("label_wavelength_stop")
        self.horizontalLayout_2.addWidget(self.label_wavelength_stop)
        self.spinBox_wavelength_stop = QtWidgets.QSpinBox(self.groupBox_laser)
        self.spinBox_wavelength_stop.setMinimumSize(QtCore.QSize(20, 0))
        self.spinBox_wavelength_stop.setMinimum(200)
        self.spinBox_wavelength_stop.setMaximum(2300)
        self.spinBox_wavelength_stop.setProperty("value", 375)
        self.spinBox_wavelength_stop.setObjectName("spinBox_wavelength_stop")
        self.horizontalLayout_2.addWidget(self.spinBox_wavelength_stop)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_wavelength_step = QtWidgets.QLabel(self.groupBox_laser)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_wavelength_step.sizePolicy().hasHeightForWidth())
        self.label_wavelength_step.setSizePolicy(sizePolicy)
        self.label_wavelength_step.setMinimumSize(QtCore.QSize(60, 0))
        self.label_wavelength_step.setObjectName("label_wavelength_step")
        self.horizontalLayout.addWidget(self.label_wavelength_step)
        self.spinBox_wavelength_step = QtWidgets.QSpinBox(self.groupBox_laser)
        self.spinBox_wavelength_step.setMinimumSize(QtCore.QSize(20, 0))
        self.spinBox_wavelength_step.setMinimum(1)
        self.spinBox_wavelength_step.setMaximum(1000)
        self.spinBox_wavelength_step.setObjectName("spinBox_wavelength_step")
        self.horizontalLayout.addWidget(self.spinBox_wavelength_step)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label = QtWidgets.QLabel(self.groupBox_laser)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(60, 0))
        self.label.setObjectName("label")
        self.horizontalLayout_7.addWidget(self.label)
        self.comboBox_energy_level_experiment = QtWidgets.QComboBox(self.groupBox_laser)
        self.comboBox_energy_level_experiment.setObjectName("comboBox_energy_level_experiment")
        self.comboBox_energy_level_experiment.addItem("")
        self.comboBox_energy_level_experiment.addItem("")
        self.horizontalLayout_7.addWidget(self.comboBox_energy_level_experiment)
        self.gridLayout_2.addLayout(self.horizontalLayout_7, 1, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_laser, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_experiment)
        self.page_alignment = QtWidgets.QWidget()
        self.page_alignment.setObjectName("page_alignment")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.page_alignment)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.groupBox = QtWidgets.QGroupBox(self.page_alignment)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton_off = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_off.setMinimumSize(QtCore.QSize(40, 0))
        self.pushButton_off.setStyleSheet("QPushButton::checked\n"
"{\n"
"background-color: rgb(0, 198, 6)\n"
"}")
        self.pushButton_off.setCheckable(True)
        self.pushButton_off.setChecked(False)
        self.pushButton_off.setObjectName("pushButton_off")
        self.horizontalLayout_5.addWidget(self.pushButton_off)
        self.pushButton_adjust = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_adjust.setMinimumSize(QtCore.QSize(40, 0))
        self.pushButton_adjust.setStyleSheet("QPushButton::checked\n"
"{\n"
"background-color: rgb(0, 198, 6)\n"
"}")
        self.pushButton_adjust.setCheckable(True)
        self.pushButton_adjust.setObjectName("pushButton_adjust")
        self.horizontalLayout_5.addWidget(self.pushButton_adjust)
        self.pushButton_max = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_max.setMinimumSize(QtCore.QSize(40, 0))
        self.pushButton_max.setStyleSheet("QPushButton::checked\n"
"{\n"
"background-color: rgb(0, 198, 6)\n"
"}")
        self.pushButton_max.setCheckable(True)
        self.pushButton_max.setObjectName("pushButton_max")
        self.horizontalLayout_5.addWidget(self.pushButton_max)
        self.pushButton_output = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_output.setMinimumSize(QtCore.QSize(40, 0))
        self.pushButton_output.setStyleSheet("QPushButton::checked\n"
"{\n"
"background-color: rgb(0, 198, 6)\n"
"}")
        self.pushButton_output.setCheckable(True)
        self.pushButton_output.setObjectName("pushButton_output")
        self.horizontalLayout_5.addWidget(self.pushButton_output)
        self.gridLayout_5.addLayout(self.horizontalLayout_5, 1, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_wavelength = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_wavelength.sizePolicy().hasHeightForWidth())
        self.label_wavelength.setSizePolicy(sizePolicy)
        self.label_wavelength.setObjectName("label_wavelength")
        self.horizontalLayout_4.addWidget(self.label_wavelength)
        self.spinBox_wavelength_alignment = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_wavelength_alignment.setMinimum(200)
        self.spinBox_wavelength_alignment.setMaximum(2300)
        self.spinBox_wavelength_alignment.setProperty("value", 375)
        self.spinBox_wavelength_alignment.setDisplayIntegerBase(10)
        self.spinBox_wavelength_alignment.setObjectName("spinBox_wavelength_alignment")
        self.horizontalLayout_4.addWidget(self.spinBox_wavelength_alignment)
        self.label_wavelength_indicator = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_wavelength_indicator.sizePolicy().hasHeightForWidth())
        self.label_wavelength_indicator.setSizePolicy(sizePolicy)
        self.label_wavelength_indicator.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_wavelength_indicator.setObjectName("label_wavelength_indicator")
        self.horizontalLayout_4.addWidget(self.label_wavelength_indicator)
        self.gridLayout_5.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_status_title = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_status_title.sizePolicy().hasHeightForWidth())
        self.label_status_title.setSizePolicy(sizePolicy)
        self.label_status_title.setObjectName("label_status_title")
        self.horizontalLayout_6.addWidget(self.label_status_title)
        self.label_status_value = QtWidgets.QLabel(self.groupBox)
        self.label_status_value.setAlignment(QtCore.Qt.AlignCenter)
        self.label_status_value.setObjectName("label_status_value")
        self.horizontalLayout_6.addWidget(self.label_status_value)
        self.line_2 = QtWidgets.QFrame(self.groupBox)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_6.addWidget(self.line_2)
        self.checkBox_stable = QtWidgets.QCheckBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_stable.sizePolicy().hasHeightForWidth())
        self.checkBox_stable.setSizePolicy(sizePolicy)
        self.checkBox_stable.setStyleSheet("QCheckBox::indicator:checked\n"
"{\n"
"background-color: rgb(0, 198, 6)\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked\n"
"{\n"
"background-color: rgb(202, 0, 3);\n"
"}")
        self.checkBox_stable.setObjectName("checkBox_stable")
        self.horizontalLayout_6.addWidget(self.checkBox_stable)
        self.gridLayout_5.addLayout(self.horizontalLayout_6, 2, 0, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_alignment)
        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox_laser.setTitle(_translate("Form", "Laser Wavelength"))
        self.label_wavelength_start.setText(_translate("Form", "start (nm)"))
        self.label_wavelength_stop.setText(_translate("Form", "stop (nm) "))
        self.label_wavelength_step.setText(_translate("Form", "step (nm) "))
        self.label.setText(_translate("Form", "energy level"))
        self.comboBox_energy_level_experiment.setItemText(0, _translate("Form", "Max"))
        self.comboBox_energy_level_experiment.setItemText(1, _translate("Form", "Adjust"))
        self.groupBox.setTitle(_translate("Form", "Laser (nm) "))
        self.pushButton_off.setText(_translate("Form", "Off"))
        self.pushButton_adjust.setText(_translate("Form", "Adjust"))
        self.pushButton_max.setText(_translate("Form", "Max"))
        self.pushButton_output.setText(_translate("Form", "Output"))
        self.label_wavelength.setText(_translate("Form", "Wavelength (nm)"))
        self.label_wavelength_indicator.setText(_translate("Form", "1100 nm"))
        self.label_status_title.setText(_translate("Form", "Status:"))
        self.label_status_value.setText(_translate("Form", "Ok"))
        self.checkBox_stable.setText(_translate("Form", "Stable"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

