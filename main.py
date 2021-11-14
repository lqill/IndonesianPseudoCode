from interpreter import Interpreter
from editor import Ui_MainWindow
from PyQt5 import QtWidgets


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    interpreter = Interpreter()
    ui.button1.clicked.connect(lambda: ui.output.clear())
    ui.button1.clicked.connect(lambda: interpreter.run(ui.edit1.toPlainText()))
    ui.button1.clicked.connect(lambda: ui.output.append(interpreter.output))

    # ui.button1.clicked.connect(interpreter.run())
    # "#Deklarasi\nString kalimat\n#Intruksi\nkalimat = \"teks\"\nCetak kalimat"

    MainWindow.show()
    sys.exit(app.exec_())
