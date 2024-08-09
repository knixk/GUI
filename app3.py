import sys
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

size = 1000

# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("My App")
    button = QPushButton("Press Me!")
    self.setFixedSize(QSize(size, size)) 
    # Set the central widget of the Window.
    self.setCentralWidget(button)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()