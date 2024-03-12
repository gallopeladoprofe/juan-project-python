from app.conexion.Conexion import Conexion

class PaisDao:
    
    def getPaises(self):
        
        querySQL = """
            SELECT id, descripcion
            FROM paises
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:    
            cur.execute(querySQL)
            return cur.fetchall()
        except con.Error as e:
            print(f"pgcode = {e.pgcode} , mensaje = {e.pgerror}")            

        finally:
            cur.close()
            con.close()