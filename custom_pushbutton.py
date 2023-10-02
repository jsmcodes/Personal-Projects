import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        
        layout = QVBoxLayout(central_widget)
        
        ### Normal
        
        button = QPushButton("Normal", central_widget)
        layout.addWidget(button)
        
        ### With Icon - Default
        
        button_with_icon = QPushButton(central_widget)
        button_with_icon.setIcon()
        
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()