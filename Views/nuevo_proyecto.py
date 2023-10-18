# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Views\nuevo_proyecto.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_frm_nuevoProyecto(object):
    def setupUi(self, frm_nuevoProyecto):
        frm_nuevoProyecto.setObjectName("frm_nuevoProyecto")
        frm_nuevoProyecto.resize(440, 300)
        frm_nuevoProyecto.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.btn_box = QtWidgets.QDialogButtonBox(frm_nuevoProyecto)
        self.btn_box.setGeometry(QtCore.QRect(270, 260, 160, 28))
        self.btn_box.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.btn_box.setStyleSheet("bottom: -100%;\n"
"  left: 0;\n"
"  width: 2px;\n"
"  height: 100%;\n"
"  background: rgb(6, 91, 103);\n"
"  color: rgb(255, 255, 255);")
        self.btn_box.setOrientation(QtCore.Qt.Horizontal)
        self.btn_box.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.btn_box.setObjectName("btn_box")
        self.lbl_titulofrm = QtWidgets.QLabel(frm_nuevoProyecto)
        self.lbl_titulofrm.setGeometry(QtCore.QRect(0, 0, 440, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.lbl_titulofrm.setFont(font)
        self.lbl_titulofrm.setStyleSheet("  font-size: 18px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(6, 91, 103);")
        self.lbl_titulofrm.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_titulofrm.setObjectName("lbl_titulofrm")
        self.txt_nombreProyecto = QtWidgets.QLineEdit(frm_nuevoProyecto)
        self.txt_nombreProyecto.setGeometry(QtCore.QRect(10, 48, 420, 32))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.txt_nombreProyecto.setFont(font)
        self.txt_nombreProyecto.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.txt_nombreProyecto.setStyleSheet("width: 100%;\n"
"  padding: 6px;\n"
"  font-size: 12px;\n"
"  color: rgb(6, 91, 103);\n"
"  border: none;\n"
"  outline: none;\n"
"  background: transparent;\n"
"border-bottom: 2px solid rgb(118, 118, 118) ;\n"
"color: rgb(6, 91, 103);")
        self.txt_nombreProyecto.setObjectName("txt_nombreProyecto")
        self.txt_alias = QtWidgets.QLineEdit(frm_nuevoProyecto)
        self.txt_alias.setGeometry(QtCore.QRect(10, 88, 420, 32))
        self.txt_alias.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.txt_alias.setStyleSheet("width: 100%;\n"
"  padding: 6px;\n"
"  font-size: 12px;\n"
"  color: rgb(6, 91, 103);\n"
"  border: none;\n"
"  outline: none;\n"
"  background: transparent;\n"
"border-bottom: 2px solid rgb(118, 118, 118) ;\n"
"color: rgb(6, 91, 103);")
        self.txt_alias.setObjectName("txt_alias")
        self.lbl_contacto = QtWidgets.QLabel(frm_nuevoProyecto)
        self.lbl_contacto.setGeometry(QtCore.QRect(10, 128, 70, 24))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.lbl_contacto.setFont(font)
        self.lbl_contacto.setStyleSheet("  font-size: 12px;\n"
"color: rgb(6, 91, 103);")
        self.lbl_contacto.setObjectName("lbl_contacto")
        self.cbb_contacto = QtWidgets.QComboBox(frm_nuevoProyecto)
        self.cbb_contacto.setGeometry(QtCore.QRect(82, 128, 348, 28))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.cbb_contacto.setFont(font)
        self.cbb_contacto.setStyleSheet(" color: rgb(255, 255, 255);\n"
"    background-color: rgb(6, 91, 103);")
        self.cbb_contacto.setObjectName("cbb_contacto")
        self.cbb_domicilio = QtWidgets.QComboBox(frm_nuevoProyecto)
        self.cbb_domicilio.setGeometry(QtCore.QRect(82, 168, 348, 28))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.cbb_domicilio.setFont(font)
        self.cbb_domicilio.setStyleSheet(" color: rgb(255, 255, 255);\n"
"    background-color: rgb(6, 91, 103);")
        self.cbb_domicilio.setObjectName("cbb_domicilio")
        self.lbl_domicilio = QtWidgets.QLabel(frm_nuevoProyecto)
        self.lbl_domicilio.setGeometry(QtCore.QRect(10, 168, 70, 24))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.lbl_domicilio.setFont(font)
        self.lbl_domicilio.setStyleSheet("  font-size: 12px;\n"
"color: rgb(6, 91, 103);")
        self.lbl_domicilio.setObjectName("lbl_domicilio")
        self.txt_folio = QtWidgets.QLineEdit(frm_nuevoProyecto)
        self.txt_folio.setGeometry(QtCore.QRect(10, 208, 110, 32))
        self.txt_folio.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.txt_folio.setStyleSheet("width: 100%;\n"
"  padding: 6px;\n"
"  font-size: 12px;\n"
"  color: rgb(6, 91, 103);\n"
"  border: none;\n"
"  outline: none;\n"
"  background: transparent;\n"
"border-bottom: 2px solid rgb(118, 118, 118) ;\n"
"color: rgb(6, 91, 103);")
        self.txt_folio.setObjectName("txt_folio")
        self.cbb_documento = QtWidgets.QComboBox(frm_nuevoProyecto)
        self.cbb_documento.setGeometry(QtCore.QRect(300, 208, 130, 24))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.cbb_documento.setFont(font)
        self.cbb_documento.setStyleSheet(" color: rgb(255, 255, 255);\n"
"    background-color: rgb(6, 91, 103);")
        self.cbb_documento.setObjectName("cbb_documento")
        self.lbl_documento = QtWidgets.QLabel(frm_nuevoProyecto)
        self.lbl_documento.setGeometry(QtCore.QRect(214, 208, 80, 24))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.lbl_documento.setFont(font)
        self.lbl_documento.setStyleSheet("  font-size: 12px;\n"
"color: rgb(6, 91, 103);")
        self.lbl_documento.setObjectName("lbl_documento")

        self.retranslateUi(frm_nuevoProyecto)
        #self.btn_box.accepted.connect(frm_nuevoProyecto.accept) # type: ignore
        #self.btn_box.rejected.connect(frm_nuevoProyecto.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(frm_nuevoProyecto)
        frm_nuevoProyecto.setTabOrder(self.txt_nombreProyecto, self.txt_alias)
        frm_nuevoProyecto.setTabOrder(self.txt_alias, self.cbb_contacto)
        frm_nuevoProyecto.setTabOrder(self.cbb_contacto, self.cbb_domicilio)
        frm_nuevoProyecto.setTabOrder(self.cbb_domicilio, self.txt_folio)
        frm_nuevoProyecto.setTabOrder(self.txt_folio, self.cbb_documento)
        frm_nuevoProyecto.setTabOrder(self.cbb_documento, self.btn_box)

    def retranslateUi(self, frm_nuevoProyecto):
        _translate = QtCore.QCoreApplication.translate
        frm_nuevoProyecto.setWindowTitle(_translate("frm_nuevoProyecto", ". . : : Nuevo Proyecto : : . ."))
        self.lbl_titulofrm.setText(_translate("frm_nuevoProyecto", "CREAR PROYECTO"))
        self.txt_nombreProyecto.setPlaceholderText(_translate("frm_nuevoProyecto", "NOMBRE DEL PROYECTO"))
        self.txt_alias.setPlaceholderText(_translate("frm_nuevoProyecto", "ALIAS"))
        self.lbl_contacto.setText(_translate("frm_nuevoProyecto", "CONTACTO"))
        self.lbl_domicilio.setText(_translate("frm_nuevoProyecto", "DOMICILIO"))
        self.txt_folio.setPlaceholderText(_translate("frm_nuevoProyecto", "FOLIO"))
        self.lbl_documento.setText(_translate("frm_nuevoProyecto", "DOCUMENTO"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    frm_nuevoProyecto = QtWidgets.QDialog()
    ui = Ui_frm_nuevoProyecto()
    ui.setupUi(frm_nuevoProyecto)
    frm_nuevoProyecto.show()
    sys.exit(app.exec_())
