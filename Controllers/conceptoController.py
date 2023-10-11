
from Models.userModel import Usuario 
from Views.conceptoView import Ui_DilogConceptos
from PyQt5 import QtWidgets
import  sys
from PyQt5.QtWidgets import QApplication
from Controllers.comunController import ControllerComun
from Models.catalogoConceptosModel import ModelCatalagoConceptos
from Models.departamentosModel import ModelDepartamento
from Models.global_variables import BdUsurio

class ControllerConcepto:
    def __init__(self, vista, ventana):
        self.vista = vista
        self.ventana = ventana 
        self.controllerComon = ControllerComun() 
        self.controllerComon.llenarCbDepartameto(self.vista.cbb_departamento_frmC)
        self.vista.cbb_departamento_frmC.setCurrentText(BdUsurio.departamento)
        self.model = ModelCatalagoConceptos() 
        self.vista.btn_box.accepted.connect(self.guardarConcepto) # type: ignore
        self.vista.btn_box.rejected.connect(self.cerrar) # type: ignore

    def guardarConcepto(self):
        '''metodo para guardar nuevos conceptos'''
        self.model_departamento = ModelDepartamento()
        id_departamento = self.model_departamento.baseDepartamentos_by_name(self.vista.cbb_departamento_frmC.currentText())
        self.model.CatalogoConceptosInsert( id_departamento[0], self.vista.lineEdit.text().upper()) 
        self.mensaje = QtWidgets.QMessageBox()
        self.mensaje.setIcon(QtWidgets.QMessageBox.Information)
        self.mensaje.setText( "Concepto guardado")
        self.mensaje.setWindowTitle(". . : : Informacion : : . .")
        self.mensaje.exec_()
        self.ventana.close()

    def cerrar(self):
        self.ventana.close()
            