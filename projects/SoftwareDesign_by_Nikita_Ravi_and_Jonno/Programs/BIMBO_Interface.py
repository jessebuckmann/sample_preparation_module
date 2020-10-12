import sys, AD2Sensor, Overview, ArduinoWidget ##Comment the ArduinoWidget if you do not have an Arduino, uncomment ArduinoWidget if you do want to use it and it is not there
from PyQt5 import QtGui
from PyQt5.QtCore import pyqtSlot
import pyqtgraph as pg   # used for additional plotting features
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
import labphew
import logging
import os
from time import time
from labphew.core.tools.gui_tools import set_spinbox_stepsize, ValueLabelItem, SaverWidget, ModifyConfig, fit_on_screen
from labphew.core.base.general_worker import WorkThread
from labphew.core.base.view_base import MonitorWindowBase, ScanWindowBase
from labphew.model.analog_discovery_2_model import Operator
from labphew.controller.digilent.waveforms import DfwController as DfwController ##This is used for the real device, comment this if you want to use the simulated version
#from labphew.controller.digilent.waveforms import SimulatedDfwController as DfwController ##This is used for the simulated device, comment this if you want use a real AD2

import ctypes # needed for setting the taskbar icon

# this makes sure the favicon also appears as the taskbar icon
myappid = 'BIMBO'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

class TabWidget(QDialog):
    def __init__(self):
        super().__init__()

        #making and centering the window, setting icons adding min/max button in the program bar
        self.title = 'Beautiful Interface of Magic Box Operations (BIMBO)'
        self.left = 200
        self.top = 200
        self.width = 1050
        self.height = 600
        self.setWindowTitle(self.title)
        self.setWindowIcon(QIcon('BIMBOLogov2Favicon.png'))
        self.setWindowFlag(Qt.WindowMinimizeButtonHint, True)
        self.setWindowFlag(Qt.WindowMaximizeButtonHint, True)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.center()

        #adding image to background
        self.background = QLabel(self)
        pixmap = QPixmap('BIMBOLogov2Start.png')
        self.background.setScaledContents(True)
        self.background.setPixmap(pixmap)

        #adding an invisible start button to be able to press enter to start
        startbutton = QPushButton('Let\'s Go!', self)
        startbutton.resize(100, 32)
        startbutton.move(-50, -50)
        startbutton.clicked.connect(self.bgHide)
        startbutton.clicked.connect(self.StartProgram)

    #hide the background
    def bgHide(self):
        self.background.hide()

    #start the control program
    def StartProgram(self):
        #initialising the tabwidget
        tabwidget = QTabWidget()

        #getting the instrument for AD2
        instrument = DfwController()
        opr = Operator(instrument)
        opr.load_config('./config.yml')

        #adding tabs to our tabwidget
        #tabwidget.addTab(Overview.Overview(), 'Overview') #this widget still needs to be implemented
        tabwidget.addTab(ArduinoWidget.TempSensor(), 'Temperature') #If you do not have an Arduino comment out this line
        tabwidget.addTab(ArduinoWidget.PresSensor(), 'Pressure') #If you do not have an Arduino comment out this line
        tabwidget.addTab(AD2Sensor.Sensor1(opr), 'Analog Discovery 2')

        vbox = QVBoxLayout()
        vbox.addWidget(tabwidget)

        self.setLayout(vbox)

    # for displaying a message when closing the program with the x button
    def closeEvent(self, event):
        quit_msg = "Are you sure you want to exit the program?"
        reply = QtGui.QMessageBox.question(self, 'Message', quit_msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    # for centering the window
    def center(self):
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

app = QApplication(sys.argv)
tabwidget = TabWidget()
tabwidget.show()
app.exec()