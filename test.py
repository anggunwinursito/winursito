import sys#, os, glob
from PyQt5 import QtWidgets, uic#QtCore, QtGui, uic
import serial, time

qtCreatorFile = "test.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
	def __init__(self):
		QtWidgets.QMainWindow.__init__(self)
		Ui_MainWindow.__init__(self)
		self.setupUi(self)
		self.pushButton_OpenSerial.clicked.connect(self.OpenSerial)
		self.pushButton_Exit.clicked.connect(self.AppExit)
		self.pushButton_stop.clicked.connect(self.STOP)         
		self.pushButton_cek.clicked.connect(self.CekStat)
		self.textEdit_log.append("PyQT-Adruino")

        
	def OpenSerial(self):
		if self.pushButton_OpenSerial.text()=='Open Serial':
			self.ser = serial.Serial("COM3", "9600", timeout=0.1)
			if self.ser.isOpen():
				self.pushButton_OpenSerial.setText('Close Serial')
				self.textEdit_log.append("Opening serial port... OK")
			else:
				self.textEdit_log.append("can not open serial port")
		else:
			if self.ser.isOpen():
				self.ser.close()
			self.pushButton_OpenSerial.setText('Open Serial')
			self.textEdit_log.append("Closing serial port... OK")

	def STOP(self):

		self.TXdata = bytearray(1)
		self.TXdata[0]=1
		self.ser.write(self.TXdata)
   
	def AppExit(self):
		self.textEdit_log.setText("Exit application")
		sys.exit()
        
        def CekStat(self):
            self.bytesToRead = self.ser.inWaiting()
            if(self.bytesToRead > 0):
                rxdata = self.ser.read(self.bytesToRead)
                time.sleep(3)
                self.textEdit.append(rxdata)
        
                
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
