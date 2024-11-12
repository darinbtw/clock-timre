import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLayout, QPushButton, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.unitGUI()
    
    def unitGUI(self):
        self.setWindowTitle("Таймер")
        self.setGeometry(100, 100, 300, 200)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())