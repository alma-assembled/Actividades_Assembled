import Models.connection as cn
import pymysql

class BaseProyectosDocumentos:
    def __init__(self, ID_BPROYECTO, PROYECTO, ALIAS, STATUS, ACTIVO) :
        self.ID_BPROYECTO=ID_BPROYECTO
        self.proyecto = PROYECTO
        self.alias = ALIAS
        self.status = STATUS
        self.activo = ACTIVO


class ModelProyectos:

    def __init__(self):
        pass

    def proyectosAll(self):
        self.c = cn.DataBase()
        try:
          x="SELECT P.PROYECTO FROM OPS.Base_Proyectos P  WHERE P.ACTIVO=1 AND P.STATUS='A' order by PROYECTO ;"
          self.c.cursor.execute(x)
          self.c.connection.commit()
          r=self.c.cursor.fetchall()
          return r
        except  pymysql.Error as e:
            print("Error:", e)
        finally:
            if hasattr(self, 'c'):
                self.c.cursor.close()

    def proyectoByNameProyecto(self, idCliente, proyecto):
        self.c = cn.DataBase()
        try:
          x='''SELECT  P.ID_BPROYECTO
            FROM OPS.Base_Proyectos P ,  OPS.Catalogo_Domicilios D,  OPS.Catalogo_Contactos CC 
            WHERE D.ID_CCLIENTE = '''+str(idCliente)+'''
            AND  CC.ID_CDOMICILIO = D.ID_CDOMICILIO 
            AND P.ID_CCONTACTO = CC.ID_CCONTACTO 
            AND P.ACTIVO=1 
            AND P.STATUS='A'
            AND P.PROYECTO = "'''+str(proyecto)+'''"
            '''
          self.c.cursor.execute(x)
          self.c.connection.commit()
          r=self.c.cursor.fetchone()
          return r
        except  pymysql.Error as e:
            print("Error:", e)
        finally:
            if hasattr(self, 'c'):
                self.c.cursor.close()

    def proyectosAllByIdCliente(self, idCliente):
        self.c = cn.DataBase()
        try:
          x='''SELECT  P.PROYECTO, P.ID_BPROYECTO
                FROM OPS.Base_Proyectos P ,  OPS.Catalogo_Domicilios D,  OPS.Catalogo_Contactos CC 
                WHERE D.ID_CCLIENTE = '''+str(idCliente)+'''
                AND  CC.ID_CDOMICILIO = D.ID_CDOMICILIO 
                AND P.ID_CCONTACTO = CC.ID_CCONTACTO 
                AND P.ACTIVO=1 
                AND P.STATUS='A' ;'''
          self.c.cursor.execute(x)
          self.c.connection.commit()
          r=self.c.cursor.fetchall()
          return r
        except  pymysql.Error as e:
            print("Error:", e)
        finally:
            if hasattr(self, 'c'):
                self.c.cursor.close()
    
    def insertProyecto(self, proyecto, alias, id_contacto, id_cdomicilio):
        self.c = cn.DataBase()
        x="INSERT INTO `OPS`.`Base_Proyectos`(`PROYECTO`, `ALIAS`,  `ID_CCONTACTO`, `ID_CDOMICILIO`) VALUES(%s, %s, %s, %s);"
        v=(""+str(proyecto)+"",""+str(alias)+"",""+str(id_contacto)+"",""+str(id_cdomicilio)+"")
        try:
            self.c.cursor.execute(x,v)
            self.c.connection.commit()
            # Obtener el ID del elemento recién insertado
            id_base_proyecto = self.c.cursor.lastrowid
            return id_base_proyecto
        except pymysql.Error as e:
            print("Error: ", e)
        finally:
            if hasattr(self, 'c'):
                self.c.cursor.close()

    def clientesAll(self):
        self.c = cn.DataBase()
        try:
          x="SELECT `RAZON_SOCIAL`,ID_CCLIENTE FROM `Catalogo_Clientes` WHERE `ACTIVO`=TRUE order by RAZON_SOCIAL;"
          self.c.cursor.execute(x)
          self.c.connection.commit()
          r=self.c.cursor.fetchall()
          return r
        except  pymysql.Error as e:
            print("Error:", e)
        finally:
            if hasattr(self, 'c'):
                self.c.cursor.close()

    def clienteByRazonSocial(self, razonSocial):
        self.c = cn.DataBase()
        try:
          x="SELECT `ID_CCLIENTE` FROM `Catalogo_Clientes` WHERE `ACTIVO`=TRUE AND `RAZON_SOCIAL`='"+razonSocial+"';"
          self.c.cursor.execute(x)
          self.c.connection.commit()
          r=self.c.cursor.fetchone()
          return r
        except  pymysql.Error as e:
            print("Error:", e)
        finally:
            if hasattr(self, 'c'):
                self.c.cursor.close()
    
    def contactosAllbyIdRazonSocial(self, idCliente):
        self.c = cn.DataBase()
        try:
          x="SELECT `Catalogo_Contactos`.`NOMBRE` , Catalogo_Contactos.ID_CCONTACTO FROM `Catalogo_Contactos`,`Catalogo_Domicilios` WHERE `Catalogo_Contactos`.`ACTIVO`=TRUE AND `Catalogo_Contactos`.`ID_CDOMICILIO`=`Catalogo_Domicilios`.`ID_CDOMICILIO` AND `Catalogo_Domicilios`.`ID_CCLIENTE`="+str(idCliente)+" order by NOMBRE;"
          self.c.cursor.execute(x)
          self.c.connection.commit()
          r=self.c.cursor.fetchall()
          return r
        except  pymysql.Error as e:
            print("Error:", e)
        finally:
            if hasattr(self, 'c'):
                self.c.cursor.close()

    def domiciliosByIdCliente(self, idCliente):
        self.c = cn.DataBase()
        try:
          x="SELECT calle, ID_CDOMICILIO FROM OPS.Catalogo_Domicilios WHERE ID_CCLIENTE="+str(idCliente)+" order by calle;"
          self.c.cursor.execute(x)
          self.c.connection.commit()
          r=self.c.cursor.fetchall()
          return r
        except  pymysql.Error as e:
            print("Error:", e)
        finally:
            if hasattr(self, 'c'):
                self.c.cursor.close()


    def insertDocumentosProyectos(self, Folio, id_BProyecto, id_CTipoDocumento):
        self.c = cn.DataBase()
        x="INSERT INTO `OPS`.`Base_DocumentosProyectos`(`FOLIO`, `ID_BPROYECTO`, `ID_CTIPODOCUMENTO`) VALUES(%s, %s, %s);"
        v=(""+str(Folio)+"", ""+str(id_BProyecto)+"",""+str(id_CTipoDocumento)+"")
        try:
            self.c.cursor.execute(x,v)
            self.c.connection.commit()
            # Obtener el ID del elemento recién insertado
            id_base_documentos = self.c.cursor.lastrowid
            return id_base_documentos
        except pymysql.Error as e:
            print("Error: ", e)
        finally:
            if hasattr(self, 'c'):
                self.c.cursor.close()