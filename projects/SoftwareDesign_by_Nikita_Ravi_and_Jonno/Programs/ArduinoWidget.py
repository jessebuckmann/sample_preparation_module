# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 20:53:59 2020

@author: j.schoppink
"""

from PyQt5 import QtWidgets, QtCore
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys  # We need sys so that we can pass argv to QApplication
import os
from random import randint
import serial  # import Serial Library
import numpy  # Import numpy

tempC = []
pressure = []
arduinoData = serial.Serial('COM3', 9600)  # Creating our serial object named arduinoData

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        
        
        super(MainWindow, self).__init__(*args, **kwargs)

        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)

        arduinoString = arduinoData.readline()  # read the line of text from the serial port
        dataArray = arduinoString.split(b',')  # Split it into an array called dataArray
        temp = float(dataArray[0])  # Convert first element to floating number and put in temp
        P = float(dataArray[1])  # Convert second element to floating number and put in P
        tempC.append(temp)  # Build our tempF array by appending temp readings
        pressure.append(P)  # Building our pressure array by appending P readings

        styles = {'color':'r', 'font-size':'20px'}
        self.graphWidget.setLabel('left', 'Temperature (°C)', **styles)
        self.graphWidget.setLabel('bottom', 'Time', **styles)
        
        self.x = list(range(100))  # 100 time points
        self.y = [0] * 100 # 100 data points

        self.graphWidget.setBackground('w')

        pen = pg.mkPen(color=(255, 0, 0))
        self.data_line =  self.graphWidget.plot(self.x, self.y, pen=pen)
        
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


app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec_())
