# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'project_gui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalSliderC = QtWidgets.QSlider(self.groupBox)
        self.verticalSliderC.setMaximum(100)
        self.verticalSliderC.setOrientation(QtCore.Qt.Vertical)
        self.verticalSliderC.setObjectName("verticalSliderC")
        self.horizontalLayout.addWidget(self.verticalSliderC)
        self.lineEditC = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditC.setReadOnly(True)
        self.lineEditC.setObjectName("lineEditC")
        self.horizontalLayout.addWidget(self.lineEditC)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalSliderF = QtWidgets.QSlider(self.groupBox_2)
        self.verticalSliderF.setMaximum(23)
        self.verticalSliderF.setOrientation(QtCore.Qt.Vertical)
        self.verticalSliderF.setObjectName("verticalSliderF")
        self.horizontalLayout_2.addWidget(self.verticalSliderF)
        self.lineEditF = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEditF.setReadOnly(True)
        self.lineEditF.setObjectName("lineEditF")
        self.horizontalLayout_2.addWidget(self.lineEditF)
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.gridLayout_3.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Maximum Capacity of the Room"))
        self.label.setText(_translate("MainWindow", "Person(s)"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Time until 100% of Maximum Capacity is Infected"))
        self.label_2.setText(_translate("MainWindow", "Minutes"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

