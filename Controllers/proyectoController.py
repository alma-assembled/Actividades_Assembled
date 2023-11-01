from Controllers.comunController import ControllerComun
from Models.baseProyectosModel import ModelProyectos
from PyQt5 import  QtWidgets
from Models.global_variables import DatosActividades
class ControllerProyecto:
    def __init__(self, vista, ventana):
        self.vista = vista
        self.ventana = ventana
        #modelos
        self.controllerComon = ControllerComun()
        self.model_proyecto = ModelProyectos()
        #hello
        self.controllerComon.llenarCbDocumentos(self.vista.cbb_documento)
        self.controllerComon.llenarCbClientes(self.vista.cbb_cliente)
        self.vista.cbb_cliente.currentIndexChanged.connect(self.evntChangedCbCliente)
        self.vista.cbb_cliente.setCurrentText("ASSEMBLED AS YOU NEED")
        self.vista.btn_box.accepted.connect(self.guardarProyecto) # type: ignore
        self.vista.btn_box.rejected.connect(self.cerrar) # type: ignore

        #INICIALIZAR MENSAJES
        self.mensaje = QtWidgets.QMessageBox()
        self.mensaje.setIcon(QtWidgets.QMessageBox.Information)
        self.mensaje.setWindowTitle(". . : : Informacion : : . .")
        

    def evntChangedCbCliente(self):
        '''
            Descripcion:
                Para actualizar el combo box (Clientes) despues de haber seleccionado un (cliente)
        '''
        self.id_cliente = self.model_proyecto.clienteByRazonSocial(self.vista.cbb_cliente.currentText())
        self.controllerComon.llenarCbContactos(self.vista.cbb_contacto, self.id_cliente[0])
        self.controllerComon.llenarCbDomicilios(self.vista.cbb_domicilio, self.id_cliente[0])
        
    
    def guardarProyecto(self):
        if self.vista.txt_nombreProyecto.text() == "" or self.vista.txt_alias.text() == "":
            self.mensaje.setText("Debes llenar el nombre y alias del proyecto")
            self.mensaje.exec_()
            return
        
        contacto_id =  self.vista.cbb_contacto.itemData(self.vista.cbb_contacto.currentIndex())
        domicilio_id = self.vista.cbb_documento.itemData(self.vista.cbb_domicilio.currentIndex())
        id_proyecto = self.model_proyecto.insertProyecto(self.vista.txt_nombreProyecto.text().upper(),self.vista.txt_alias.text().upper(), contacto_id, domicilio_id)
        
        #inicalizar los datos
        DatosActividades.bandera = True
        DatosActividades.folio = self.vista.txt_folio.text().upper()
        DatosActividades.cliente = self.vista.cbb_cliente.currentText()
        DatosActividades.documento = self.vista.cbb_documento.currentText()
        DatosActividades.proyecto =  self.vista.txt_nombreProyecto.text().upper()

        self.mensaje.setText("PROYECTO GUARDADO")
        self.mensaje.exec_()
        self.cerrar()
    def cerrar(self):
        self.ventana.close()