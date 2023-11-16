#--------------------------------------------------------------------------------------------------------------------------------------
# Name:                  Exam4_Ledbetter.py
# Purpose:               Provide an empty working example Qt GUI App.
#                        template.
# Notes:                 Requires that PyQt6 be installed in Thonny using Tools, Manage Packages.
# Additional Files:      This program loads gui_template.ui which MUST be in the same folder as
#                        this Python program. 
#
# Author:                Tiffany Ledbetter
#
# Created:               10/29/2023
#-------------------------------------------------------------------------------------------------------------------------------------
import sys                        # needed for the sys.argv passed to QApplication below (command line arguments)

from PyQt6.QtWidgets import QDialog, QApplication, QCalendarWidget
from PyQt6.uic import loadUi
from PyQt6.QtCore import QDate
# special library to load .ui file directly

class MyForm(QDialog):
    # constructor for this MyForm class 
    def __init__(self):
        super().__init__()   # calls the constructor of the QDialog class that is inherited
        
        # Change 'gui_template.ui' to the .ui file you created with Qt Designer
        # or rename the provided gui_template.ui to your own file and change name
        # the .ui file MUST BE IN THE SAME FOLDER AS THIS .PY FILE
        self.ui = loadUi('Exam4_Ledbetter.ui', self)   #<======= this line must be changed to your .UI file!
        
        self.ui.pushButtonExit.clicked.connect( self.exitMethod)
        self.ui.pushButtonConvert.clicked.connect( self.convertMethod)
        self.ui.calendarWidget.selectionChanged.connect(self.convertMethod)
        # add code here to connect the pushButton widgets to your methods.
        # for this first project three empty methods are already created.
        # you are responsible for connecting the clicked signal from your widgets
        
    def convertMethod(self):
        selectedDate = self.ui.calendarWidget.selectedDate()
        julianDate = selectedDate.toJulianDay()
        formatJulianDate = ('{:,}'.format(julianDate))
        self.ui.labelJulianDate.setText(formatJulianDate)
        
    def exitMethod(self):
        # the following code quits the application.
        # It is connected to the Exit push button in the
        # constructor above.
        QApplication.instance().quit()

# the code below should not be changed and is constant for all GUI programs
if __name__=="__main__":    
    app = QApplication(sys.argv)
    window = MyForm()
    window.show()         
    sys.exit(app.exec())  # note - sys.exit causes traceback in some editors if it does in yours just use app.exec()
