from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QLabel, QVBoxLayout, QDesktopWidget, QHBoxLayout
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QIcon

import sys

from Resources.Icons import icons_rc

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)
        
        screen_size = QDesktopWidget().screenGeometry().size()
        
        window_width = int(screen_size.width() * 0.75)
        window_height = int(screen_size.height() * 0.75)
        
        window_x = (screen_size.width() - window_width) // 2
        window_y = (screen_size.height() - window_height) // 2
        
        self.setGeometry(window_x, window_y, window_width, window_height)
        
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        
        main_layout = QVBoxLayout(central_widget)
        main_layout.setSpacing(0)
        main_layout.setContentsMargins(0, 0, 0, 0)
        
        self.window_widget = QWidget(central_widget)
        self.window_widget.setStyleSheet("""
            background: grey;
        """)
        main_layout.addWidget(self.window_widget)
        
        window_layout = QHBoxLayout(self.window_widget)
        window_layout.setSpacing(0)
        window_layout.setContentsMargins(0, 0, 0, 0)
        
        window_logo = QPushButton(self.window_widget)
        window_logo.setIcon(QIcon("Resources/Icons/cart.svg"))
        window_logo.setStyleSheet("""
            border: none;
        """)
        window_layout.addWidget(window_logo)
        
        title = "Custom Window"
        window_title = QLabel(title, self.window_widget)
        window_title.setAlignment(Qt.AlignCenter)
        window_layout.addWidget(window_title)
        
        minimize_button = QPushButton(self.window_widget)
        minimize_button.setIcon(QIcon("Resources/Icons/minimize.svg"))
        minimize_button.setStyleSheet("""
            border: none;
        """)
        minimize_button.clicked.connect(self.minimizeWindow)
        window_layout.addWidget(minimize_button)
        
        maximize_button = QPushButton(self.window_widget)
        maximize_button.setIcon(QIcon("Resources/Icons/maximize.svg"))
        maximize_button.setStyleSheet("""
            border: none;
        """)
        maximize_button.clicked.connect(self.maximizeWindow)
        window_layout.addWidget(maximize_button)
        
        close_button = QPushButton(self.window_widget)
        close_button.setIcon(QIcon("Resources/Icons/close.svg"))
        close_button.setStyleSheet("""
            border: none;
        """)
        close_button.clicked.connect(self.closeWindow)
        window_layout.addWidget(close_button)
        
        self.content_widget = QWidget(central_widget)
        self.content_widget.setStyleSheet("""
            background: lightgrey;
        """)
        main_layout.addWidget(self.content_widget)
        
        window_layout.setStretch(0, 1)
        window_layout.setStretch(1, 26)
        window_layout.setStretch(2, 1)
        window_layout.setStretch(3, 1)
        window_layout.setStretch(4, 1)
        
        main_layout.setStretch(0, 2)
        main_layout.setStretch(1, 38)
        
        self.dragging = False
        self.offset = QPoint(0, 0)
        
    def maximizeWindow(self):
        if not self.isMaximized():
            self.showMaximized()
        else:
            self.showNormal()
        
    def minimizeWindow(self):
        self.showMinimized()
        
    def closeWindow(self):
        QApplication.quit()
    
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton and self.window_widget.geometry().contains(event.pos()):
            self.dragging = True
            self.offset = event.globalPos() - self.pos()
            
    def mouseMoveEvent(self, event):
        if self.dragging:
            self.move(event.globalPos() - self.offset)
            
    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragging = False
        
def main():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()