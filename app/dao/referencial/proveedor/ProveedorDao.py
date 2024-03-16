from flask import current_app as app
from app.conexion.Conexion import Conexion

class ProveedorDto:
    def __init__(self, id, ruc, identificador_ruc, razon, apellido, \
        direccion, email, telefono, id_ciudad, usuario_actual):
        self.id = id
        self.ruc = ruc
        self.identificador_ruc = identificador_ruc
        self.razon = razon
        self.apellido = apellido
        self.direccion = direccion
        self.email = email
        self.telefono = telefono
        self.id_ciudad = id_ciudad
        self.usuario_actual = usuario_actual

class ProveedorDao:
    
    def getProveedores(self):
        
        querySQL = """
            SELECT p.id, p.ruc, p.ruc_nro_identificador, p.razon_social, p.apellidos
                , p.direccion, p.email, p.telefono, p.id_ciudad, c.descripcion, c.id_pais
            FROM proveedores p LEFT JOIN ciudades c ON c.id = p.id_ciudad
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:    
            cur.execute(querySQL)
            lista = cur.fetchall()
            return [ {
                    'id': item[0],
                    'ruc': item[1]
                    , 'ruc_nro_identificador' : item[2]
                    , 'razon_social' : item[3]
                    , 'apellidos': item[4]
                    , 'direccion': item[5]
                    , 'email': item[6]
                    , 'telefono': item[7]
                    , 'id_ciudad': item[8]
                    , 'nombre_ciudad': item[9]
                    , 'id_pais': item[10]
                    } for item in lista ] if lista else []
        except con.Error as e:
            app.logger.info(f"pgcode = {e.pgcode} , mensaje = {e.pgerror}")

        finally:
            cur.close()
            con.close()
    
    def insertProveedor(self, dto:ProveedorDto):
        
        insertSQL = """
            INSERT INTO public.proveedores (ruc, ruc_nro_identificador, razon_social, 
            apellidos, direccion, email, telefono, id_ciudad, creacion_usuario, 
            creacion_fecha, creacion_hora) 
            VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, CURRENT_DATE, CURRENT_TIME(0));
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:    
            cur.execute(insertSQL, (dto.ruc, dto.identificador_ruc, dto.razon, dto.apellido, dto.direccion,\
                dto.email, dto.telefono, dto.id_ciudad, dto.usuario_actual,))
            con.commit()
            return True
        except con.Error as e:
            app.logger.info(f"pgcode = {e.pgcode} , mensaje = {e.pgerror}")

        finally:
            cur.close()
            con.close()
        return False

    def deleteProveedor(self, id):

        deleteSQL = """
            DELETE FROM public.proveedores WHERE id = %s;
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(deleteSQL, (id,))
            con.commit()
            return True
        except con.Error as e:
            app.logger.info(f"pgcode = {e.pgcode} , mensaje = {e.pgerror}")

        finally:
            cur.close()
            con.close()
        return False