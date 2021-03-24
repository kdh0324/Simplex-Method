import sys
from PyQt5.QtWidgets import *


class SoftwareUI(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.resize(400, 150)
        self.setWindowTitle('Simplex Method')
        self.set_center()
        self.show()

    def set_center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def coefficient_box(self):
        new_variable = QLineEdit(self)

    # def coefficient_changed(self, text):


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SoftwareUI()
    sys.exit(app.exec_())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
