import sys
from PyQt6 import QtWidgets as qw

# class Window(QWidget):
class Window(qw.QWidget):
    def __init__(self):
        super().__init__()

        # general window settings
        self.setWindowTitle('Test')
        #self.setGeometry(100,100,600,500)
        layout = qw.QVBoxLayout()
        
        # Widget definitions
        self.btn = qw.QPushButton('press me', self) 
        self.btn.clicked.connect(self.button_pushed)
        layout.addWidget(self.btn)

        self.dropdown = qw.QComboBox()
        self.dropdown.addItems([r"C:\Users\zolse\VSCode Projects\Projects\spec_anlyz\SAINt JHN - Still Mine.wav", "Item 2", "Item 3"])
        self.dropdown.currentIndexChanged.connect(self.selection_change)
        layout.addWidget(self.dropdown)

        
        
        self.setLayout(layout)

    def button_pushed(self):
        print("Left mouse button pressed at:")

    def selection_change(self,i):
        print(f"Number of items in the list are : {self.dropdown.count()}")
        print(f"Selection change, selected item index = {i} : text='{self.dropdown.currentText()}'")


if __name__ == '__main__':
    myApp = qw.QApplication(sys.argv)
    myWindow = Window()
    myWindow.show()
    sys.exit(myApp.exec())


