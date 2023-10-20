
from Models.userModel import Usuario 
from Views.conceptoView import Ui_DilogConceptos
from Views.nuevo_proyecto import Ui_frm_nuevoProyecto
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
        self.vista.btn_actividad.clicked.connect(self.mostrar_vista_concepto)
        self.vista.btn_nuevoProyecto.clicked.connect(self.mostrar_vista_nuevo_proyecto)
        #self.vista.btn_cerrar.clicked.connect(self.cerrar)
        self.vista.cbb_departamento.currentIndexChanged.connect(self.evntChangedCbConcepto)
        self.vista.txt_op.editingFinished.connect(self.evtEditingFinishedOpLLenarInfo)
        self.vista.btn_agregaAct.clicked.connect(self.evtAgregarActididad)
        self.vista.btn_guardar.clicked.connect(self.evtGuaradarFormulario)
        self.vista.btn_quitar.clicked.connect(self.evtQuitarElemento)
        self.vista.txt_tiempo.editingFinished.connect(self.evtEditingFinishedTiempo)
        self.vista.rbt_horas.toggled.connect(self.evtRadio_button_toggled)
        self.vista.rbt_minutos.toggled.connect(self.evtRadio_button_toggled)
        self.controllerComon.llenarCbDepartameto(self.vista.cbb_departamento)
        self.controllerComon.llenarCbDocumentos(self.vista.cbb_documentos)
        self.vista.rbt_variasOPs.clicked.connect(self.variasOps)
        self.vista.rbt_unaOP.clicked.connect(self.unaOp)
        self.vista.rbt_proyectos.clicked.connect(self.porProyeto)
        self.vista.btn_agregarOP.clicked.connect(self.evtAgregarOpList)
        self.vista.btn_quitarOP.clicked.connect(self.evtQuitarOPList)

        #validar campos numericos
        int_validator = QIntValidator()
        self.vista.txt_tiempo.setValidator(int_validator)
        self.vista.txt_op.setValidator(int_validator)


        self.llenarInfoInicial()
        
        #Descripcion: crear un modelo y asignar la cabecera de las tablas
        self.tabla_activiades_modelo = QStandardItemModel()
        self.tabla_activiades_modelo.setHorizontalHeaderLabels(["OP", "MODO","TIEMPO","DEPARTAMENTO","CONCEPTO"])
        self.vista.tbl_actividad.setModel(self.tabla_activiades_modelo)
        self.vista.tbl_actividad.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows) 

        #Crear un modelo para el QlistView
        self.model_ops = QStandardItemModel()
        

        self.mensaje = QtWidgets.QMessageBox()
        self.mensaje.setIcon(QtWidgets.QMessageBox.Information)
        self.mensaje.setWindowTitle(". . : : Informacion : : . .")
    
    def mostrar_vista_concepto(self):
        '''
            Descripcion:
                Manda ha hablar  la ventana para agregar nuevos conceptos
        '''
        self.view_conceptos = QtWidgets.QMainWindow()
        self.ui = Ui_DilogConceptos() 
        self.ui.setupUi(self.view_conceptos)
        self.controlador = ControllerConcepto(self.ui, self.view_conceptos) 
        self.view_conceptos.show()
        '''Asignar el evento cerrar, a la ventana conceptos'''
        self.view_conceptos.closeEvent = self.evento_de_cierre_conceptos

    def mostrar_vista_nuevo_proyecto(self):
        '''
            Descripcion:
                Manda ha hablar  la ventana para agregar nuevos proyectos
        '''
        self.view_proyecto = QtWidgets.QMainWindow()
        self.ui = Ui_frm_nuevoProyecto() 
        self.ui.setupUi(self.view_proyecto)
        #self.controlador = ControllerConcepto(self.ui, self.view_proyecto) 
        self.view_proyecto.show()
        '''Asignar el evento cerrar, a la ventana conceptos'''
        #self.view_proyecto.closeEvent = self.evento_de_cierre_conceptos



    def cerrar(self):

        self.ventana.close()

    def evntChangedCbConcepto(self):
        '''
            Descripcion:    
                Para actualizar el combo box (Conceptos) despues de haber seleccionado un (departamento)
        '''
        id_departamento = self.model_departamento.baseDepartamentos_by_name(self.vista.cbb_departamento.currentText())
        self.controllerComon.llenarCbConceptos(self.vista.cbb_actividad, id_departamento[0])

    def evento_de_cierre_conceptos(self, event):
        '''
            Descripcion:
                Despues de cerrar la ventana de agregar  conceptos 
        '''
        self.evntChangedCbConcepto()
        
    def llenarInfoInicial(self): 
        '''
            Descripcion:
                Llenar la informacion inicial apartir de el usuario logeado
        '''
        self.modelUser.infoUsuario()
        self.vista.lbl_nombre.setText(BdUsurio.nombre)
        self.vista.cbb_departamento.setCurrentText(BdUsurio.departamento)
        self.controllerComon.llenarCbConceptos(self.vista.cbb_actividad, BdUsurio.id_departamento)

        '''Definir hora que se abre la app'''
        self.hora_inicial = datetime.datetime.now().time()
        print("hora inicial:", self.hora_inicial )
        self.fecha_actual = QDate.currentDate()
        self.vista.dte_fechoy.setDate(self.fecha_actual )
        self.vista.rbt_minutos.setChecked(True)
        #Inicial con solo una op
        self.vista.rbt_unaOP.setChecked(True)
        self.unaOp()
        
        
    def evtEditingFinishedOpLLenarInfo(self):
        '''
            Descripcion:
                Para cargar informacion apartir de ingresar una op
        '''
        op = self.vista.txt_op.text() 
        cliente= self.model_op.ConsultaCliente(op)
        if cliente != None:
            self.vista.txt_cliente.setText(cliente[0])
        else:
            self.evtLimpiaraCampos()

    def evtAgregarActididad(self):
        '''
            Descripcion:
                Agregar actividad al modelo, se ve reflejado en la tabla
        '''
        if self.vista.txt_tiempo.text() != "" :
            HoraMinutos = ""
            if self.vista.rbt_minutos.isChecked():
                HoraMinutos = "M"
            else :
                HoraMinutos = "H"

            #POR OP
            if self.vista.rbt_unaOP.isChecked() :
                op = QStandardItem(self.vista.txt_op.text() )
                modo = QStandardItem(HoraMinutos)
                tiempo = QStandardItem(self.vista.txt_tiempo.text())
                departamento = QStandardItem(self.vista.cbb_departamento.currentText())
                concepto = QStandardItem(self.vista.cbb_actividad.currentText())
                self.tabla_activiades_modelo.appendRow([op, modo, tiempo, departamento, concepto])
                self.vista.tbl_actividad.setModel(self.tabla_activiades_modelo)
            #VARIAS OP
            elif self.vista.rbt_variasOPs.isChecked() : 
                minutos = int(self.vista.txt_tiempo.text())
                if HoraMinutos == "H":
                    minutos =  int(self.vista.txt_tiempo.text()) * 60
                filas = self.model_ops.rowCount()
                tiempo_individual = int(minutos/int(filas)) 
                for fila in range(filas):
                    item = self.model_ops.item(fila, 0)
                    if item is not None :
                        op = QStandardItem(item.text())
                        modo = QStandardItem("M")
                        tiempo = QStandardItem(str(tiempo_individual))
                        departamento = QStandardItem(self.vista.cbb_departamento.currentText())
                        concepto = QStandardItem(self.vista.cbb_actividad.currentText())
                        self.tabla_activiades_modelo.appendRow([op, modo, tiempo, departamento, concepto])
                        self.vista.tbl_actividad.setModel(self.tabla_activiades_modelo)
            #POR PROYECTO
            elif  self.vista.rbt_proyectos.setChecked().isChecked() : 
                pass
            
            self.evtLimpiaraCampos()
            self.vista.txt_tiempo.setText("")

        else :
            self.mensaje.setText( "Debes ingresar el tiempo que tardaste haciendo esa actividad")
            self.mensaje.exec_()

    def evtLimpiaraCampos(self):
        ''''
        Descripcion:
            limpiar campos
        '''
        self.vista.txt_cliente.setText("")
        self.vista.txt_op.setText("")

    def evtQuitarElemento(self):
        '''
        Descripcion: 
            Eliminar un elemento seleccionado de la tabla
        '''
        modelo = self.vista.tbl_actividad.model()
        indices_seleccionados = self.vista.tbl_actividad.selectionModel().selectedRows()
        for indice in sorted(indices_seleccionados, reverse=True):
            modelo.removeRow(indice.row())
        self.vista.tbl_actividad.update()

    def evtEditingFinishedTiempo(self):
        '''
            Descripcion:
                Validar que no meta mas de 59 min: si es  50 >   = se limpiar campo 
        '''
        time = self.vista.txt_tiempo.text() 
        if self.vista.rbt_minutos.isChecked() == True and int(time) > 59 :
            self.vista.txt_tiempo.setText("")

    def evtRadio_button_toggled(self, state):
        ''' 
            Descripcion:
                Evento disparado al cambiar el  estado del radio button
                Limpiar el campo txt_tiempo despues de cambiar el estado
            Args:
                state:estado del radio button
        '''
        if state:
            self.vista.txt_tiempo.setText("")

    def evtGuaradarFormulario(self):
        '''
            Descripcion:
                para guardar las actididaes en la base datos
                -Base_Tareas
                -lista de (Base_Conceptos)
        '''
        modelo = self.vista.tbl_actividad.model()
        num_filas = modelo.rowCount()
        num_columnas = modelo.columnCount()

        fecha= self.vista.dte_fechoy.date()
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
        self.tabla_activiades_modelo.clear()
        self.tabla_activiades_modelo.setHorizontalHeaderLabels(["op", "Modo","Tiempo","Departamento","Concepto"])
        self.model_ops.clear()
        self.vista.tbl_actividad.setModel(self.tabla_activiades_modelo)
        self.mensaje = QtWidgets.QMessageBox()
        self.mensaje.setIcon(QtWidgets.QMessageBox.Information)
        self.mensaje.setText( "Actididades Guardadas")
        self.mensaje.setWindowTitle("Informacion")
        self.mensaje.exec_()

    def evtAgregarOpList(self):
        '''
            Descripcion: 
            Agregar un elemento a la lista de Ops 
        '''
        if self.vista.txt_op.text() != "" :
            filas = self.model_ops.rowCount()
            for fila in range(filas):
                    item = self.model_ops.item(fila, 0)
                    if item is not None and item.text() == self.vista.txt_op.text():
                        self.evtLimpiaraCampos()
                        self.mensaje.setText( "OP ya agregada" + item.text())
                        self.mensaje.exec_()
                        return
            concepto = QStandardItem(self.vista.txt_op.text())
            self.model_ops.appendRow(concepto)
            self.vista.lsv_ops.setModel(self.model_ops)
            self.evtLimpiaraCampos()


    def evtQuitarOPList(self):
        '''
            Descripcion: 
                Eliminar un elemento seleccionado de la lista
        '''
        modelo = self.vista.lsv_ops.model()
        indices_seleccionados = self.vista.lsv_ops.selectionModel().selectedRows()
        for indice in sorted(indices_seleccionados, reverse=True):
            modelo.removeRow(indice.row())
        self.vista.lsv_ops.update()


    def unaOp(self):
        '''
            Descripcion:
                Ocultar los elementos necesarios cuando sea para solo una op
        '''
        self.vista.lsv_ops.setVisible(False)
        self.vista.btn_nuevoProyecto.setVisible(False)
        self.vista.btn_agregarOP.setVisible(False)
        self.vista.btn_quitarOP.setVisible(False)
        self.vista.lbl_listaProyectos.setVisible(False)
        self.vista.cbb_listaProyectos.setVisible(False)
        self.vista.lbl_documentos.setVisible(False)
        self.vista.cbb_documentos.setVisible(False)

    def variasOps(self):
        '''
            Descripcion:
                Ocultar los elementos necesarios cuando sea para varias op
        '''
        self.vista.lsv_ops.setVisible(True)
        self.vista.btn_nuevoProyecto.setVisible(False)
        self.vista.btn_agregarOP.setVisible(True)
        self.vista.btn_quitarOP.setVisible(True)
        self.vista.lbl_listaProyectos.setVisible(False)
        self.vista.cbb_listaProyectos.setVisible(False)
        self.vista.lbl_documentos.setVisible(False)
        self.vista.cbb_documentos.setVisible(False)

    def porProyeto(self):
        '''
            Descripcion:
                Ocultar los elementos necesarios cuando no tenga op, sea por proyecto
        '''
        self.vista.lsv_ops.setVisible(False)
        self.vista.btn_nuevoProyecto.setVisible(True)
        self.vista.btn_agregarOP.setVisible(False)
        self.vista.btn_quitarOP.setVisible(False)
        self.vista.lbl_listaProyectos.setVisible(True)
        self.vista.cbb_listaProyectos.setVisible(True)
        self.vista.lbl_documentos.setVisible(True)
        self.vista.cbb_documentos.setVisible(True)