from Models.departamentosModel import BaseDepartamentos, ModelDepartamento
from Models.catalogoTipodDocumentosModel import ModelCatalogoTiposDocumentos
from Models.catalogoConceptosModel import ModelCatalagoConceptos, CatalagoConceptos
from Models.baseProyectosModel import ModelProyectos

class ControllerComun:
    def __init__(self):
     pass   

    def llenarCbDepartameto(self, comboBox):
        '''
        Llenar el combo box: departamentos
        '''
        self.model =ModelDepartamento()
        departamentos_list =  self.model.baseDepartamentosAll()

        for fila in departamentos_list:
            departamento = BaseDepartamentos(fila[0],fila[1])
            comboBox.addItem(departamento.departemanto) 

    def llenarCbConceptos(self, comboBox, idDepartameto):
        '''
        Llenar el combo box: conceptos
        '''
        comboBox.clear() 
        self.model =ModelCatalagoConceptos()
        conceptos_list =  self.model.catalagoConceptosByDepartamento(idDepartameto)

        for fila in conceptos_list:
            c = CatalagoConceptos(fila[1],fila[0])
            comboBox.addItem(c.concepto)

    def llenarCbDocumentos(self, comboBox):
        '''
            Llenar el combo box: Tipo de documento
        '''
        comboBox.clear() 
        self.model = ModelCatalogoTiposDocumentos()
        documentos_list =  self.model.tipoDocumentosAll()

        for fila in documentos_list:
            comboBox.addItem(fila[0],fila[1])
    
    def llenarCbProyectos(self, comboBox):
        '''
            Llenar el combo box: Proyectos
        '''
        comboBox.clear() 
        self.model = ModelProyectos()
        documentos_list =  self.model.proyectosAll()

        for fila in documentos_list:
            comboBox.addItem(fila[0])

    def llenarCbProyectosByIdCliente(self, comboBox, idCliente):
        '''
            Llenar el combo box: Proyectos
            id_cliente
        '''
        comboBox.clear() 
        self.model = ModelProyectos()
        documentos_list =  self.model.proyectosAllByIdCliente(idCliente)

        for fila in documentos_list:
            comboBox.addItem(fila[0],fila[1])

    def llenarCbClientes(self, comboBox):
        '''
            Llenar el combo box: Clientes         
        '''
        comboBox.clear() 
        self.model = ModelProyectos()
        clientes_list =  self.model.clientesAll()

        for fila in clientes_list:
            comboBox.addItem(fila[0], fila[1])
            
    
    def llenarCbContactos(self, comboBox, idCliente):
        '''
            Llenar el combo box: Contactos, apartir de un idCliente
        '''
        comboBox.clear()
        self.model = ModelProyectos()
        contactos_list = self.model.contactosAllbyIdRazonSocial(idCliente)

        for fila in contactos_list:
            comboBox.addItem(fila[0],fila[1])

    def llenarCbDomicilios(self, comboBox, idCliente):
        '''
            Llenar el combo box: Contactos, apartir de un idCliente
        '''
        comboBox.clear()
        self.model = ModelProyectos()
        domicilios_list = self.model.domiciliosByIdCliente(idCliente)

        for fila in domicilios_list:
            comboBox.addItem(fila[0],fila[1])

'''if __name__ == "__main__":
    ventana_principal = ControllerComun()
    ventana_principal.llenarModel()'''