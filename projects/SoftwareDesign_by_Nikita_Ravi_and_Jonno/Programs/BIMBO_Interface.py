import sys, AD2Sensor, Overview
from PyQt5 import QtGui
from PyQt5.QtCore import pyqtSlot
import pyqtgraph as pg   # used for additional plotting features
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
import labphew
import logging
import os
from time import time
from labphew.core.tools.gui_tools import set_spinbox_stepsize, ValueLabelItem, SaverWidget, ModifyConfig, fit_on_screen
from labphew.core.base.general_worker import WorkThread
from labphew.core.base.view_base import MonitorWindowBase, ScanWindowBase
from labphew.model.analog_discovery_2_model import Operator
from labphew.controller.digilent.waveforms import SimulatedDfwController as DfwController


import ctypes # needed for setting the taskbar icon

# this makes sure the favicon also appears as the taskbar icon
myappid = 'BIMBO'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)


class TabWidget(QDialog):
    def __init__(self):
        super().__init__()

        self.title = 'Beautiful Interface of Magic Box Operations (BIMBO)'
        self.left = 200
        self.top = 200
        self.width = 1050
        self.height = 600
        self.setWindowTitle(self.title)
        self.setWindowIcon(QIcon('BIMBOLogov1.png'))
        self.setWindowFlag(Qt.WindowMinimizeButtonHint, True)
        self.setWindowFlag(Qt.WindowMaximizeButtonHint, True)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.center()

        tabwidget = QTabWidget()
        tabwidget.addTab(Overview.Overview(), 'Overview')

        instrument = DfwController()
        opr = Operator(instrument)
        opr.load_config()

        tabwidget.addTab(AD2Sensor.Sensor1(opr), 'Sensor 1')

        vbox = QVBoxLayout()
        vbox.addWidget(tabwidget)

        # # Use this bit to display an "Are you sure"-dialogbox

        self.setLayout(vbox)

    # for displaying a message when closing the program with the x button
    """
    def closeEvent(self, event):
        quit_msg = "Are you sure you want to exit the program?"
        reply = QtGui.QMessageBox.question(self, 'Message', quit_msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
    """
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