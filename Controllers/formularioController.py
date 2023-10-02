
from Models.userModel import Usuario 
from Views.conceptoView import Ui_DilogConceptos
from PyQt5 import  QtWidgets
import  sys
from Controllers.conceptoController import ControllerConcepto
from Controllers.comunController import ControllerComun
from Models.userModel import ModelUser
from Models.global_variables import BdUsurio
from Models.departamentosModel import ModelDepartamento
from Models.catalogoConceptosModel import ModelCatalagoConceptos
from Models.baseTareasModel import ModelBaseTarea, BaseTarea
from Models.baseConceptosModel import ModelBaseConceptos, BaseConceptos
from Models.opModel import opModel
import datetime
from PyQt5.QtCore import QDate
from PyQt5.QtGui import QStandardItemModel,  QStandardItem , QIntValidator

class ControllerFormulario:
    def __init__(self, vista, ventana):
        self.vista = vista
        self.ventana =  ventana

        #CONTROLADORES
        self.controllerComon = ControllerComun() 
        #MODELOS
        self.modelUser = ModelUser()
        self.model_departamento = ModelDepartamento()
        self.model_op = opModel()
        self.model_conceptos = ModelCatalagoConceptos()
        self.model_base_tareas = ModelBaseTarea()
        self.model_base_conceptos = ModelBaseConceptos()
        #INICIAL
        self.vista.btn_concepto.clicked.connect(self.mostrar_vista_concepto)
        self.vista.btn_cerrar.clicked.connect(self.cerrar)
        self.vista.cb_departamento.currentIndexChanged.connect(self.evntChangedCbConcepto)
        self.vista.txt_op.editingFinished.connect(self.evtEditingFinishedOpLLenarInfo)
        self.vista.btn_agregarActividad.clicked.connect(self.evtAgregarActididad)
        self.vista.btn_guardar.clicked.connect(self.evtGuaradarFormulario)
        self.vista.btn_quitar.clicked.connect(self.evtQuitarElemento)
        self.vista.txt_horasMinutos.editingFinished.connect(self.evtEditingFinishedTiempo)
        self.vista.rb_horas.toggled.connect(self.evtRadio_button_toggled)
        self.vista.rb_minutos.toggled.connect(self.evtRadio_button_toggled)
        self.controllerComon.llenarCbDepartameto(self.vista.cb_departamento)

        #validar campos numericos
        int_validator = QIntValidator()
        self.vista.txt_horasMinutos.setValidator(int_validator)
        self.vista.txt_op.setValidator(int_validator)


        self.llenarInfoInicial()
        '''Crear un modelo de tabla de elementos estándar '''
        self.tabla_activiades_modelo = QStandardItemModel()
        self.tabla_activiades_modelo.setHorizontalHeaderLabels(["op", "Modo","Tiempo","Departamento","Concepto"])
        self.vista.tabla_actividad.setModel(self.tabla_activiades_modelo)
        self.vista.tabla_actividad.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows) 


    def mostrar_vista_concepto(self):
        '''Metodo:  muesta la ventana para agregar concepto        '''
        self.view_conceptos = QtWidgets.QMainWindow()
        self.ui = Ui_DilogConceptos() 
        self.ui.setupUi(self.view_conceptos)
        self.controlador = ControllerConcepto(self.ui, self.view_conceptos) 
        self.view_conceptos.show()
        '''evento al cerrrar la ventana conceptos'''
        self.view_conceptos.closeEvent = self.evento_de_cierre_conceptos

    def cerrar(self):

        self.ventana.close()

    def evntChangedCbConcepto(self):
        '''Metodo:  para actualizar el el combo box (Conceptos) despues de aver seleccionado un (departamento)        '''
        id_departamento = self.model_departamento.baseDepartamentos_by_name(self.vista.cb_departamento.currentText())
        self.controllerComon.llenarCbConceptos(self.vista.cb_concepto, id_departamento[0])

    def evento_de_cierre_conceptos(self, event):
         '''despues de cerrar la ventana de agregar  conceptos '''
         self.evntChangedCbConcepto()
        
    def llenarInfoInicial(self): 
        '''Metodo:  para llenar la el nombre del usurio y su departamento con sus conceptos   '''
        self.vista.rb_minutos.setChecked(True)
        self.modelUser.infoUsuario()
        self.vista.txt_nombre.setText(BdUsurio.nombre)
        self.vista.cb_departamento.setCurrentText(BdUsurio.departamento)
        self.controllerComon.llenarCbConceptos(self.vista.cb_concepto, BdUsurio.id_departamento)

        '''Definir hora que se abre la app'''
        self.hora_inicial = datetime.datetime.now().time()
        print("hora inicial:", self.hora_inicial )
        self.fecha_actual = QDate.currentDate()
        self.vista.dateEdit.setDate(self.fecha_actual )

        
        
    def evtEditingFinishedOpLLenarInfo(self):
        '''Metodo:  para cargar informacion apartir de ingresar una op   '''
        op = self.vista.txt_op.text() 
        cliente= self.model_op.ConsultaCliente(op)
        if cliente != None:
            self.vista.txt_cliente.setText(cliente[0])
            self.llenar_cb_productos(op)
        else:
            self.evtLimpiaraCampos()

    def llenar_cb_productos(self, op):
        '''Metodo:  para cargar los pructos al combo box, apartir de una op '''
        self.vista.cb_productos.clear() 
        conceptos_list =  self.model_op.ConsultaProducctos(op)

        for fila in conceptos_list:
            producto = fila[0]
            self.vista.cb_productos.addItem(producto)

    def evtAgregarActididad(self):
        '''Agregar actividad al modelo de QStandardItemModel() '''
        if self.vista.txt_horasMinutos.text() != "" :
            HoraMinutos = ""
            if self.vista.rb_minutos.isChecked():
                HoraMinutos = "M"
            else :
                HoraMinutos = "H"

            op = QStandardItem(self.vista.txt_op.text() )
            modo = QStandardItem(HoraMinutos)
            tiempo = QStandardItem(self.vista.txt_horasMinutos.text())
            departamento = QStandardItem(self.vista.cb_departamento.currentText())
            concepto = QStandardItem(self.vista.cb_concepto.currentText())
            self.tabla_activiades_modelo.appendRow([op, modo, tiempo, departamento, concepto])
            self.vista.tabla_actividad.setModel(self.tabla_activiades_modelo)
            self.evtLimpiaraCampos()
            self.vista.txt_horasMinutos.setText("")
        else :
            self.mensaje = QtWidgets.QMessageBox()
            self.mensaje.setIcon(QtWidgets.QMessageBox.Information)
            self.mensaje.setText( "Debes ingresar el tiempo que tardaste haciendo esa actividad")
            self.mensaje.setWindowTitle("Informacion")
            self.mensaje.exec_()

    def evtLimpiaraCampos(self):
        ''''limpiar campos'''
        self.vista.txt_cliente.setText("")
        self.vista.txt_op.setText("")
        self.vista.cb_productos.clear()

    def evtQuitarElemento(self):
        '''eliminar un elemento seleccionado de la tabla'''
        modelo = self.vista.tabla_actividad.model()
        indices_seleccionados = self.vista.tabla_actividad.selectionModel().selectedRows()
        for indice in sorted(indices_seleccionados, reverse=True):
            modelo.removeRow(indice.row())
        self.vista.tabla_actividad.update()

    def evtEditingFinishedTiempo(self):
        '''metodo: validar si que no meta mas de 59 min:  50 >   = se limpiar campo '''
        time = self.vista.txt_horasMinutos.text() 
        if self.vista.rb_minutos.isChecked() == True and int(time) > 59 :
            self.vista.txt_horasMinutos.setText("")

    def evtRadio_button_toggled(self, state):
        '''Metodo: limpiar el campo txt_horasMinutos despues de cambiar el estado'''
        if state:
            self.vista.txt_horasMinutos.setText("")

    def evtGuaradarFormulario(self):
        '''Metodo: para guardar las actididaes'''
        modelo = self.vista.tabla_actividad.model()
        num_filas = modelo.rowCount()
        num_columnas = modelo.columnCount()

        fecha= self.vista.dateEdit.date()
        fecha_text = fecha.toString('yyyy-MM-dd')
        hora_i = (str(fecha_text) +" "+ str(self.hora_inicial))
        hora_f = (str(fecha_text) +" "+ str(datetime.datetime.now().time()))

        base_tarea = BaseTarea(BdUsurio.idEmpleado,hora_i,  hora_f,)
        id_base_tarea = self.model_base_tareas.BaseTareasInsert(base_tarea)
        for fila in range(num_filas):
            op = modelo.index(fila, 0)
            tipo = modelo.index(fila, 1)
            tiempo = modelo.index(fila, 2)
            departamento= modelo.index(fila, 3)
            concepto = modelo.index(fila, 4)

            dato_tipo = modelo.data(tipo)
            dato_tiempo = modelo.data(tiempo)
            departamento_id = self.model_departamento.baseDepartamentos_by_name(modelo.data(departamento))[0]
            concepto_id =  self.model_conceptos.catalagoConceptosId(departamento_id,modelo.data(concepto))[0]
            _op= self.model_op.ConsultaOpByFolio(modelo.data(op))
            if _op != None :
                base_concepto =BaseConceptos(_op[0], concepto_id,  id_base_tarea, dato_tiempo, dato_tipo)
                self.model_base_conceptos.BaseConceptosInsert_Op(base_concepto )
            else :
                _op = 0
                base_concepto =BaseConceptos(_op, concepto_id,  id_base_tarea, dato_tiempo, dato_tipo)
                self.model_base_conceptos.BaseConceptosInsert(base_concepto )

        self.mensaje = QtWidgets.QMessageBox()
        self.mensaje.setIcon(QtWidgets.QMessageBox.Information)
        self.mensaje.setText( "Actididades Guardadas")
        self.mensaje.setWindowTitle("Informacion")
        self.mensaje.exec_()
        self.cerrar()