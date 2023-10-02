
from Models.userModel import Usuario 
from Views.formularioView import Ui_Viewformulario
from PyQt5 import  QtWidgets
import  sys
from Controllers.formularioController import ControllerFormulario
from Models.global_variables import BdUsurio


class ControllerUser:
    def __init__(self, modelo, vista , ventana_principal):
        self.modelo = modelo
        self.vista = vista
        self.ventana_principal = ventana_principal
        self.vista.btn_cerrar.clicked.connect(self.cerrar)
        self.vista.btn_logear.clicked.connect(self.logear)
        self.vista.label_info.hide()

    def logear(self):
        usuario = self.vista.txt_user.text()
        password = self.vista.txt_password.text()

        if usuario and password:
            user = Usuario(usuario, password)
            if self.modelo.ConsultaUsuario(user) == True:
                self.mostrar_vista_formulario()
            else : 
                self.vista.label_info.show()

    def mostrar_vista_formulario(self):
        self.ventana_principal.close()
        self.Fo = QtWidgets.QMainWindow()
        self.ui = Ui_Viewformulario()
        self.ui.setupUi(self.Fo)
        self.controlador = ControllerFormulario(self.ui, self.Fo)
        self.Fo.show()

    def cerrar(self):
        self.ventana_principal.close()