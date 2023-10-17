# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Views\login.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ViewLogin(object):
    def setupUi(self, ViewLogin):
        ViewLogin.setObjectName("ViewLogin")
        ViewLogin.resize(423, 550)
        self.widget = QtWidgets.QWidget(ViewLogin)
        self.widget.setGeometry(QtCore.QRect(40, 10, 370, 480))
        self.widget.setStyleSheet("QPushButton#pushButton{    \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20, 47, 78, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#pushButton:hover{    \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 226));\n"
"}\n"
"QPushButton#pushButton:pressed{    \n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(105, 118, 132, 200);\n"
"}\n"
"\n"
"QPushButton#pushButton_2, #pushButton_3, #pushButton_4, #pushButton_5{    \n"
"    background-color: rgba(0, 0, 0, 0);\n"
"    color:rgba(85, 98, 112, 255);\n"
"}\n"
"QPushButton#pushButton_2:hover, #pushButton_3:hover, #pushButton_4:hover, #pushButton_5:hover{    \n"
"    color:rgba(155, 168, 182, 220);\n"
"}\n"
"QPushButton#pushButton_2:pressed, #pushButton_3:pressed, #pushButton_4:pressed, #pushButton_5:pressed{    \n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    color:rgba(115, 128, 142, 255);\n"
"}")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(30, 30, 300, 420))
        self.label.setStyleSheet("border-radius:20px;\n"
"background-image: url(:/images/background.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(30, 40, 301, 421))
        self.label_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:0.715909, stop:0 rgba(0, 0, 0, 9), stop:0.375 rgba(0, 0, 0, 50), stop:0.835227 rgba(0, 0, 0, 75));\n"
"background-image: url(:/images/background.png);\n"
"border-radius:20px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_title = QtWidgets.QLabel(self.widget)
        self.label_title.setGeometry(QtCore.QRect(100, 80, 161, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet("color:rgba(255, 255, 255, 210);")
        self.label_title.setObjectName("label_title")
        self.txt_user = QtWidgets.QLineEdit(self.widget)
        self.txt_user.setGeometry(QtCore.QRect(80, 165, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txt_user.setFont(font)
        self.txt_user.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.txt_user.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(105, 118, 132, 255);\n"
"color:rgba(255, 255, 255, 230);\n"
"padding-bottom:7px;")
        self.txt_user.setObjectName("txt_user")
        self.txt_password = QtWidgets.QLineEdit(self.widget)
        self.txt_password.setGeometry(QtCore.QRect(80, 230, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txt_password.setFont(font)
        self.txt_password.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.txt_password.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(105, 118, 132, 255);\n"
"color:rgba(255, 255, 255, 230);\n"
"padding-bottom:7px;")
        self.txt_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txt_password.setObjectName("txt_password")
        self.btn_logear = QtWidgets.QPushButton(self.widget)
        self.btn_logear.setGeometry(QtCore.QRect(80, 330, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_logear.setFont(font)
        self.btn_logear.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.btn_logear.setStyleSheet(" background: linear-gradient(360deg,#03e9f4);")
        self.btn_logear.setObjectName("btn_logear")
        self.label_info = QtWidgets.QLabel(self.widget)
        self.label_info.setEnabled(True)
        self.label_info.setGeometry(QtCore.QRect(140, 379, 101, 41))
        self.label_info.setStyleSheet("color:rgba(255, 255, 255, 210);")
        self.label_info.setObjectName("label_info")
        self.btn_cerrar = QtWidgets.QPushButton(self.widget)
        self.btn_cerrar.setGeometry(QtCore.QRect(280, 40, 41, 31))
        self.btn_cerrar.setStyleSheet("\n"
"outline:none;\n"
"  font-size: 20px;\n"
"  background: transparent;\n"
"color:rgba(255, 255, 255, 210);")
        self.btn_cerrar.setObjectName("btn_cerrar")
        self.btn_mostrar = QtWidgets.QPushButton(self.widget)
        self.btn_mostrar.setGeometry(QtCore.QRect(250, 230, 31, 31))
        self.btn_mostrar.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.btn_mostrar.setStyleSheet("image: url(:/img/ojo.png);\n"
"background-color: transparent;\n"
"")
        self.btn_mostrar.setText("")
        self.btn_mostrar.setObjectName("btn_mostrar")

        self.retranslateUi(ViewLogin)
        QtCore.QMetaObject.connectSlotsByName(ViewLogin)
        ViewLogin.setTabOrder(self.txt_user, self.txt_password)
        ViewLogin.setTabOrder(self.txt_password, self.btn_mostrar)
        ViewLogin.setTabOrder(self.btn_mostrar, self.btn_logear)
        ViewLogin.setTabOrder(self.btn_logear, self.btn_cerrar)

    def retranslateUi(self, ViewLogin):
        _translate = QtCore.QCoreApplication.translate
        ViewLogin.setWindowTitle(_translate("ViewLogin", "login"))
        self.label_title.setText(_translate("ViewLogin", "Assembled"))
        self.txt_user.setPlaceholderText(_translate("ViewLogin", "  Usuario"))
        self.txt_password.setPlaceholderText(_translate("ViewLogin", "Contraseña"))
        self.btn_logear.setText(_translate("ViewLogin", "Aceptar"))
        self.label_info.setText(_translate("ViewLogin", "Datos incorrectos"))
        self.btn_cerrar.setText(_translate("ViewLogin", "X"))
        self.btn_mostrar.setWhatsThis(_translate("ViewLogin", "<html><head/><body><p><br/></p></body></html>"))
import ojo_rc
import res_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ViewLogin = QtWidgets.QWidget()
    ui = Ui_ViewLogin()
    ui.setupUi(ViewLogin)
    ViewLogin.show()
    sys.exit(app.exec_())
