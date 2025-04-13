# -*- coding: utf-8 -*-
from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
from numpy import arange, sin, cos, pi
import pyqtgraph as pg
import sys

class Plot2D():
    def __init__(self):
        self.traces = dict()

        #QtGui.QApplication.setGraphicsSystem('raster')
        #self.app = QtGui.QApplication([])
        self.app = pg.mkQApp()
        #mw = QtGui.QMainWindow()
        #mw.resize(800,800)

        #self.win = pg.GraphicsWindow(title="Basic plotting examples")
        self.win = pg.GraphicsLayoutWidget(show=True, title="Basic plotting examples")
        self.win.resize(1000,600)
        self.win.setWindowTitle('pyqtgraph example: Plotting')

        # Enable antialiasing for prettier plots
        pg.setConfigOptions(antialias=True)

        self.canvas = self.win.addPlot(title="Pytelemetry")

    def start(self):
        if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
            #QtGui.QApplication.instance().exec_()
            pg.exec()

    def trace(self,name,dataset_x,dataset_y):
        if name in self.traces:
            self.traces[name].setData(dataset_x,dataset_y)
        else:
            self.traces[name] = self.canvas.plot(pen='y')

## Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    p = Plot2D()
    i = 0

    def update():
        global p, i
        t = np.arange(0,3.0,0.01)
        s = sin(2 * pi * t + i)
        c = cos(2 * pi * t + i)
        p.trace("sin",t,s)
        p.trace("cos",t,c)
        i += 0.1

    timer = QtCore.QTimer()
    timer.timeout.connect(update)
    timer.start(50)

    p.start()


#https://pyqtgraph.readthedocs.io/en/latest/getting_started/qtcrashcourse.html#events-overview

from PyQt6 import QtWidgets  # Should work with PyQt5 / PySide2 / PySide6 as well
import pyqtgraph as pg

# Always start by initializing Qt (only once per application)
app = QtWidgets.QApplication([])

# Define a top-level widget to hold everything
w = QtWidgets.QWidget()
w.setWindowTitle('PyQtGraph example')

# Create some widgets to be placed inside
btn = QtWidgets.QPushButton('press me')
text = QtWidgets.QLineEdit('enter text')
listWidget = QtWidgets.QListWidget()
plot = pg.PlotWidget()

# Create a grid layout to manage the widgets size and position
layout = QtWidgets.QGridLayout()
w.setLayout(layout)

# Add widgets to the layout in their proper positions
layout.addWidget(btn, 0, 0)  # button goes in upper-left
layout.addWidget(text, 1, 0)  # text edit goes in middle-left
layout.addWidget(listWidget, 2, 0)  # list widget goes in bottom-left
layout.addWidget(plot, 0, 1, 3, 1)  # plot goes on right side, spanning 3 rows
# Display the widget as a new window
w.show()

# Start the Qt event loop
app.exec()  # or app.exec_() for PyQt5 / PySide2