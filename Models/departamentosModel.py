import Models.connection as cn

class BaseDepartamentos:
    def __init__(self, ID_RHCATDEPARTAMENTOS, departamento) :
        self.idDepartamento= ID_RHCATDEPARTAMENTOS
        self.departemanto = departamento


class ModelDepartamento:
    def __init__(self):
        self.c = cn.DataBase()
        global idEmpleado 

    def baseDepartamentosAll(self):
        try:  
          x="SELECT ID_RHCDEPARTAMENTO, DEPARTAMENTO FROM OPS.RH_Cat_Departamentos;"
          #x="SELECT ID_RHCPUESTO, PUESTO FROM OPS.RH_Cat_Puestos;"   #puestos
          self.c.cursor.execute(x)
          self.c.connection.commit()
          r=self.c.cursor.fetchall()
          return r
        except KeyError:
         print("error basetareasall:", KeyError)

    def baseDepartamentos_by_name(self, txt_departamento):
        try:  
          x="SELECT ID_RHCDEPARTAMENTO FROM OPS.RH_Cat_Departamentos where DEPARTAMENTO='"+txt_departamento+"';"
          self.c.cursor.execute(x)
          self.c.connection.commit()
          r=self.c.cursor.fetchone()
          return r
        except KeyError:
         print("error basetareasall:", KeyError)