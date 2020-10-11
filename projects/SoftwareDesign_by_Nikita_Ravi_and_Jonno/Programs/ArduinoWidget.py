from PyQt5 import QtGui
import pyqtgraph as pg  # used for additional plotting features
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtCore
import serial  # import Serial Library

tempC = [0]
pressure = [0]
arduinoData = serial.Serial('COM5', 9600)  # Change the COMX here to the one your device uses to communicate


class TempSensor(QWidget):
    def _init_(self, parent=None):
        super()._init_(parent)
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

        styles = {'color': '#FFFFFF', 'font-size': '16px'}
        tempWidget.setLabel('left', 'Temperature (°C)', **styles)
        tempWidget.setLabel('bottom', 'Time (s)', **styles)

        self.x = list()  # 100 time points
        for i in range(100):
            self.x.append(i / 100000000)

        self.y = [0] * 100  # 100 data points

        pen = pg.mkPen(color=(255, 0, 0))
        self.data_line = tempWidget.plot(self.x, self.y, pen=pen)

    def start_measure(self):
        self.timer.setInterval(50)
        if not self.timer.isActive():
            self.timer.timeout.connect(self.update_plot_data)
            self.timer.start()

    def stop_measure(self):
        if self.timer.isActive():
            self.timer.stop()

    def update_plot_data(self):
        arduinoString = arduinoData.readline()  # read the line of text from the serial port
        dataArray = arduinoString.split(b',')  # Split it into an array called dataArray
        time = float(dataArray[0])
        temp = float(dataArray[1])  # Convert first element to floating number and put in temp
        tempC.append(temp)  # Build our tempF array by appending temp readings

        self.x = self.x[1:]  # Remove the first y element.
        self.x.append(time / 1000)  # Add a new value 1 higher than the last.

        self.y = self.y[1:]  # Remove the first
        self.y.append(temp)  # Add new temperature value

        self.data_line.setData(self.x, self.y)  # Update the data.


class PresSensor(QWidget):
    def _init_(self, parent=None):
        super()._init_(parent)
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

        layout.addWidget(presWidget)
        layout.addWidget(box_monitor)

        styles = {'color': '#FFFFFF', 'font-size': '16px'}
        presWidget.setLabel('left', 'Pressure (bar)', **styles)
        presWidget.setLabel('bottom', 'Time (s)', **styles)

        self.x1 = list()  # 100 time points
        for i in range(100):
            self.x1.append(i / 100000000)

        self.y1 = [0] * 100  # 100 data points

        pen = pg.mkPen(color=(0, 255, 0))
        self.data_line = presWidget.plot(self.x1, self.y1, pen=pen)

    def start_measure(self):
        self.timer2.setInterval(50)

        if not self.timer2.isActive():
            self.timer2.timeout.connect(self.update_plot_data)
            self.timer2.start()

    def stop_measure(self):
        if self.timer2.isActive():
            self.timer2.stop()

    def update_plot_data(self):
        arduinoString = arduinoData.readline()  # read the line of text from the serial port
        dataArray = arduinoString.split(b',')  # Split it into an array called dataArray
        time = float(dataArray[0])
        P = float(dataArray[2])  # Convert second element to floating number and put in P
        pressure.append(P)  # Building our pressure array by appending P readings

        self.x1 = self.x1[1:]  # Remove the first y element.
        self.x1.append(time / 1000)  # Add a new value 1 higher than the last.

        self.y1 = self.y1[1:]  # Remove the first
        self.y1.append(P)  # Add new pressure value

        self.data_line.setData(self.x1, self.y1)  # Update the data.