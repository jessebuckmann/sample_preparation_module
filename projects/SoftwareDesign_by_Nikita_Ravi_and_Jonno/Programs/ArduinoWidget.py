from PyQt5 import QtGui
import pyqtgraph as pg   # used for additional plotting features
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtCore
from pyqtgraph import PlotWidget, plot
import sys  # We need sys so that we can pass argv to QApplication
import os
from random import randint
import serial  # import Serial Library
import numpy  # Import numpy

tempC = []
pressure = []
arduinoData = serial.Serial('COM5', 9600)  # Creating our serial object named arduinoData
class TempSensor(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QtGui.QVBoxLayout()
        self.setLayout(layout)
        tempWidget = pg.PlotWidget(name='Temp')  ## giving the plots names allows us to link their axes together

        # Add start stop scan button

        box_monitor = QGroupBox('Controls')
        layout_monitor = QVBoxLayout()
        box_monitor.setLayout(layout_monitor)

        layout_monitor_buttons = QHBoxLayout()
        layout_monitor.addLayout(layout_monitor_buttons)

        self.timer = QtCore.QTimer()
        self.timer.setInterval(50)
        self.timer.timeout.connect(self.update_plot_data)

        self.start_button = QPushButton('Start')
        self.start_button.clicked.connect(self.start_measure)
        self.stop_button = QPushButton('Stop')
        self.stop_button.clicked.connect(self.stop_measure)

        # button for opening the scan function
        self.scan_button = QPushButton('Scan')
        # self.scan_button.clicked.connect(self.open_scan)

        layout_monitor_buttons.addWidget(self.start_button)
        layout_monitor_buttons.addWidget(self.stop_button)
        layout_monitor_buttons.addWidget(self.scan_button)

        layout.addWidget(tempWidget)
        layout.addWidget(box_monitor)

        arduinoString = arduinoData.readline()  # read the line of text from the serial port
        dataArray = arduinoString.split(b',')  # Split it into an array called dataArray
        temp = float(dataArray[0])  # Convert first element to floating number and put in temp
        P = float(dataArray[1])  # Convert second element to floating number and put in P
        tempC.append(temp)  # Build our tempF array by appending temp readings
        pressure.append(P)  # Building our pressure array by appending P readings

        styles = {'color': '#FFFFFF', 'font-size': '16px'}
        tempWidget.setLabel('left', 'Temperature (°C)', **styles)
        tempWidget.setLabel('bottom', 'Time (s)', **styles)

        self.x = list(range(100))  # 100 time points
        self.y = [0] * 100  # 100 data points


        pen = pg.mkPen(color=(255, 0, 0))
        self.data_line = tempWidget.plot(self.x, self.y, pen=pen)



    def start_measure(self):
        if not self.timer.isActive():
            self.timer.start()

    def stop_measure(self):
        if self.timer.isActive():
            self.timer.stop()



    def update_plot_data(self):
        arduinoString = arduinoData.readline()  # read the line of text from the serial port
        dataArray = arduinoString.split(b',')  # Split it into an array called dataArray
        temp = float(dataArray[0])  # Convert first element to floating number and put in temp
        P = float(dataArray[1])  # Convert second element to floating number and put in P
        tempC.append(temp)  # Build our tempF array by appending temp readings
        pressure.append(P)  # Building our pressure array by appending P readings

        self.x = self.x[1:]  # Remove the first y element.
        self.x.append(self.x[-1] + 1)  # Add a new value 1 higher than the last.

        self.y = self.y[1:]  # Remove the first
        self.y.append(temp)  # Add new pressure value

        self.data_line.setData(self.x, self.y)  # Update the data.

class PresSensor(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QtGui.QVBoxLayout()
        self.setLayout(layout)
        presWidget = pg.PlotWidget(name='Pres')  ## giving the plots names allows us to link their axes together


        # Add start stop scan button

        box_monitor = QGroupBox('Controls')
        layout_monitor = QVBoxLayout()
        box_monitor.setLayout(layout_monitor)


        layout_monitor_buttons = QHBoxLayout()
        layout_monitor.addLayout(layout_monitor_buttons)
        self.timer2 = QtCore.QTimer()
        self.timer2.setInterval(50)
        self.timer2.timeout.connect(self.update_plot_data)

        self.start_button = QPushButton('Start')
        self.start_button.clicked.connect(self.start_measure)
        self.stop_button = QPushButton('Stop')
        self.stop_button.clicked.connect(self.stop_measure)

        #button for opening the scan function
        self.scan_button = QPushButton('Scan')
        #self.scan_button.clicked.connect(self.open_scan)

        layout_monitor_buttons.addWidget(self.start_button)
        layout_monitor_buttons.addWidget(self.stop_button)
        layout_monitor_buttons.addWidget(self.scan_button)

        layout.addWidget(presWidget)
        layout.addWidget(box_monitor)

        arduinoString = arduinoData.readline()  # read the line of text from the serial port
        dataArray = arduinoString.split(b',')  # Split it into an array called dataArray
        temp = float(dataArray[0])  # Convert first element to floating number and put in temp
        P = float(dataArray[1])  # Convert second element to floating number and put in P
        tempC.append(temp)  # Build our tempF array by appending temp readings
        pressure.append(P)  # Building our pressure array by appending P readings

        styles = {'color': '#FFFFFF', 'font-size': '16px'}
        presWidget.setLabel('left', 'Pressure (bar)', **styles)
        presWidget.setLabel('bottom', 'Time (s)', **styles)

        self.x = list(range(100))  # 100 time points
        self.y = [0] * 100  # 100 data points


        pen = pg.mkPen(color=(0, 255, 0))
        self.data_line = presWidget.plot(self.x, self.y, pen=pen)

    def start_measure(self):
        if not self.timer2.isActive():
            self.timer2.start()

    def stop_measure(self):
        if self.timer2.isActive():
            self.timer2.stop()

    def update_plot_data(self):
        arduinoString = arduinoData.readline()  # read the line of text from the serial port
        dataArray = arduinoString.split(b',')  # Split it into an array called dataArray
        temp = float(dataArray[0])  # Convert first element to floating number and put in temp
        P = float(dataArray[1])  # Convert second element to floating number and put in P
        tempC.append(temp)  # Build our tempF array by appending temp readings
        pressure.append(P)  # Building our pressure array by appending P readings

        self.x = self.x[1:]  # Remove the first y element.
        self.x.append(self.x[-1] + 1)  # Add a new value 1 higher than the last.

        self.y = self.y[1:]  # Remove the first
        self.y.append(P)  # Add new pressure value

        self.data_line.setData(self.x, self.y)  # Update the data.