from flask import current_app as app
from app.conexion.Conexion import Conexion

class EstadoDao:
    
    def getEstados(self):
        
        querySQL = """
            SELECT id, descripcion FROM estados
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:    
            cur.execute(querySQL)
            tuplas = cur.fetchall()
            return [{ 'id': item[0], 'descripcion': item[1] }  for item in tuplas] if tuplas else []
        except con.Error as e:
            app.logger.info(f"pgcode = {e.pgcode} , mensaje = {e.pgerror}")

        finally:
            cur.close()
            con.close()