

def mostrar_status_code(code):
    if code == 400:
        return (f"""
                code: {code}\n
                messaje: Bad request.\n
                level: ERROR.\n
                description: El servidor no puede procesar tu solicitud, los datos ingresados pueden no ser correctos.\n  
                """,400)
    elif code == 404:
        return (f"""
                code: {code} \n
                messaje: Not Found.\n
                level: ERROR.\n
                description: La pagina que buscas ya no existe, se ha movido o escribiste mal la direccion URL.\n   
                """,404)
    elif code == 200:
        return (f"""
                code: {code}.\n
                messaje: OK.\n
                level: INFO.\n
                description: Tu solicitud se procesó con éxito.\n
                """,200)
    elif code == 201:
        return (f"""
                code: {code}.\n
                messaje: Created.\n
                level: INFO.\n
                description: Solicitud realizada con éxito, se ha creado o cambiado un recurso en el servidor.\n
                """,201)