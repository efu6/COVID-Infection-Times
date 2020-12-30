from project_gui import *

from math import *

def signals(self):
    # Link the verticalSliders' valueChanged signual
    self.verticalSliderC.valueChanged['int'].connect(self.slider_c)  
    self.verticalSliderF.valueChanged['int'].connect(self.slider_f)

def slider_c(self):
    self.lineEditC.setText(str(self.verticalSliderC.value()))
    f = log(self.verticalSliderC.value())/(.33*.625)
    self.verticalSliderF.setValue(round(f))

def slider_f(self):
    self.lineEditF.setText(str(self.verticalSliderF.value()))
    c = exp(.625*.33*self.verticalSliderF.value())
    self.verticalSliderC.setValue(round(c))

Ui_MainWindow.signals = signals
Ui_MainWindow.slider_c = slider_c
Ui_MainWindow.slider_f = slider_f

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.signals()
    MainWindow.show()
    sys.exit(app.exec_())