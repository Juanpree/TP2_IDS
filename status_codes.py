
errors = [

    {   
        "code": "400.",
        "messaje": "Bad request.",
        "level": "ERROR.",
        "description": "El servidor no puede procesar tu solicitud, los datos ingresados pueden no ser correctos.\n"
    },
    {   
        "code": "404.",
        "messaje": "Not found.",
        "level": "ERROR.",
        "description": "La pagina que buscas ya no existe, se ha movido o escribiste mal la direccion URL.\n"
    },
    {   
        "code": "409.",
        "messaje": "Conflict.",
        "level": "ERROR.",
        "description": "Los datos ingresados ya existen."
    },
    {   
        "code": "500.",
        "messaje": "Internal Server Error.",
        "level": "ERROR.",
        "description": "Fallo inesperado del servidor, intenta recargar la pagina."
    }

]

status_ok = [

    {   
        "code": "200.",
        "messaje": "OK.",
        "level": "INFO.",
        "description": "Tu solicitud se procesó con éxito."
    },
    {   
        "code": "201.",
        "messaje": "Created.",
        "level": "INFO.",
        "description": "Solicitud realizada con éxito, se ha creado o cambiado un recurso en el servidor."
    },
    {   
        "code": "204.",
        "messaje": "No content.",
        "level": "INFO.",
        "description": "Solicitud procesada con exito pero NO hay información disponible para mostrar, no existe."
    }

]
