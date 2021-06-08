# This Python file uses the following encoding: utf-8
import sys
import os
import serial
import glob
import time

from PyQt5 import QtCore, QtWidgets
import breeze_resources

from form import Ui_main


class main(QtWidgets.QMainWindow):

    def __init__(self):
        super(main, self).__init__()
        self.ui = Ui_main()
        self.ui.setupUi(self)
        #Get serial ports
        self.get_serial_ports()
        #Connect all GUI components
        self.connect_all_gui_components()
        #Gray out buttons
        self.ui.pushButton_disconnect.setEnabled(False)
        self.ui.pushButton_start.setEnabled(False)
        self.ui.pushButton_stop.setEnabled(False)


    def connect_all_gui_components(self):
        self.ui.pushButton_connect.clicked.connect(self.connect)
        self.ui.pushButton_disconnect.clicked.connect(self.disconnect)
        self.ui.pushButton_start.clicked.connect(self.start)
        self.ui.pushButton_stop.clicked.connect(self.stop)
        self.ui.pushButton_refresh.clicked.connect(self.get_serial_ports)


    def get_serial_ports(self):
        """ Lists serial port names
        :raises EnvironmentError
        On unsupported or unknown platform
        :returns:
         A list of the serial ports available on the system
         """
        if sys.platform.startswith('win'):
            ports = [r'\\.\COM%s' % (i + 1) for i in range(256)]
        elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
            # this excludes your current terminal "/dev/tty"
            ports = glob.glob('/dev/tty[A-Za-z]*')
        elif sys.platform.startswith('darwin'):
            ports = glob.glob('/dev/tty.*')
        else:
            raise EnvironmentError('Unsupported platform')

        result = []
        for port in ports:
            try:
                s = serial.Serial(port)
                s.close()
                result.append(port)
            except (OSError, serial.SerialException):
                    pass
        self.ui.comboBox_ports.clear()
        self.ui.comboBox_ports.addItems(result)


        # Connect to the Arduino board
    def connect(self):
        try:
            port_declared = self.ui.comboBox_ports.currentText()
            try:
                self.serial = serial.Serial()
                self.serial.port = port_declared
                self.serial.baudrate = 230400
                self.serial.parity = serial.PARITY_NONE
                self.serial.stopbits = serial.STOPBITS_ONE
                self.serial.bytesize = serial.EIGHTBITS
                self.serial.timeout = 1
                self.serial.open()


                self.ui.pushButton_disconnect.setEnabled(True)
                self.ui.pushButton_start.setEnabled(True)
                self.ui.pushButton_connect.setEnabled(False)
                time.sleep(3)
                print("Board has been connected")
            except:
               raise CannotConnectException
        except AttributeError:
            print("Please plug in the board and select a proper port, then press connect.")


        # Disconnect from the Arduino board
    def disconnect(self):
        print("Disconnecting from board..")
        time.sleep(3)
        self.serial.close()
        print("Board has been disconnected")

        self.ui.pushButton_connect.setEnabled(True)
        #Gray out buttons
        self.ui.pushButton_disconnect.setEnabled(False)
        self.ui.pushButton_start.setEnabled(False)
        self.ui.pushButton_stop.setEnabled(False)

        # Start pump
    def start(self):

        if self.ui.checkBox_1.isChecked():
            self.p1_velocity = self.ui.spinBox_velocity_p1.value()
            self.p1_volume = self.ui.spinBox_volume_p1.value()
            self.syringe_1 = self.ui.comboBox_syringe_1.currentIndex()
            steps_per_second_1 = self.calc_steps_per_second(self.p1_velocity, self.syringe_1)
            total_steps_1 = self.calc_total_steps(self.p1_volume, self.syringe_1)
            if steps_per_second_1 < 0:
                total_steps_1 = -total_steps_1
        else:
            steps_per_second_1 = 0
            total_steps_1 = 0

        if self.ui.checkBox_2.isChecked():
            self.p2_velocity = self.ui.spinBox_velocity_p2.value()
            self.p2_volume = self.ui.spinBox_volume_p2.value()
            self.syringe_2 = self.ui.comboBox_syringe_2.currentIndex()
            steps_per_second_2 = self.calc_steps_per_second(self.p2_velocity, self.syringe_2)
            total_steps_2 = self.calc_total_steps(self.p2_volume, self.syringe_2)
            if steps_per_second_2 < 0:
                total_steps_2 = -total_steps_2
        else:
            steps_per_second_2 = 0
            total_steps_2 = 0

        if self.ui.checkBox_3.isChecked():
            self.p3_velocity = self.ui.spinBox_velocity_p3.value()
            self.p3_volume = self.ui.spinBox_volume_p3.value()
            self.syringe_3 = self.ui.comboBox_syringe_3.currentIndex()
            steps_per_second = self.calc_steps_per_second(self.p3_velocity, self.syringe_3)
            total_steps = self.calc_total_steps(self.p3_volume, self.syringe_3)
            if steps_per_second_3 < 0:
                total_steps_3 = -total_steps_3
        else:
            steps_per_second_3 = 0
            total_steps_3 = 0

        data = str(steps_per_second_1) + '_' + str(total_steps_1) + '_' + str(steps_per_second_2) + '_' + str(total_steps_2) + '_' + str(steps_per_second_3) + '_' + str(total_steps_3)
        self.serial.write(data.encode())
        print(data)
        self.ui.pushButton_start.setEnabled(False)
        self.ui.pushButton_stop.setEnabled(True)

        # Stop pump
    def stop(self):
        data = '0_0_0_0_0_0'
        self.serial.write(data.encode())
        print(data)
        self.ui.pushButton_start.setEnabled(True)
        self.ui.pushButton_stop.setEnabled(False)


    def calc_steps_per_second(self, velocity, syringe_index):
        self.microsteps = self.ui.comboBox_microsteps.currentText()
        # syringe_parameters = steps needed per uL when microstepping=1
        # BD 1mL = 14.53, 3mL, 5mL, 10mL, 15mL
        syringe_parameters = [4.47, 2.7, 1.35, 0.9]
        volume_per_second = float(velocity)/60
        steps_per_second = round(volume_per_second*syringe_parameters[syringe_index]*int(self.microsteps))
        print(steps_per_second)
        return steps_per_second

    def calc_total_steps(self,volume, syringe_index):
        self.microsteps = self.ui.comboBox_microsteps.currentText()
        # syringe_parameters = steps needed per uL when microstepping=1
        # BD 1mL = 14.53, 3mL, 5mL, 10mL, 15mL
        syringe_parameters = [4.47, 2.7, 1.35, 0.9]
        total_steps = volume*syringe_parameters[syringe_index]*int(self.microsteps)
        return total_steps


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    #Set Stylesheet
    file = QtCore.QFile(":/dark.qss")
    file.open(QtCore.QFile.ReadOnly | QtCore.QFile.Text)
    stream = QtCore.QTextStream(file)
    app.setStyleSheet(stream.readAll())

    window = main()
    window.show()
    sys.exit(app.exec_())
