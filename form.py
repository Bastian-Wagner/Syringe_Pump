# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_main(object):
    def setupUi(self, main):
        main.setObjectName("main")
        main.resize(784, 600)
        self.centralwidget = QtWidgets.QWidget(main)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_3 = QtWidgets.QLabel(self.tab_1)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_7.addWidget(self.label_3)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.comboBox_syringe_1 = QtWidgets.QComboBox(self.tab_1)
        self.comboBox_syringe_1.setCurrentText("BD 3 mL Syringe")
        self.comboBox_syringe_1.setObjectName("comboBox_syringe_1")
        self.comboBox_syringe_1.addItem("")
        self.comboBox_syringe_1.addItem("")
        self.comboBox_syringe_1.addItem("")
        self.comboBox_syringe_1.addItem("")
        self.verticalLayout_3.addWidget(self.comboBox_syringe_1)
        self.spinBox_velocity_p1 = QtWidgets.QSpinBox(self.tab_1)
        self.spinBox_velocity_p1.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_velocity_p1.setMinimum(-3000)
        self.spinBox_velocity_p1.setMaximum(3000)
        self.spinBox_velocity_p1.setProperty("value", 100)
        self.spinBox_velocity_p1.setObjectName("spinBox_velocity_p1")
        self.verticalLayout_3.addWidget(self.spinBox_velocity_p1)
        self.spinBox_volume_p1 = QtWidgets.QSpinBox(self.tab_1)
        self.spinBox_volume_p1.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_volume_p1.setMaximum(10000)
        self.spinBox_volume_p1.setObjectName("spinBox_volume_p1")
        self.verticalLayout_3.addWidget(self.spinBox_volume_p1)
        self.verticalLayout_7.addLayout(self.verticalLayout_3)
        self.horizontalLayout_6.addLayout(self.verticalLayout_7)
        self.line = QtWidgets.QFrame(self.tab_1)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_6.addWidget(self.line)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_2 = QtWidgets.QLabel(self.tab_1)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_8.addWidget(self.label_2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.comboBox_syringe_2 = QtWidgets.QComboBox(self.tab_1)
        self.comboBox_syringe_2.setObjectName("comboBox_syringe_2")
        self.comboBox_syringe_2.addItem("")
        self.comboBox_syringe_2.addItem("")
        self.comboBox_syringe_2.addItem("")
        self.comboBox_syringe_2.addItem("")
        self.verticalLayout_4.addWidget(self.comboBox_syringe_2)
        self.spinBox_velocity_p2 = QtWidgets.QSpinBox(self.tab_1)
        self.spinBox_velocity_p2.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_velocity_p2.setMinimum(-3000)
        self.spinBox_velocity_p2.setMaximum(3000)
        self.spinBox_velocity_p2.setProperty("value", 100)
        self.spinBox_velocity_p2.setObjectName("spinBox_velocity_p2")
        self.verticalLayout_4.addWidget(self.spinBox_velocity_p2)
        self.spinBox_volume_p2 = QtWidgets.QSpinBox(self.tab_1)
        self.spinBox_volume_p2.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_volume_p2.setMaximum(10000)
        self.spinBox_volume_p2.setObjectName("spinBox_volume_p2")
        self.verticalLayout_4.addWidget(self.spinBox_volume_p2)
        self.verticalLayout_8.addLayout(self.verticalLayout_4)
        self.horizontalLayout_6.addLayout(self.verticalLayout_8)
        self.line_2 = QtWidgets.QFrame(self.tab_1)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_6.addWidget(self.line_2)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label = QtWidgets.QLabel(self.tab_1)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_9.addWidget(self.label)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.comboBox_syringe_3 = QtWidgets.QComboBox(self.tab_1)
        self.comboBox_syringe_3.setObjectName("comboBox_syringe_3")
        self.comboBox_syringe_3.addItem("")
        self.comboBox_syringe_3.addItem("")
        self.comboBox_syringe_3.addItem("")
        self.comboBox_syringe_3.addItem("")
        self.verticalLayout_5.addWidget(self.comboBox_syringe_3)
        self.spinBox_velocity_p3 = QtWidgets.QSpinBox(self.tab_1)
        self.spinBox_velocity_p3.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_velocity_p3.setMinimum(-3000)
        self.spinBox_velocity_p3.setMaximum(2000)
        self.spinBox_velocity_p3.setProperty("value", 100)
        self.spinBox_velocity_p3.setObjectName("spinBox_velocity_p3")
        self.verticalLayout_5.addWidget(self.spinBox_velocity_p3)
        self.spinBox_volume_p3 = QtWidgets.QSpinBox(self.tab_1)
        self.spinBox_volume_p3.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_volume_p3.setMaximum(10000)
        self.spinBox_volume_p3.setObjectName("spinBox_volume_p3")
        self.verticalLayout_5.addWidget(self.spinBox_volume_p3)
        self.verticalLayout_9.addLayout(self.verticalLayout_5)
        self.horizontalLayout_6.addLayout(self.verticalLayout_9)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.line_3 = QtWidgets.QFrame(self.tab_1)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_2.addWidget(self.line_3)
        self.frame_3 = QtWidgets.QFrame(self.tab_1)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.checkBox_1 = QtWidgets.QCheckBox(self.frame_3)
        self.checkBox_1.setObjectName("checkBox_1")
        self.verticalLayout_10.addWidget(self.checkBox_1)
        self.checkBox_2 = QtWidgets.QCheckBox(self.frame_3)
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout_10.addWidget(self.checkBox_2)
        self.checkBox_3 = QtWidgets.QCheckBox(self.frame_3)
        self.checkBox_3.setObjectName("checkBox_3")
        self.verticalLayout_10.addWidget(self.checkBox_3)
        self.horizontalLayout_4.addLayout(self.verticalLayout_10)
        self.pushButton_start = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_start.setObjectName("pushButton_start")
        self.horizontalLayout_4.addWidget(self.pushButton_start)
        self.pushButton_stop = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_stop.setObjectName("pushButton_stop")
        self.horizontalLayout_4.addWidget(self.pushButton_stop)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.comboBox_ports = QtWidgets.QComboBox(self.tab_2)
        self.comboBox_ports.setObjectName("comboBox_ports")
        self.horizontalLayout_2.addWidget(self.comboBox_ports)
        self.pushButton_connect = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_connect.setObjectName("pushButton_connect")
        self.horizontalLayout_2.addWidget(self.pushButton_connect)
        self.pushButton_disconnect = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_disconnect.setObjectName("pushButton_disconnect")
        self.horizontalLayout_2.addWidget(self.pushButton_disconnect)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.comboBox_microsteps = QtWidgets.QComboBox(self.tab_2)
        self.comboBox_microsteps.setObjectName("comboBox_microsteps")
        self.comboBox_microsteps.addItem("")
        self.comboBox_microsteps.addItem("")
        self.comboBox_microsteps.addItem("")
        self.comboBox_microsteps.addItem("")
        self.horizontalLayout_5.addWidget(self.comboBox_microsteps)
        self.verticalLayout_6.addLayout(self.horizontalLayout_5)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout.addWidget(self.tabWidget)
        main.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(main)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 784, 22))
        self.menubar.setObjectName("menubar")
        main.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(main)
        self.statusbar.setObjectName("statusbar")
        main.setStatusBar(self.statusbar)

        self.retranslateUi(main)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(main)

    def retranslateUi(self, main):
        _translate = QtCore.QCoreApplication.translate
        main.setWindowTitle(_translate("main", "Syringe Pump Controller"))
        self.label_3.setText(_translate("main", "PUMP #1"))
        self.comboBox_syringe_1.setItemText(0, _translate("main", "BD 3 mL Syringe"))
        self.comboBox_syringe_1.setItemText(1, _translate("main", "BD 5 mL Syringe"))
        self.comboBox_syringe_1.setItemText(2, _translate("main", "BD 10 mL Syringe"))
        self.comboBox_syringe_1.setItemText(3, _translate("main", "BD 15 mL Syringe"))
        self.spinBox_velocity_p1.setSuffix(_translate("main", " µL/min"))
        self.spinBox_volume_p1.setSuffix(_translate("main", " µL"))
        self.label_2.setText(_translate("main", "PUMP #2"))
        self.comboBox_syringe_2.setItemText(0, _translate("main", "BD 3 mL Syringe"))
        self.comboBox_syringe_2.setItemText(1, _translate("main", "BD 5 mL Syringe"))
        self.comboBox_syringe_2.setItemText(2, _translate("main", "BD 10 mL Syringe"))
        self.comboBox_syringe_2.setItemText(3, _translate("main", "BD 15 mL Syringe"))
        self.spinBox_velocity_p2.setSuffix(_translate("main", " µL/min"))
        self.spinBox_volume_p2.setSuffix(_translate("main", " µL"))
        self.label.setText(_translate("main", "PUMP #3"))
        self.comboBox_syringe_3.setItemText(0, _translate("main", "BD 3 mL Syringe"))
        self.comboBox_syringe_3.setItemText(1, _translate("main", "BD 5 mL Syringe"))
        self.comboBox_syringe_3.setItemText(2, _translate("main", "BD 10 mL Syringe"))
        self.comboBox_syringe_3.setItemText(3, _translate("main", "BD 15 mL Syringe"))
        self.spinBox_velocity_p3.setSuffix(_translate("main", " µL/min"))
        self.spinBox_volume_p3.setSuffix(_translate("main", " µL"))
        self.checkBox_1.setText(_translate("main", "Pump #1 active"))
        self.checkBox_2.setText(_translate("main", "Pump #2 active"))
        self.checkBox_3.setText(_translate("main", "Pump #3 active"))
        self.pushButton_start.setText(_translate("main", "START"))
        self.pushButton_stop.setText(_translate("main", "STOP"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("main", "Syringe Controller"))
        self.pushButton_connect.setText(_translate("main", "Connect to Controller"))
        self.pushButton_disconnect.setText(_translate("main", "Disconnect"))
        self.label_4.setText(_translate("main", "Microstepping Option:"))
        self.comboBox_microsteps.setItemText(0, _translate("main", "32"))
        self.comboBox_microsteps.setItemText(1, _translate("main", "16"))
        self.comboBox_microsteps.setItemText(2, _translate("main", "8"))
        self.comboBox_microsteps.setItemText(3, _translate("main", "64"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("main", "Setup"))
