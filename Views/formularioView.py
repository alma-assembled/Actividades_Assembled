# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'formulario.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_vfm_registroActs(object):
    def setupUi(self, vfm_registroActs):
        vfm_registroActs.setObjectName("vfm_registroActs")
        vfm_registroActs.resize(752, 684)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(19)
        vfm_registroActs.setFont(font)
        vfm_registroActs.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.vfm_registroActs_body = QtWidgets.QWidget(vfm_registroActs)
        self.vfm_registroActs_body.setObjectName("vfm_registroActs_body")
        self.gridLayoutWidget = QtWidgets.QWidget(self.vfm_registroActs_body)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 2, 2))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.txt_tiempo = QtWidgets.QLineEdit(self.vfm_registroActs_body)
        self.txt_tiempo.setGeometry(QtCore.QRect(170, 328, 50, 32))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txt_tiempo.setFont(font)
        self.txt_tiempo.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.txt_tiempo.setStyleSheet("width: 100%;\n"
"  padding: 10px 0;\n"
"  font-size: 12px;\n"
"  color: rgb(6, 91, 103);\n"
"  border: none;\n"
"  outline: none;\n"
"  background: transparent;\n"
"border-bottom: 2px solid rgb(118, 118, 118) ;\n"
"color: rgb(6, 91, 103);")
        self.txt_tiempo.setText("")
        self.txt_tiempo.setObjectName("txt_tiempo")
        self.txt_op = QtWidgets.QLineEdit(self.vfm_registroActs_body)
        self.txt_op.setGeometry(QtCore.QRect(170, 74, 130, 32))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txt_op.setFont(font)
        self.txt_op.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.txt_op.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.txt_op.setStyleSheet("width: 100%;\n"
"  padding: 10px 0;\n"
"  font-size: 12px;\n"
"  color: rgb(6, 91, 103);\n"
"  border: none;\n"
"  outline: none;\n"
"  background: transparent;\n"
"border-bottom: 2px solid rgb(118, 118, 118) ;\n"
"color: rgb(6, 91, 103);")
        self.txt_op.setText("")
        self.txt_op.setFrame(True)
        self.txt_op.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.txt_op.setObjectName("txt_op")
        self.frm_left = QtWidgets.QFrame(self.vfm_registroActs_body)
        self.frm_left.setEnabled(True)
        self.frm_left.setGeometry(QtCore.QRect(0, 0, 160, 670))
        self.frm_left.setStyleSheet("background-color: rgb(6, 91, 103);")
        self.frm_left.setObjectName("frm_left")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frm_left)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lbl_logoAayn = QtWidgets.QLabel(self.frm_left)
        self.lbl_logoAayn.setStyleSheet("image: url(:/logoAayn/Logo_Verical_Blanco.png);\n"
"margin-top: -514px;")
        self.lbl_logoAayn.setText("")
        self.lbl_logoAayn.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lbl_logoAayn.setObjectName("lbl_logoAayn")
        self.horizontalLayout.addWidget(self.lbl_logoAayn)
        self.lbl_nombre = QtWidgets.QLabel(self.vfm_registroActs_body)
        self.lbl_nombre.setGeometry(QtCore.QRect(170, 40, 561, 24))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lbl_nombre.setFont(font)
        self.lbl_nombre.setFocusPolicy(QtCore.Qt.NoFocus)
        self.lbl_nombre.setToolTip("")
        self.lbl_nombre.setToolTipDuration(1)
        self.lbl_nombre.setStyleSheet("font: 12px \"Arial\";\n"
"color: rgb(6, 91, 103);\n"
"")
        self.lbl_nombre.setObjectName("lbl_nombre")
        self.txt_cliente = QtWidgets.QLineEdit(self.vfm_registroActs_body)
        self.txt_cliente.setEnabled(False)
        self.txt_cliente.setGeometry(QtCore.QRect(300, 74, 440, 32))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txt_cliente.setFont(font)
        self.txt_cliente.setFocusPolicy(QtCore.Qt.NoFocus)
        self.txt_cliente.setStyleSheet("width: 100%;\n"
"  padding: 10px 0;\n"
"  font-size: 12px;\n"
"  color: rgb(6, 91, 103);\n"
"  border: none;\n"
"  outline: none;\n"
"  background: transparent;\n"
"border-bottom: 2px solid rgb(118, 118, 118) ;\n"
"color: rgb(6, 91, 103);")
        self.txt_cliente.setText("")
        self.txt_cliente.setObjectName("txt_cliente")
        self.lbl_departamento = QtWidgets.QLabel(self.vfm_registroActs_body)
        self.lbl_departamento.setGeometry(QtCore.QRect(170, 180, 100, 24))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_departamento.setFont(font)
        self.lbl_departamento.setStyleSheet("  font-size: 12px;\n"
"color: rgb(6, 91, 103);;")
        self.lbl_departamento.setObjectName("lbl_departamento")
        self.lbl_actividad = QtWidgets.QLabel(self.vfm_registroActs_body)
        self.lbl_actividad.setGeometry(QtCore.QRect(170, 242, 72, 24))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_actividad.setFont(font)
        self.lbl_actividad.setStyleSheet("  font-size: 12px;\n"
"color: rgb(6, 91, 103);")
        self.lbl_actividad.setObjectName("lbl_actividad")
        self.cbb_actividad = QtWidgets.QComboBox(self.vfm_registroActs_body)
        self.cbb_actividad.setGeometry(QtCore.QRect(170, 272, 460, 28))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.cbb_actividad.setFont(font)
        self.cbb_actividad.setStyleSheet(" color: rgb(255, 255, 255);\n"
"    background-color: rgb(6, 91, 103);")
        self.cbb_actividad.setObjectName("cbb_actividad")
        self.btn_actividad = QtWidgets.QPushButton(self.vfm_registroActs_body)
        self.btn_actividad.setGeometry(QtCore.QRect(656, 272, 84, 28))
        self.btn_actividad.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.btn_actividad.setStyleSheet(" background:rgb(6, 91, 103);\n"
"color: rgb(255, 255, 255);")
        self.btn_actividad.setObjectName("btn_actividad")
        self.rbt_horas = QtWidgets.QRadioButton(self.vfm_registroActs_body)
        self.rbt_horas.setGeometry(QtCore.QRect(240, 310, 60, 24))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        self.rbt_horas.setFont(font)
        self.rbt_horas.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.rbt_horas.setStyleSheet("color: rgb(6, 91, 103);\n"
"indicator { background-color: red; }")
        self.rbt_horas.setObjectName("rbt_horas")
        self.rbt_minutos = QtWidgets.QRadioButton(self.vfm_registroActs_body)
        self.rbt_minutos.setGeometry(QtCore.QRect(240, 340, 70, 24))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.rbt_minutos.setFont(font)
        self.rbt_minutos.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.rbt_minutos.setStyleSheet("color: rgb(6, 91, 103);\n"
"indicator { background-color: red; }")
        self.rbt_minutos.setObjectName("rbt_minutos")
        self.btn_guardar = QtWidgets.QPushButton(self.vfm_registroActs_body)
        self.btn_guardar.setGeometry(QtCore.QRect(600, 630, 140, 28))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.btn_guardar.setFont(font)
        self.btn_guardar.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.btn_guardar.setStyleSheet("color: rgb(255, 255, 255);\n"
" background: rgb(6, 91, 103);\n"
"")
        self.btn_guardar.setObjectName("btn_guardar")
        self.btn_agregaAct = QtWidgets.QPushButton(self.vfm_registroActs_body)
        self.btn_agregaAct.setGeometry(QtCore.QRect(600, 328, 141, 28))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        self.btn_agregaAct.setFont(font)
        self.btn_agregaAct.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.btn_agregaAct.setStyleSheet("color: rgb(255, 255, 255);\n"
"  background: rgb(6, 91, 103);")
        self.btn_agregaAct.setObjectName("btn_agregaAct")
        self.btn_quitar = QtWidgets.QPushButton(self.vfm_registroActs_body)
        self.btn_quitar.setGeometry(QtCore.QRect(170, 630, 60, 28))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.btn_quitar.setFont(font)
        self.btn_quitar.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.btn_quitar.setStyleSheet("color: rgb(255,255,255);\n"
" background: rgb(6, 91, 103);")
        self.btn_quitar.setObjectName("btn_quitar")
        self.cbb_departamento = QtWidgets.QComboBox(self.vfm_registroActs_body)
        self.cbb_departamento.setGeometry(QtCore.QRect(170, 210, 460, 28))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.cbb_departamento.setFont(font)
        self.cbb_departamento.setStyleSheet(" color: rgb(255, 255, 255);\n"
"    background-color: rgb(6, 91, 103);")
        self.cbb_departamento.setObjectName("cbb_departamento")
        self.dte_fechoy = QtWidgets.QDateEdit(self.vfm_registroActs_body)
        self.dte_fechoy.setEnabled(False)
        self.dte_fechoy.setGeometry(QtCore.QRect(640, 6, 100, 24))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.dte_fechoy.setFont(font)
        self.dte_fechoy.setFocusPolicy(QtCore.Qt.NoFocus)
        self.dte_fechoy.setStyleSheet(" color: rgb(6, 91, 103);\n"
"   background: linear-gradient(360deg,#03e9f4);")
        self.dte_fechoy.setFrame(False)
        self.dte_fechoy.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.dte_fechoy.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.dte_fechoy.setCalendarPopup(False)
        self.dte_fechoy.setDate(QtCore.QDate(2023, 10, 6))
        self.dte_fechoy.setObjectName("dte_fechoy")
        self.cbb_productos = QtWidgets.QComboBox(self.vfm_registroActs_body)
        self.cbb_productos.setGeometry(QtCore.QRect(170, 140, 570, 28))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.cbb_productos.setFont(font)
        self.cbb_productos.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.cbb_productos.setStyleSheet(" color: rgb(255, 255, 255);\n"
"    background-color: rgb(6, 91, 103);")
        self.cbb_productos.setObjectName("cbb_productos")
        self.lbl_productos = QtWidgets.QLabel(self.vfm_registroActs_body)
        self.lbl_productos.setGeometry(QtCore.QRect(170, 114, 78, 24))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_productos.setFont(font)
        self.lbl_productos.setStyleSheet("  font-size: 12px;\n"
"color: rgb(6, 91, 103);")
        self.lbl_productos.setObjectName("lbl_productos")
        self.tbl_actividad = QtWidgets.QTableView(self.vfm_registroActs_body)
        self.tbl_actividad.setEnabled(True)
        self.tbl_actividad.setGeometry(QtCore.QRect(170, 370, 570, 252))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode,Lucida Grande,Sans-Serif")
        font.setPointSize(12)
        self.tbl_actividad.setFont(font)
        self.tbl_actividad.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tbl_actividad.setStyleSheet("font-family: \"Lucida Sans Unicode\", \"Lucida Grande\", Sans-Serif;\n"
"    font-size: 12px;       width: 480px; text-align: left;    border-\n"
"\n"
"th {     font-size: 13px;     font-weight: normal;     padding: 8px;     background: #b9c9fe;\n"
"    border-top: 4px solid #aabcfe;    border-bottom: 1px solid #fff; color: #039; }\n"
"\n"
"td {    padding: 8px;     background: #e8edff;     border-bottom: 1px solid #fff;\n"
"    color: #669;    border-top: 1px solid transparent; }\n"
"\n"
"tr:hover td { background: #d0dafd; color: #339; }")
        self.tbl_actividad.setObjectName("tbl_actividad")
        vfm_registroActs.setCentralWidget(self.vfm_registroActs_body)
        self.vfm_registroActs_statusb = QtWidgets.QStatusBar(vfm_registroActs)
        self.vfm_registroActs_statusb.setObjectName("vfm_registroActs_statusb")
        vfm_registroActs.setStatusBar(self.vfm_registroActs_statusb)

        self.retranslateUi(vfm_registroActs)
        QtCore.QMetaObject.connectSlotsByName(vfm_registroActs)
        vfm_registroActs.setTabOrder(self.txt_op, self.cbb_productos)
        vfm_registroActs.setTabOrder(self.cbb_productos, self.cbb_departamento)
        vfm_registroActs.setTabOrder(self.cbb_departamento, self.cbb_actividad)
        vfm_registroActs.setTabOrder(self.cbb_actividad, self.btn_actividad)
        vfm_registroActs.setTabOrder(self.btn_actividad, self.txt_tiempo)
        vfm_registroActs.setTabOrder(self.txt_tiempo, self.rbt_horas)
        vfm_registroActs.setTabOrder(self.rbt_horas, self.rbt_minutos)
        vfm_registroActs.setTabOrder(self.rbt_minutos, self.btn_agregaAct)
        vfm_registroActs.setTabOrder(self.btn_agregaAct, self.tbl_actividad)
        vfm_registroActs.setTabOrder(self.tbl_actividad, self.btn_guardar)
        vfm_registroActs.setTabOrder(self.btn_guardar, self.btn_quitar)

    def retranslateUi(self, vfm_registroActs):
        _translate = QtCore.QCoreApplication.translate
        vfm_registroActs.setWindowTitle(_translate("vfm_registroActs", ". . : : Actividades : : . ."))
        self.txt_tiempo.setPlaceholderText(_translate("vfm_registroActs", "TIEMPO"))
        self.txt_op.setPlaceholderText(_translate("vfm_registroActs", "OP"))
        self.lbl_nombre.setText(_translate("vfm_registroActs", "NOMBRE  COMPLETO"))
        self.txt_cliente.setPlaceholderText(_translate("vfm_registroActs", "CLIENTE"))
        self.lbl_departamento.setText(_translate("vfm_registroActs", "DEPARTAMENTO"))
        self.lbl_actividad.setText(_translate("vfm_registroActs", "ACTIVIDAD"))
        self.btn_actividad.setText(_translate("vfm_registroActs", "+ ACTIVIDAD"))
        self.rbt_horas.setText(_translate("vfm_registroActs", "HORAS"))
        self.rbt_minutos.setText(_translate("vfm_registroActs", "MINUTOS"))
        self.btn_guardar.setText(_translate("vfm_registroActs", "GUARDAR ACTIVIDADES"))
        self.btn_agregaAct.setText(_translate("vfm_registroActs", "AGREGAR ACTIVIDAD"))
        self.btn_quitar.setText(_translate("vfm_registroActs", "QUITAR"))
        self.lbl_productos.setText(_translate("vfm_registroActs", "PRODUCTOS"))
import Views.recursos_AA

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    vfm_registroActs = QtWidgets.QMainWindow()
    ui = Ui_vfm_registroActs()
    ui.setupUi(vfm_registroActs)
    vfm_registroActs.show()
    sys.exit(app.exec_())
