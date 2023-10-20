import Models.connection as cn
import pymysql

class CatalogoTiposDocumentos:
    def __init__(self, ID_CTIPODOCUMENTO, DOCUMENTO) :
        self.id_ctipodocumento=ID_CTIPODOCUMENTO
        self.documentos = DOCUMENTO

class ModelCatalogoTiposDocumentos:

    def __init__(self):
        self.c = cn.DataBase()

    def tipoDocumentosAll(self):
        self.c = cn.DataBase()
        try:
          x="SELECT DOCUMENTO FROM OPS.Catalogo_TiposDocumento where ACTIVO=1;"
          self.c.cursor.execute(x)
          self.c.connection.commit()
          r=self.c.cursor.fetchall()
          return r
        except  pymysql.Error as e:
            print("Error:", e)
        finally:
            if hasattr(self, 'c'):
                self.c.cursor.close()