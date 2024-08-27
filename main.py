import sys

from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt

from view.main_window import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setAttribute(Qt.ApplicationAttribute.AA_DontCreateNativeWidgetSiblings)
    w = MainWindow()
    w.show()
    app.exec()
