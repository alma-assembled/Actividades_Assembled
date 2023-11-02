import Models.connection as cn
import pymysql

class BaseConceptos:
    def __init__(self, idOp, idCConcepto, idBTareas  , tiempo, modo, id_BDocuementoProyectos ) :
        self.idOp = idOp
        self.idCConcepto = idCConcepto
        self.idBTareas = idBTareas 
        self.tiempo = tiempo
        self.modo  = modo
        self.id_BDocuementoProyectos = id_BDocuementoProyectos

class ModelBaseConceptos:
    def __init__(self):
        pass
    
    def BaseTareasAll(self):
        self.c = cn.DataBase()
        try:  
          x="SELECT * FROM OPS.Base_Conceptos;"
          self.c.cursor.execute(x)
          self.c.connection.commit()
          r=self.c.cursor.fetchall()
          return r
        except  pymysql.Error as e:
            print("Error:", e)
        finally:
            if hasattr(self, 'c'):
                self.c.cursor.close()


    def BaseTareasById(self, ID_BCONCEPTO):
        self.c = cn.DataBase()
        try:  
          x="SELECT * FROM OPS.Base_Conceptos where ID_BCONCEPTO= "+ID_BCONCEPTO+";"
          self.c.cursor.execute(x)
          self.c.connection.commit()
          r=self.c.cursor.fetchone()
          return r
        except  pymysql.Error as e:
            print("Error:", e)
        finally:
            if hasattr(self, 'c'):
                self.c.cursor.close()
  
    def BaseConceptosInsert_Op(self, BaseConceptos):
        self.c = cn.DataBase()
        x="INSERT INTO `OPS`.`Base_Conceptos` (`ID_BOP`, `ID_CCONCEPTO`, `ID_BTAREA`, `TIEMPO`, `MODO`, ID_BDOCUMENTOPROYECTO) VALUES (%s, %s, %s, %s, %s, %s);"
        v=(""+str(BaseConceptos.idOp)+"" , ""+ str(BaseConceptos.idCConcepto) + "" , ""+ str(BaseConceptos.idBTareas)  +"" , "" + str(BaseConceptos.tiempo) + "" , "" + str(BaseConceptos.modo)+ "" , "" + str(BaseConceptos.id_BDocuementoProyectos))
        try:  
            self.c.cursor.execute(x, v) 
            self.c.connection.commit()
        except  pymysql.Error as e:
            print("Error:", e)
        finally:
            if hasattr(self, 'c'):
                self.c.cursor.close()

    def BaseConceptosInsert(self, BaseConceptos):
        self.c = cn.DataBase()
        x="INSERT INTO `OPS`.`Base_Conceptos` (`ID_CCONCEPTO`, `ID_BTAREA`, `TIEMPO`, `MODO`) VALUES ( %s, %s, %s, %s);"
        v=(""+ str(BaseConceptos.idCConcepto) + "" , ""+ str(BaseConceptos.idBTareas)  +"" , "" + str(BaseConceptos.tiempo) + "" , "" + str(BaseConceptos.modo)+"")
        try:  
            self.c.cursor.execute(x, v) 
            self.c.connection.commit()
        except  pymysql.Error as e:
            print("Error:", e)
        finally:
            if hasattr(self, 'c'):
                self.c.cursor.close()