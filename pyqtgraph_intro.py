"""Example PyQtGraph Integration Into Qt"""
"""https://pyqtgraph.readthedocs.io/en/latest/getting_started/qtcrashcourse.html"""


# from PyQt6 import QtWidgets  # Should work with PyQt5 / PySide2 / PySide6 as well
# import pyqtgraph as pg
# from PyQt6.QtCore import pyqtSlot

# # Always start by initializing Qt (only once per application)
# app = QtWidgets.QApplication([])

# # Define a top-level widget to hold everything
# w = QtWidgets.QWidget()
# w.setWindowTitle('PyQtGraph example')

# # Create some widgets to be placed inside
# btn = QtWidgets.QPushButton('press me')
# text = QtWidgets.QLineEdit('enter text')
# listWidget = QtWidgets.QListWidget()
# listWidget.addItem('l')
# plot = pg.PlotWidget()


# # Create a grid layout to manage the widgets size and position
# layout = QtWidgets.QGridLayout()
# w.setLayout(layout)

# # Add widgets to the layout in their proper positions
# layout.addWidget(btn, 0, 0)  # button goes in upper-left
# layout.addWidget(text, 1, 0)  # text edit goes in middle-left
# layout.addWidget(listWidget, 2, 0)  # list widget goes in bottom-left
# layout.addWidget(plot, 0, 1, 3, 1)  # plot goes on right side, spanning 3 rows

# # Display the widget as a new window
# w.show()

# # Start the Qt event loop
# app.exec()  # or app.exec_() for PyQt5 / PySide2


# from PyQt6.QtWidgets import QApplication, QMainWindow
# from PyQt6.QtCore import Qt

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         # Set the Title of the window
#         self.setWindowTitle('Mouse and Keyboard Event Demo')
#         # Set the position and size of the window
#         self.setGeometry(100, 100, 400, 300)

#     # This method checks if the left mouse button was pressed on the widget
#     # and prints the position of the click.
#     def mousePressEvent(self, event):
#         if event.button() == Qt.MouseButton.LeftButton:
#             print("Left mouse button pressed at:", event.position())

# # Initialize the QApplication
# app = QApplication([])
# window = MainWindow() 
# window.show()
# app.exec()  # Start the event loop

##########################################################################################################################

# from PyQt6.QtWidgets import QApplication, QWidget, QPushButton
# from PyQt6.QtCore import pyqtSlot

# class App(QWidget):

#     def __init__(self):
#         super().__init__()
#         self.title = 'PyQt5 button'
#         self.left = 10
#         self.top = 10
#         self.width = 320
#         self.height = 200
#         self.initUI()
    
#     def initUI(self):
#         self.setWindowTitle(self.title)
#         self.setGeometry(self.left, self.top, self.width, self.height)
        
#         button = QPushButton('PyQt5 button', self)
#         button.setToolTip('This is an example button')
#         button.move(100,70)
#         button.clicked.connect(self.on_click)
        
#         self.show()

#     @pyqtSlot()
#     def on_click(self):
#         print('PyQt5 button click')

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = App()
#     sys.exit(app.exec_())

#######################################################################################################################

#from PyQt6.QtWidgets import QApplication, QWidget, QPushButton
from PyQt6 import QtWidgets as qw
from PyQt6.QtCore import pyqtSlot

# class Window(QWidget):
class Window(qw.QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(100,100,600,500)
        self.setWindowTitle('Test')

        self.btn = qw.QPushButton('press me', self) 
        self.btn.clicked.connect(self.click)        

    @pyqtSlot()
    def click(self):
        print("Left mouse button pressed at:")

myApp = qw.QApplication([])
myWindow = Window()
myWindow.show()
myApp.exec()


import sys
from PyQt6.QtWidgets import QApplication, QWidget, QComboBox, QVBoxLayout

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QComboBox Example")
        
        self.combo = QComboBox()
        self.combo.addItems(["Item 1", "Item 2", "Item 3"])
        self.combo.currentIndexChanged.connect(self.selectionchange)

        layout = QVBoxLayout()
        layout.addWidget(self.combo)
        self.setLayout(layout)
        

    def selectionchange(self, i):
         print(f"Items in the list are : {self.combo.count()}")
         print(f"Current index {i} selection changed , text='{self.combo.currentText()}'")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())