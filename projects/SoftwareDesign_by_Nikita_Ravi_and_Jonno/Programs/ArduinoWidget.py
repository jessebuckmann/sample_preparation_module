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
        tempWidget = pg.PlotWidget(name='Plot1')  ## giving the plots names allows us to link their axes together
        layout.addWidget(tempWidget)

        arduinoString = arduinoData.readline()  # read the line of text from the serial port
        dataArray = arduinoString.split(b',')  # Split it into an array called dataArray
        temp = float(dataArray[0])  # Convert first element to floating number and put in temp
        P = float(dataArray[1])  # Convert second element to floating number and put in P
        tempC.append(temp)  # Build our tempF array by appending temp readings
        pressure.append(P)  # Building our pressure array by appending P readings

        styles = {'color': 'w', 'font-size': '20px'}
        tempWidget.setLabel('left', 'Temperature (°C)', **styles)
        tempWidget.setLabel('bottom', 'Time (s)', **styles)

        self.x = list(range(100))  # 100 time points
        self.y = [0] * 100  # 100 data points


        pen = pg.mkPen(color=(255, 0, 0))
        self.data_line = tempWidget.plot(self.x, self.y, pen=pen)

        self.timer = QtCore.QTimer()
        self.timer.setInterval(50)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start()

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
        presWidget = pg.PlotWidget(name='Plot1')  ## giving the plots names allows us to link their axes together
        layout.addWidget(presWidget)

        arduinoString = arduinoData.readline()  # read the line of text from the serial port
        dataArray = arduinoString.split(b',')  # Split it into an array called dataArray
        temp = float(dataArray[0])  # Convert first element to floating number and put in temp
        P = float(dataArray[1])  # Convert second element to floating number and put in P
        tempC.append(temp)  # Build our tempF array by appending temp readings
        pressure.append(P)  # Building our pressure array by appending P readings

        styles = {'color': 'w', 'font-size': '20px'}
        presWidget.setLabel('left', 'Temperature (°C)', **styles)
        presWidget.setLabel('bottom', 'Time (s)', **styles)

        self.x = list(range(100))  # 100 time points
        self.y = [0] * 100  # 100 data points


        pen = pg.mkPen(color=(255, 0, 0))
        self.data_line = presWidget.plot(self.x, self.y, pen=pen)

        self.timer = QtCore.QTimer()
        self.timer.setInterval(50)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start()

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