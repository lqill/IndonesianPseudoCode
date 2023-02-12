# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'editorHFynCc.ui'
##
## Created by: Qt User Interface Compiler version 5.15.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actionNew = QAction(MainWindow)
        self.actionNew.setObjectName(u"actionNew")
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionSave_as = QAction(MainWindow)
        self.actionSave_as.setObjectName(u"actionSave_as")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.output = QTextBrowser(self.centralwidget)
        self.output.setObjectName(u"output")
        self.output.setGeometry(QRect(420, 240, 361, 311))
        self.table1 = QTableWidget(self.centralwidget)
        self.table1.setObjectName(u"table1")
        self.table1.setGeometry(QRect(420, 60, 361, 161))
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 30, 411, 521))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.edit1 = QPlainTextEdit(self.tab)
        self.edit1.setObjectName(u"edit1")
        self.edit1.setGeometry(QRect(0, 0, 411, 491))
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.button1 = QPushButton(self.centralwidget)
        self.button1.setObjectName(u"button1")
        self.button1.setGeometry(QRect(750, 10, 31, 23))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 20))
        self.menuNew = QMenu(self.menubar)
        self.menuNew.setObjectName(u"menuNew")
        self.menuRun = QMenu(self.menubar)
        self.menuRun.setObjectName(u"menuRun")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuNew.menuAction())
        self.menubar.addAction(self.menuRun.menuAction())
        self.menuNew.addAction(self.actionNew)
        self.menuNew.addAction(self.actionOpen)
        self.menuNew.addAction(self.actionSave)
        self.menuNew.addAction(self.actionSave_as)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionNew.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open [Ctrl+O]", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save [Ctrl+S]", None))
        self.actionSave_as.setText(QCoreApplication.translate("MainWindow", u"Save as [Ctrl+Shift+S]", None))
        self.edit1.setPlainText(QCoreApplication.translate("MainWindow", u"#DEKLARASI\n"
"\n"
"#INTRUKSI", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tab 2", None))
        self.button1.setText(QCoreApplication.translate("MainWindow", u"Run", None))
        self.menuNew.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuRun.setTitle(QCoreApplication.translate("MainWindow", u"Run (F5)", None))
    # retranslateUi

