# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'spectrometer.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(347, 284)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
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
        self.groupBox_experiment = QtWidgets.QGroupBox(self.page_experiment)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_experiment.sizePolicy().hasHeightForWidth())
        self.groupBox_experiment.setSizePolicy(sizePolicy)
        self.groupBox_experiment.setObjectName("groupBox_experiment")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_experiment)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_integration_time_experiment = QtWidgets.QLabel(self.groupBox_experiment)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_integration_time_experiment.sizePolicy().hasHeightForWidth())
        self.label_integration_time_experiment.setSizePolicy(sizePolicy)
        self.label_integration_time_experiment.setMinimumSize(QtCore.QSize(110, 0))
        self.label_integration_time_experiment.setObjectName("label_integration_time_experiment")
        self.horizontalLayout.addWidget(self.label_integration_time_experiment)
        self.spinBox_integration_time_experiment = QtWidgets.QSpinBox(self.groupBox_experiment)
        self.spinBox_integration_time_experiment.setMinimum(30)
        self.spinBox_integration_time_experiment.setMaximum(100000)
        self.spinBox_integration_time_experiment.setObjectName("spinBox_integration_time_experiment")
        self.horizontalLayout.addWidget(self.spinBox_integration_time_experiment)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.groupBox_experiment)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(110, 0))
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.spinBox_averageing_experiment = QtWidgets.QSpinBox(self.groupBox_experiment)
        self.spinBox_averageing_experiment.setMinimum(1)
        self.spinBox_averageing_experiment.setMaximum(1000)
        self.spinBox_averageing_experiment.setObjectName("spinBox_averageing_experiment")
        self.horizontalLayout_2.addWidget(self.spinBox_averageing_experiment)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_experiment, 1, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_experiment)
        self.page_alignment = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.page_alignment.sizePolicy().hasHeightForWidth())
        self.page_alignment.setSizePolicy(sizePolicy)
        self.page_alignment.setObjectName("page_alignment")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.page_alignment)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.groupBox_alignment = QtWidgets.QGroupBox(self.page_alignment)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_alignment.sizePolicy().hasHeightForWidth())
        self.groupBox_alignment.setSizePolicy(sizePolicy)
        self.groupBox_alignment.setObjectName("groupBox_alignment")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_alignment)
        self.gridLayout_5.setContentsMargins(9, 9, 9, 9)
        self.gridLayout_5.setSpacing(6)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_integration_time_alignment = QtWidgets.QLabel(self.groupBox_alignment)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_integration_time_alignment.sizePolicy().hasHeightForWidth())
        self.label_integration_time_alignment.setSizePolicy(sizePolicy)
        self.label_integration_time_alignment.setMinimumSize(QtCore.QSize(110, 0))
        self.label_integration_time_alignment.setObjectName("label_integration_time_alignment")
        self.horizontalLayout_5.addWidget(self.label_integration_time_alignment)
        self.spinBox_integration_time_alignment = QtWidgets.QSpinBox(self.groupBox_alignment)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_integration_time_alignment.sizePolicy().hasHeightForWidth())
        self.spinBox_integration_time_alignment.setSizePolicy(sizePolicy)
        self.spinBox_integration_time_alignment.setMinimum(30)
        self.spinBox_integration_time_alignment.setMaximum(100000)
        self.spinBox_integration_time_alignment.setObjectName("spinBox_integration_time_alignment")
        self.horizontalLayout_5.addWidget(self.spinBox_integration_time_alignment)
        self.label_integration_time_alignment_value = QtWidgets.QLabel(self.groupBox_alignment)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_integration_time_alignment_value.sizePolicy().hasHeightForWidth())
        self.label_integration_time_alignment_value.setSizePolicy(sizePolicy)
        self.label_integration_time_alignment_value.setMinimumSize(QtCore.QSize(80, 0))
        self.label_integration_time_alignment_value.setAlignment(QtCore.Qt.AlignCenter)
        self.label_integration_time_alignment_value.setObjectName("label_integration_time_alignment_value")
        self.horizontalLayout_5.addWidget(self.label_integration_time_alignment_value)
        self.gridLayout_5.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pushButton_dark = QtWidgets.QPushButton(self.groupBox_alignment)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_dark.sizePolicy().hasHeightForWidth())
        self.pushButton_dark.setSizePolicy(sizePolicy)
        self.pushButton_dark.setObjectName("pushButton_dark")
        self.horizontalLayout_6.addWidget(self.pushButton_dark)
        self.pushButton_lamp = QtWidgets.QPushButton(self.groupBox_alignment)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_lamp.sizePolicy().hasHeightForWidth())
        self.pushButton_lamp.setSizePolicy(sizePolicy)
        self.pushButton_lamp.setObjectName("pushButton_lamp")
        self.horizontalLayout_6.addWidget(self.pushButton_lamp)
        self.gridLayout_5.addLayout(self.horizontalLayout_6, 2, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_reset = QtWidgets.QPushButton(self.groupBox_alignment)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_reset.sizePolicy().hasHeightForWidth())
        self.pushButton_reset.setSizePolicy(sizePolicy)
        self.pushButton_reset.setObjectName("pushButton_reset")
        self.horizontalLayout_3.addWidget(self.pushButton_reset)
        self.pushButton_transmission = QtWidgets.QPushButton(self.groupBox_alignment)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_transmission.sizePolicy().hasHeightForWidth())
        self.pushButton_transmission.setSizePolicy(sizePolicy)
        self.pushButton_transmission.setObjectName("pushButton_transmission")
        self.horizontalLayout_3.addWidget(self.pushButton_transmission)
        self.gridLayout_5.addLayout(self.horizontalLayout_3, 3, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_averageing_alignment = QtWidgets.QLabel(self.groupBox_alignment)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_averageing_alignment.sizePolicy().hasHeightForWidth())
        self.label_averageing_alignment.setSizePolicy(sizePolicy)
        self.label_averageing_alignment.setMinimumSize(QtCore.QSize(110, 0))
        self.label_averageing_alignment.setObjectName("label_averageing_alignment")
        self.horizontalLayout_4.addWidget(self.label_averageing_alignment)
        self.spinBox_averageing_alignment = QtWidgets.QSpinBox(self.groupBox_alignment)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_averageing_alignment.sizePolicy().hasHeightForWidth())
        self.spinBox_averageing_alignment.setSizePolicy(sizePolicy)
        self.spinBox_averageing_alignment.setMinimum(1)
        self.spinBox_averageing_alignment.setMaximum(1000)
        self.spinBox_averageing_alignment.setObjectName("spinBox_averageing_alignment")
        self.horizontalLayout_4.addWidget(self.spinBox_averageing_alignment)
        self.label_averageing_alignment_value = QtWidgets.QLabel(self.groupBox_alignment)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_averageing_alignment_value.sizePolicy().hasHeightForWidth())
        self.label_averageing_alignment_value.setSizePolicy(sizePolicy)
        self.label_averageing_alignment_value.setMinimumSize(QtCore.QSize(80, 0))
        self.label_averageing_alignment_value.setAlignment(QtCore.Qt.AlignCenter)
        self.label_averageing_alignment_value.setObjectName("label_averageing_alignment_value")
        self.horizontalLayout_4.addWidget(self.label_averageing_alignment_value)
        self.gridLayout_5.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_alignment, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_alignment)
        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox_experiment.setTitle(_translate("Form", "Spectrometer"))
        self.label_integration_time_experiment.setText(_translate("Form", "integration time (ms)"))
        self.label.setText(_translate("Form", "averageing #"))
        self.groupBox_alignment.setTitle(_translate("Form", "Spectrometer"))
        self.label_integration_time_alignment.setText(_translate("Form", "integration time (ms)"))
        self.label_integration_time_alignment_value.setText(_translate("Form", "10000 ms"))
        self.pushButton_dark.setText(_translate("Form", "Dark"))
        self.pushButton_lamp.setText(_translate("Form", "Lamp"))
        self.pushButton_reset.setText(_translate("Form", "Reset"))
        self.pushButton_transmission.setText(_translate("Form", "Transmission"))
        self.label_averageing_alignment.setText(_translate("Form", "averageing #"))
        self.label_averageing_alignment_value.setText(_translate("Form", "10"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

