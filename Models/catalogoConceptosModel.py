import Models.connection as cn
import pymysql

class CatalagoConceptos:
    def __init__(self, concepto, idDepartamento) :
        self.concepto = concepto
        self.idDepartamento = idDepartamento

class ModelCatalagoConceptos:
    def __init__(self):
        pass

    def catalagoConceptosByDepartamento(self, idDepartamento):
        self.c = cn.DataBase()
        try:  
          x="SELECT ID_CCONCEPTO, CONCEPTO FROM OPS.Catalogo_Conceptos where ID_RHCATDEPARTAMENTOS="+str(idDepartamento)+";"
          self.c.cursor.execute(x)
          self.c.connection.commit()
          r=self.c.cursor.fetchall()
          return r
        except  pymysql.Error as e:
            print("Error:", e)
        finally:
            if hasattr(self, 'c'):
                self.c.cursor.close()

    def CatalogoConceptosInsert(self, id_departamento,txt_concepto):
        self.c = cn.DataBase()
        x="INSERT INTO `OPS`.`Catalogo_Conceptos` (`CONCEPTO`, `ID_RHCATDEPARTAMENTOS`)  VALUES (%s, %s);"
        v=(""+str(txt_concepto)+"" , ""+str(id_departamento)+"")
        try:       
            self.c.cursor.execute(x, v)
            self.c.connection.commit()
        except  pymysql.Error as e:
            print("Error:", e)
        finally:
            if hasattr(self, 'c'):
                self.c.cursor.close()

    def catalagoConceptosId(self, idDepartamento, concepto):
        self.c = cn.DataBase()
        try:  
          x="SELECT ID_CCONCEPTO FROM OPS.Catalogo_Conceptos where ID_RHCATDEPARTAMENTOS="+str(idDepartamento)+" and CONCEPTO= '"+str(concepto)+"';"
          self.c.cursor.execute(x)
          self.c.connection.commit()
          r=self.c.cursor.fetchone()
          return r
        except  pymysql.Error as e:
            print("Error:", e)
        finally:
            if hasattr(self, 'c'):
                self.c.cursor.close()