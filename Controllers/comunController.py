from Models.departamentosModel import BaseDepartamentos, ModelDepartamento
from Models.catalogoConceptosModel import ModelCatalagoConceptos, CatalagoConceptos

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
    
'''if __name__ == "__main__":
    ventana_principal = ControllerComun()
    ventana_principal.llenarModel()'''