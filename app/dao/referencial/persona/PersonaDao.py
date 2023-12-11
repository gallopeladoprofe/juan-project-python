from conexion.Conexion import Conexion

class PersonaDao:
    
    def getPersonas(self):
        
        personaSQL = """
            SELECT id, nombres, apellidos, ci, direccion FROM public.personas
        """
        lista = []
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:    
            cur.execute(personaSQL)
            tuplas_personas = cur.fetchall()
            if len(tuplas_personas) > 0:
                for persona in tuplas_personas:
                    lista.append({
                        'id': persona[0],
                        'nombres': persona[1], 
                        'apellidos': persona[2],
                        'ci': persona[3],
                        'direccion': persona[4]
                    })
        except con.Error as e:
            print(f"pgcode = {e.pgcode} , mensaje = {e.pgerror}")            

        finally:
            cur.close()
            con.close()
        return lista
            
    def getPersonaById(self, id):
        
        personaSQL = """
            SELECT id, nombres, apellidos, ci, direccion FROM public.personas
            WHERE id = %s
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:    
            cur.execute(personaSQL, (id,))
            persona = cur.fetchone()
            if persona:
                return {
                        'id': persona[0],
                        'nombres': persona[1], 
                        'apellidos': persona[2],
                        'ci': persona[3],
                        'direccion': persona[4]
                    }
            return None
        except con.Error as e:
            print(f"pgcode = {e.pgcode} , mensaje = {e.pgerror}")            

        finally:
            cur.close()
            con.close()
            
    def insertPersona(self, nombres, apellidos, ci, direccion):
        
        insertSQL = """
            INSERT INTO public.personas(nombres, apellidos, ci, direccion)
	        VALUES (%s, %s, %s, %s)
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:    
            cur.execute(insertSQL, (nombres, apellidos, ci, direccion,))
            con.commit()
            return True
        except con.Error as e:
            print(f"pgcode = {e.pgcode} , mensaje = {e.pgerror}")            

        finally:
            cur.close()
            con.close()
        return False
    
    def updatePersona(self, id, nombres, apellidos, ci, direccion):
        
        updateSQL = """
            UPDATE public.personas
	        SET nombres=%s, apellidos=%s, ci=%s, direccion=%s
	        WHERE id=%s;
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:    
            cur.execute(updateSQL, (nombres, apellidos, ci, direccion, id,))
            con.commit()
            return True
        except con.Error as e:
            print(f"pgcode = {e.pgcode} , mensaje = {e.pgerror}")            

        finally:
            cur.close()
            con.close()
        return False
    
    def deletePersona(self, id):
        
        deleteSQL = """
            DELETE FROM personas WHERE id = %s
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:    
            cur.execute(deleteSQL, (id,))
            con.commit()
            return True
        except con.Error as e:
            print(f"pgcode = {e.pgcode} , mensaje = {e.pgerror}")            

        finally:
            cur.close()
            con.close()
        return False