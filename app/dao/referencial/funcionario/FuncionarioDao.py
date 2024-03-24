from flask import current_app as app
from app.conexion.Conexion import Conexion

class FuncionarioDao:

    def getFuncionarios(self):

        querySQL = """
            SELECT
                f.id, p.nombres, p.apellidos, p.ci
            FROM
                funcionarios f
            LEFT JOIN personas p ON p.id = f.id_persona
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(querySQL)
            lista = cur.fetchall()
            return [ {'id': item[0],'nombres': item[1], 'apellidos' : item[2], 'ci': item[3]
                    } for item in lista ] if lista else []
        except con.Error as e:
            app.logger.info(f"pgcode = {e.pgcode} , mensaje = {e.pgerror}")

        finally:
            cur.close()
            con.close()

    def getFuncionarioById(self, id):

        querySQL = """
            SELECT
                f.id, p.nombres, p.apellidos, p.ci
                , c.descripcion AS cargo, d.descripcion AS departamento
            FROM
                funcionarios f
            LEFT JOIN personas p ON p.id = f.id_persona
            LEFT JOIN cargos c ON c.id = f.id_cargo
            LEFT JOIN departamento d ON d.id = f.id_departamento
            WHERE f.id = %s

        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(querySQL, (id,))
            item = cur.fetchone()
            return { 'id': item[0],'nombres': item[1], 'apellidos' : item[2]
                    , 'ci': item[3], 'cargo': item[4], 'departamento': item[5] } if item else {}
        except con.Error as e:
            app.logger.info(f"pgcode = {e.pgcode} , mensaje = {e.pgerror}")
        finally:
            cur.close()
            con.close()