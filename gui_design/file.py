# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'file.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(343, 298)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox = QtWidgets.QGroupBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 280))
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 280))
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(75, 0))
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.lineEdit_sample = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_sample.setObjectName("lineEdit_sample")
        self.horizontalLayout_3.addWidget(self.lineEdit_sample)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_substrate = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_substrate.sizePolicy().hasHeightForWidth())
        self.label_substrate.setSizePolicy(sizePolicy)
        self.label_substrate.setMinimumSize(QtCore.QSize(75, 0))
        self.label_substrate.setObjectName("label_substrate")
        self.horizontalLayout_4.addWidget(self.label_substrate)
        self.comboBox_substrate = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_substrate.setObjectName("comboBox_substrate")
        self.comboBox_substrate.addItem("")
        self.comboBox_substrate.addItem("")
        self.comboBox_substrate.addItem("")
        self.horizontalLayout_4.addWidget(self.comboBox_substrate)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QtCore.QSize(75, 0))
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.comboBox_nd_filter = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_nd_filter.setObjectName("comboBox_nd_filter")
        self.comboBox_nd_filter.addItem("")
        self.comboBox_nd_filter.addItem("")
        self.horizontalLayout_5.addWidget(self.comboBox_nd_filter)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMinimumSize(QtCore.QSize(75, 0))
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.comboBox_longpass_filter = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_longpass_filter.setObjectName("comboBox_longpass_filter")
        self.comboBox_longpass_filter.addItem("")
        self.comboBox_longpass_filter.addItem("")
        self.comboBox_longpass_filter.addItem("")
        self.comboBox_longpass_filter.addItem("")
        self.comboBox_longpass_filter.addItem("")
        self.comboBox_longpass_filter.addItem("")
        self.comboBox_longpass_filter.addItem("")
        self.horizontalLayout_6.addWidget(self.comboBox_longpass_filter)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMinimumSize(QtCore.QSize(75, 0))
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_7.addWidget(self.label_6)
        self.comboBox_bandpass_filter = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_bandpass_filter.setObjectName("comboBox_bandpass_filter")
        self.comboBox_bandpass_filter.addItem("")
        self.comboBox_bandpass_filter.addItem("")
        self.horizontalLayout_7.addWidget(self.comboBox_bandpass_filter)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(75, 0))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.plainTextEdit_comments = QtWidgets.QPlainTextEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plainTextEdit_comments.sizePolicy().hasHeightForWidth())
        self.plainTextEdit_comments.setSizePolicy(sizePolicy)
        self.plainTextEdit_comments.setMinimumSize(QtCore.QSize(0, 0))
        self.plainTextEdit_comments.setObjectName("plainTextEdit_comments")
        self.horizontalLayout_2.addWidget(self.plainTextEdit_comments)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(75, 0))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.lineEdit_directory = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_directory.setObjectName("lineEdit_directory")
        self.horizontalLayout.addWidget(self.lineEdit_directory)
        self.toolButton_directory = QtWidgets.QToolButton(self.groupBox)
        self.toolButton_directory.setObjectName("toolButton_directory")
        self.horizontalLayout.addWidget(self.toolButton_directory)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)

        self.retranslateUi(Form)
        self.comboBox_substrate.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "File"))
        self.label.setText(_translate("Form", "sample"))
        self.label_substrate.setText(_translate("Form", "substrate"))
        self.comboBox_substrate.setItemText(0, _translate("Form", "50X50 mm (Borofloat)"))
        self.comboBox_substrate.setItemText(1, _translate("Form", "44X44 mm (Quartz)"))
        self.comboBox_substrate.setItemText(2, _translate("Form", "22X22 mm (Quartz small)"))
        self.label_4.setText(_translate("Form", "neutral filter"))
        self.comboBox_nd_filter.setItemText(0, _translate("Form", "none"))
        self.comboBox_nd_filter.setItemText(1, _translate("Form", "OD 1.0 -  Thorlabs NDUVW10B"))
        self.label_5.setText(_translate("Form", "longpasss filter"))
        self.comboBox_longpass_filter.setItemText(0, _translate("Form", "none"))
        self.comboBox_longpass_filter.setItemText(1, _translate("Form", "300 nm - Semrock FF01-300/LP25"))
        self.comboBox_longpass_filter.setItemText(2, _translate("Form", "325 nm - Semrock BLP01-325R-25"))
        self.comboBox_longpass_filter.setItemText(3, _translate("Form", "355 nm - Semrock BLP01-355R-25"))
        self.comboBox_longpass_filter.setItemText(4, _translate("Form", "405 nm - Semrock BLP01-405R-25"))
        self.comboBox_longpass_filter.setItemText(5, _translate("Form", "430 nm - Semrock FF01-430/LP-25"))
        self.comboBox_longpass_filter.setItemText(6, _translate("Form", "473 nm - Semrock BLP01-473R-25"))
        self.label_6.setText(_translate("Form", "bandpass filter"))
        self.comboBox_bandpass_filter.setItemText(0, _translate("Form", "none"))
        self.comboBox_bandpass_filter.setItemText(1, _translate("Form", "640 nm - Thorlabs FB640-10-1 V 1-39-11"))
        self.label_2.setText(_translate("Form", "comments"))
        self.label_3.setText(_translate("Form", "storage dir"))
        self.toolButton_directory.setText(_translate("Form", "..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

