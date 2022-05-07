from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5 import QtCore,QtWidgets
from PyQt5.QtWidgets import QApplication,  QFileDialog
from PyQt5.QtGui import QPixmap
from v import v

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(616, 491)
        self.centralwidget = QtWidgets.QWidget(Form)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 80, 300, 300))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(120, 420, 100, 30))
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(390, 80, 200, 300))
        self.textEdit.setObjectName("textEdit")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(330, 420, 100, 30))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.pushButton.clicked.connect(self.openimg)
        self.pushButton_2.clicked.connect(self.open)

    def openimg(self):
        self.img_file, _ = QFileDialog.getOpenFileName(self.centralwidget, 'Open file',
                                                         r'',
                                                         'Image files (*.jpg)')
        self.img = QPixmap(self.img_file)
        self.label.setPixmap(self.img)
        self.label.setScaledContents(True)
    def open(self):
        v1 = v(self.img_file)
        self.textEdit.append('物体体积为：%.2f cm^3'%v1)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "基于opencv的物体体积测量系统"))
        self.label.setText(_translate("Form", "TextLabel"))
        self.pushButton.setText(_translate("Form", "输入图片"))
        self.pushButton_2.setText(_translate("Form", "开始"))
if __name__ == '__main__':
    import PyQt5
    app = QApplication(sys.argv)
    ex = Ui_Form()
    window = PyQt5.QtWidgets.QMainWindow()
    ex.setupUi(window)
    window.show()
    sys.exit(app.exec_())