from PySide6.QtWidgets import (
  QApplication,
  QMainWindow,
  QPushButton,
) 

import sys

class MainWindow(QMainWindow):
  
  def __init__(self):
    super().__init__() 
    self.setWindowTitle("My App")
    button = QPushButton("Press Me!")
    button.setCheckable(True)
    button.clicked.connect(self.the_button_was_clicked)
    # Set the central widget of the Window.
    self.setCentralWidget(button)

  def the_button_was_clicked(self):
    print("Kanishk Clicked me!")

app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()