import sys
import PySide
from PySide.QtCore import *
from PySide.QtGui import *

app=QApplication(sys.argv)

# label=QLabel("Hola mundo")
# label.show()

# txt=QLineEdit()
# txt.show()

# radio=QRadioButton()
# radio.show()
calendar=QCalendarWidget()
calendar.show()
# calendar.setGridVisible(False)
sys.exit(app.exec_())