# import sys
# from PyQt6 import QtWidgets as qw
# import pyqtgraph as pg
# from pyqtgraph.Qt import QtCore, QtGui
# from PyQt6.QtCore import pyqtSlot
# from PyQt6.QtWidgets import QWidget, QVBoxLayout

# # class Window(qw.QWidget):
# class GUI(qw.QWidget):
#     def __init__(self):
#         super().__init__()

#         # general window settings
#         #self.setWindowTitle('Test')
#         #self.setGeometry(100,100,600,500)
#         #layout = qw.QVBoxLayout()
#         #self.app = pg.mkQApp()
#         self.win = pg.GraphicsLayoutWidget(show=True, title="Basic plotting examples")
#         self.win.setWindowTitle('my window')

#         #self.app2 = QtGui.QApplication([])

#         #self.win = pg.GraphicsWindow(title='Spectrum Analyzer')
#         # self.win.resize(1000,600)
#         #self.canvas = self.window.addPlot(title="Pytelemetry")
#         # # Widget definitions
#         self.btn = qw.QPushButton('press me', self) 
#         self.btn.clicked.connect(self.button_pushed)
#         #layout.addWidget(self.btn)

#         # self.dropdown = qw.QComboBox()
#         # self.dropdown.addItems([r"C:\Users\zolse\VSCode Projects\Projects\spec_anlyz\SAINt JHN - Still Mine.wav", "Item 2", "Item 3"])
#         # self.dropdown.currentIndexChanged.connect(self.selection_change)
#         # layout.addWidget(self.dropdown)

        
        
#         #self.setLayout(layout)
#     @pyqtSlot()
#     def button_pushed(self):
#         print("Left mouse button pressed at:")

#     def selection_change(self,i):
#         print(f"Number of items in the list are : {self.dropdown.count()}")
#         print(f"Selection change, selected item index = {i} : text='{self.dropdown.currentText()}'")

#     def start(self):
#         if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
#             #QtGui.QApplication.instance().exec_()
#             pg.exec()

# if __name__ == '__main__':
#     myWinow = GUI()
#     myApp = qw.QApplication([])
#     myApp.exec()


    #app.start()
    #window = Window()

# if __name__ == '__main__':
#     myApp = qw.QApplication(sys.argv)
#     myWindow = Window()
#     myWindow.show()
#     sys.exit(myApp.exec())


import sys
from PyQt6 import QtWidgets as qw
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
from PyQt6.QtCore import pyqtSlot
from PyQt6.QtWidgets import QWidget, QVBoxLayout

# class Window(qw.QWidget):
class GUI(qw.QWidget):
    def __init__(self):
        super().__init__()

        # Define a top-level widget to hold everything
        self.w = qw.QWidget()
        self.w.setWindowTitle('PyQtGraph example')

        # Create some widgets to be placed inside
        self.btn = qw.QPushButton('press me',self)
        self.btn.clicked.connect(self.click)
        self.btn.clicked.connect(self.click2)
        self.text = qw.QLineEdit('enter text')
        self.listWidget = qw.QListWidget()
        self.plot = pg.PlotWidget()

        # Create a grid layout to manage the widgets size and position
        layout = qw.QGridLayout()
        self.w.setLayout(layout)

        # Add widgets to the layout in their proper positions
        layout.addWidget(self.btn, 0, 0)  # button goes in upper-left
        layout.addWidget(self.text, 1, 0)  # text edit goes in middle-left
        layout.addWidget(self.listWidget, 2, 0)  # list widget goes in bottom-left
        layout.addWidget(self.plot, 0, 1, 3, 1)  # plot goes on right side, spanning 3 rows
    
    @pyqtSlot()
    def click(self):
        print("click")

    @pyqtSlot()
    def click2(self):
        print("click2")

if __name__ == '__main__':

    #myApp = qw.QApplication([])
    myApp = qw.QApplication(sys.argv)
    myWindow = GUI()
    myWindow.w.show()
    #myApp.exec()
    sys.exit(myApp.exec())