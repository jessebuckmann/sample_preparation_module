import sys, AD2Sensor
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

class Overview(QWidget):
    def __init__(self):
        super().__init__()
