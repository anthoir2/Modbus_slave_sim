#this is a Modbus TCP slave using PyModbus and PyQT for GUI development 

from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QPushButton, QShortcut, #QShortcut adds in the actions executed when a shortcut is ueed 
                             QLineEdit, QSpinBox, QComboBox, QCheckBox,
                             QGroupBox, QVBoxLayout, QHBoxLayout, QWidget, #QVBox layout addes features for making sections in the GUI
                             QRadioButton, QButtonGroup)


from PyQt5.QtGui import QKeySequence #Qkey sequence has tools used to interpret the sequence of key board short cuts or keys 

from PyQt5.QtCore import Qt

import sys #imports pyhton system tools needed to run the python app and close it among other things TBD 

app = QApplication(sys.argv)

#variables for reference 
window_height = int(1400) #typecasting in python  
window_width = int(1000)

# Create main window
window = QMainWindow()
window.setWindowTitle("Modbus TCP slave simulator")
window.setGeometry(50, 50, 1400, 1000)
window.setStyleSheet("background-color: #000000;")



# Central widget
central_widget = QWidget()
window.setCentralWidget(central_widget)
layout = QVBoxLayout() 


# Info label (contains key shortcut descriptions)
info_label = QLabel("Keyboard Shortcuts:\n\n"
                   "Ctrl+Q or Ctrl+W - Close window\n"
                   "Esc - Close window\n"
                   "Ctrl+R - Connect to Modbus\n"
                   "F5 - Read Data\n"
                   "F6 - Write Data\n"
                   "Ctrl+D - Disconnect")
info_label.setStyleSheet("color: green; font-size: 14px; padding: 20px;")
layout.addWidget(info_label)


status_label = QLabel("Status: Ready")
status_label.setStyleSheet("color: lime; font-size: 16px; font-weight: bold; padding: 20px;")
layout.addWidget(status_label)

central_widget.setLayout(layout)


# Add widgets
label = QLabel("Modbus Slave Simulator", window)
label.move( 700 , 500 )
label.setGeometry(450,10, 450, 50)
label.setStyleSheet("background-color: #00F000; color: white; font-size: 32px; font-weight: bold ; padding: 10px;")


window.show()
sys.exit(app.exec_()) #ENSURES the app exits without running any processes in the background


