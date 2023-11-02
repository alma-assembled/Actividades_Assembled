import Models.connection as cn
import pymysql


class BaseTarea:
    def __init__(self, idUsuario, horaInicio, horaFin) :
        self.idUsuario = idUsuario
        self.horaInicio = horaInicio
        self.horaFin = horaFin

class ModelBaseTarea:
    def __init__(self):
       pass

    def BaseTareasAll(self):
        self.c = cn.DataBase()
        try:  
          x="SELECT * FROM OPS.Base_Tareas;"
          self.c.cursor.execute(x)
          self.c.connection.commit()
          r=self.c.cursor.fetchall()
          return r
        except  pymysql.Error as e:
            print("Error:", e)
        finally:
            if hasattr(self, 'c'):
                self.c.cursor.close()

    def BaseTareasById(self, ID_BTAREA):
        self.c = cn.DataBase()
        try:  
          x="SELECT * FROM OPS.Base_Tareas where ID_BTAREA= "+ID_BTAREA+";"
          self.c.cursor.execute(x)
          self.c.connection.commit()
          r=self.c.cursor.fetchone()
          return r
        except  pymysql.Error as e:
            print("Error:", e)
        finally:
            if hasattr(self, 'c'):
                self.c.cursor.close()

    def BaseTareasInsert(self, BaseTarea):
        self.c = cn.DataBase()
        x="INSERT INTO `OPS`.`Base_Tareas` (`HORA_INICIO`, `HORA_FIN`, `ID_CEMPLEADO`)  VALUES (%s, %s, %s);"
        v=(""+str(BaseTarea.horaInicio)+"" , ""+ str(BaseTarea.horaFin) + "" , ""+ str(BaseTarea.idUsuario) +"")
        try:  
            self.c.cursor.execute(x, v) 
            self.c.connection.commit()

            # Obtener el ID del elemento recién insertado
            id_base_tarea = self.c.cursor.lastrowid
            return id_base_tarea
        except  pymysql.Error as e:
            print("Error:", e)
        finally:
            if hasattr(self, 'c'):
                self.c.cursor.close()

    def selectIdentity(self):
        self.c = cn.DataBase()
        try:  
          x="SELECT @@IDENTITY AS 'Identity';"
          self.c.cursor.execute(x)
          self.c.connection.commit()
          r=self.c.cursor.fetchone()
          return r
        except  pymysql.Error as e:
            print("Error:", e)
        finally:
            if hasattr(self, 'c'):
                self.c.cursor.close()