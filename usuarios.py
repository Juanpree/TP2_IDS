

from flask import jsonify, request, Blueprint
from db import get_connection
from status_codes import errors, status_ok


usuarios_bp = Blueprint("usuarios",__name__)

@usuarios_bp.route("", methods = ["GET"])
def listar_usuarios():
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
    except:
        return jsonify({"errors":errors[3]}),500

    #paginacion, muestra los datos divididos por la cantidad especificada en limit
    limit= request.args.get("_limit", 2, type=int)
    offset= request.args.get("_offset", 0, type=int)

    if limit <= 0 or offset <0:
            cursor.close()
            conn.close()
            return jsonify(errors[0]), 400
    cursor.execute("SELECT COUNT(*) AS total FROM usuarios")
    total= cursor.fetchone()["total"]

    if not total:
            return jsonify(),204

    cursor.execute("SELECT * FROM usuarios LIMIT %s OFFSET %s", (limit, offset))
    usuarios = cursor.fetchall()
        
    base_url= request.base_url
    ultimo_offset= ((total-1)//limit) * limit if total > 0 else 0
   
    links={
       "_first": {"href": f"{base_url}?_offset=0"},
       "_prev": {"href": f"{base_url}?_offset={max(offset - limit, 0)}"},
       "_next": {"href": f"{base_url}?_offset={min(offset + limit, ultimo_offset)}"},
       "_last": {"href": f"{base_url}?_offset={ultimo_offset}"}
        }
    cursor.close()
    conn.close()
    return jsonify({
            "usuarios": usuarios,
            "_links": links
            }), 200

@usuarios_bp.route("", methods = ["POST"])
def agregar_usuario():
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
    except:
         return jsonify({"errors":errors[3]}),500

    data = request.json
    nombre = data.get("nombre")
    email = data.get("email")

    if not nombre or not email:
        return jsonify({"errors":errors[0]}),400
    
    cursor.execute("""INSERT INTO usuarios(nombre,email)VALUES(%s, %s)""",(nombre,email))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify(),201

@usuarios_bp.route("/<int:id>", methods = ["GET"])
def obtener_usuario_por_id(id):
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
    except:
         return jsonify({"errors":errors[3]}),500
    
         
    cursor.execute("SELECT * FROM usuarios WHERE id = %s",(id,))
    usuario= cursor.fetchone()
    cursor.close()
    conn.close()
    if not usuario:
        return jsonify({"errors":errors[1]}),404
    
    return jsonify({"usuario": usuario}),200

@usuarios_bp.route("/<int:id>", methods = ["PUT"])
def reemplazar_usuario_por_id(id):
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
    except: 
        return jsonify({"errors":errors[3]}),500
    data = request.json
    nombre = data.get("nombre")
    email = data.get("email")
    if not nombre:
        return jsonify({"errors":errors[0]}),400
    cursor.execute( """UPDATE usuarios SET nombre = %s, email = %s WHERE id = %s """,(nombre,email,id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify(),204

@usuarios_bp.route("/<int:id>", methods = ["DELETE"])
def borrar_usuario(id):
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
    except:
        return jsonify({"errors":errors[3]}),500
    
    
         
    cursor.execute("""DELETE FROM usuarios WHERE id = %s""",(id,))
    conn.commit()
    filas_borradas = cursor.rowcount
    
    if filas_borradas == 0:
         return jsonify({"errors":[errors[1]]}),404
    
    cursor.close()
    conn.close()
   
    return jsonify(),204
    
    
