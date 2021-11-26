from database import setup
from PySide2.QtWidgets import QApplication
from controllers.mainwindow import MainWindow
import sys

setup.create_tables()

app = QApplication()
window = MainWindow()
window.show()

sys.exit(app.exec_())

""" if __name__ == "__main__":
    pass """
