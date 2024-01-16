from interpreter import Interpreter
from editor import Ui_MainWindow
from PySide2 import QtWidgets, QtGui

# TODO: TAMBAHI TOMBOL SAVE OUTPUT
# TODO: Tambah data viewer
# TODO: tambah file operation read write


class UI(Ui_MainWindow):
    def __init__(self, MainWindow: QtWidgets.QApplication) -> None:
        super().__init__()
        self.setupUi(MainWindow)
        self.interpreter = Interpreter()
        self.button1.clicked.connect(self.run)

    def run(self):
        self.output.clear()
        self.interpreter.run(self.edit1.toPlainText())
        self.output.append(self.interpreter.output)

    def file_save(self):
        name = QtGui.QFileDialog.getSaveFileName(self, 'Save File')
        file = open(name, 'w')
        text = self.output.toPlainText()
        file.write(text)
        file.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = UI(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
