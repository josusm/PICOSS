# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_fi2.ui'
#
# Created: Mon Jul 22 18:55:56 2019
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(581, 396)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout.addWidget(self.label_4)
        self.line_3 = QtGui.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.verticalLayout.addWidget(self.line_3)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.label_13 = QtGui.QLabel(self.centralwidget)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_13)
        self.sliderFrequency = QtGui.QSlider(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Noto Sans [unknown]"))
        font.setBold(True)
        font.setWeight(75)
        self.sliderFrequency.setFont(font)
        self.sliderFrequency.setMinimum(1)
        self.sliderFrequency.setMaximum(10)
        self.sliderFrequency.setProperty("value", 5)
        self.sliderFrequency.setOrientation(QtCore.Qt.Horizontal)
        self.sliderFrequency.setTickPosition(QtGui.QSlider.TicksBothSides)
        self.sliderFrequency.setTickInterval(1)
        self.sliderFrequency.setObjectName(_fromUtf8("sliderFrequency"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.sliderFrequency)
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_8)
        self.loadedsegmentation = QtGui.QLabel(self.centralwidget)
        self.loadedsegmentation.setText(_fromUtf8(""))
        self.loadedsegmentation.setObjectName(_fromUtf8("loadedsegmentation"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.loadedsegmentation)
        self.loadedMaintrace = QtGui.QLabel(self.centralwidget)
        self.loadedMaintrace.setText(_fromUtf8(""))
        self.loadedMaintrace.setObjectName(_fromUtf8("loadedMaintrace"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.loadedMaintrace)
        self.verticalLayout_4.addLayout(self.formLayout)
        self.line_4 = QtGui.QFrame(self.centralwidget)
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.verticalLayout_4.addWidget(self.line_4)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_14 = QtGui.QLabel(self.centralwidget)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.verticalLayout_3.addWidget(self.label_14)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.formLayout_2 = QtGui.QFormLayout()
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_3)
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_5)
        self.mu1 = QtGui.QDoubleSpinBox(self.centralwidget)
        self.mu1.setSingleStep(0.1)
        self.mu1.setProperty("value", 0.5)
        self.mu1.setObjectName(_fromUtf8("mu1"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.mu1)
        self.mu2 = QtGui.QDoubleSpinBox(self.centralwidget)
        self.mu2.setMaximum(3.0)
        self.mu2.setSingleStep(0.1)
        self.mu2.setProperty("value", 0.5)
        self.mu2.setObjectName(_fromUtf8("mu2"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.mu2)
        self.mu3 = QtGui.QDoubleSpinBox(self.centralwidget)
        self.mu3.setMaximum(3.0)
        self.mu3.setSingleStep(0.1)
        self.mu3.setProperty("value", 0.5)
        self.mu3.setObjectName(_fromUtf8("mu3"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.mu3)
        self.horizontalLayout.addLayout(self.formLayout_2)
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.horizontalLayout.addWidget(self.line_2)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.radioButtonMX = QtGui.QRadioButton(self.centralwidget)
        self.radioButtonMX.setObjectName(_fromUtf8("radioButtonMX"))
        self.verticalLayout_2.addWidget(self.radioButtonMX)
        self.formLayout_3 = QtGui.QFormLayout()
        self.formLayout_3.setObjectName(_fromUtf8("formLayout_3"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_6)
        self.hybridlow = QtGui.QLineEdit(self.centralwidget)
        self.hybridlow.setEnabled(False)
        self.hybridlow.setReadOnly(False)
        self.hybridlow.setObjectName(_fromUtf8("hybridlow"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.FieldRole, self.hybridlow)
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_7)
        self.hybridhigh = QtGui.QLineEdit(self.centralwidget)
        self.hybridhigh.setEnabled(False)
        self.hybridhigh.setObjectName(_fromUtf8("hybridhigh"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.FieldRole, self.hybridhigh)
        self.verticalLayout_2.addLayout(self.formLayout_3)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.buttonCancel = QtGui.QPushButton(self.centralwidget)
        self.buttonCancel.setObjectName(_fromUtf8("buttonCancel"))
        self.horizontalLayout_2.addWidget(self.buttonCancel)
        self.buttonLoad = QtGui.QPushButton(self.centralwidget)
        self.buttonLoad.setObjectName(_fromUtf8("buttonLoad"))
        self.horizontalLayout_2.addWidget(self.buttonLoad)
        self.buttonLoadTrace = QtGui.QPushButton(self.centralwidget)
        self.buttonLoadTrace.setObjectName(_fromUtf8("buttonLoadTrace"))
        self.horizontalLayout_2.addWidget(self.buttonLoadTrace)
        self.buttonComputeSave = QtGui.QPushButton(self.centralwidget)
        self.buttonComputeSave.setObjectName(_fromUtf8("buttonComputeSave"))
        self.horizontalLayout_2.addWidget(self.buttonComputeSave)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Classification Generic Settings</span></p></body></html>", None))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">Loaded Main Trace : </span></p></body></html>", None))
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">Frequency Threshold (1-10 Hz.) : </span></p></body></html>", None))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">Loaded Segmentation Results :  </span></p></body></html>", None))
        self.label_14.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Thresholds Settings</span></p></body></html>", None))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Mu_1 (LF) (-)</span></p></body></html>", None))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Mu_2 (HF) (+)</span></p></body></html>", None))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Mu_3 (ROCK)</span></p></body></html>", None))
        self.radioButtonMX.setText(_translate("MainWindow", "Mixed Frequency", None))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Hybrid low</span></p></body></html>", None))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Hybrid high</span></p></body></html>", None))
        self.buttonCancel.setText(_translate("MainWindow", "Cancel", None))
        self.buttonLoad.setText(_translate("MainWindow", "Load Segmentation", None))
        self.buttonLoadTrace.setText(_translate("MainWindow", "Load Main Trace", None))
        self.buttonComputeSave.setText(_translate("MainWindow", "Compute/Save", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
