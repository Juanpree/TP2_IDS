from flask import Flask, jsonify, request
from db import get_connection
from status_codes import mostrar_status_code


app = Flask(__name__)


@app.route("/usuarios", methods = ["GET"])
def listar_usuarios():
   conn = get_connection()
   cursor = conn.cursor(dictionary=True)

   #paginacion, muestra los datos divididos por la cantidad especificada en limit
   limit= request.args.get("_limit", 2, type=int)
   offset= request.args.get("_offset", 0, type=int)

   if limit <= 0 or offset <0:
       cursor.close()
       conn.close()
       return mostrar_status_code(400)
   cursor.execute("SELECT COUNT(*) AS total FROM usuarios")
   total= cursor.fetchone()["total"]

   cursor.execute("SELECT * FROM usuarios LIMIT %s OFFSET %s", (limit, offset))
   usuarios = cursor.fetchall()

   cursor.close()
   conn.close()
   
   base_url= request.base_url
   ultimo_offset= ((total-1)//limit) * limit if total > 0 else 0
   
   links={
       "_first": {"href": f"{base_url}?_offset=0"},
       "_prev": {"href": f"{base_url}?_offset={max(offset - limit, 0)}"},
       "_next": {"href": f"{base_url}?_offset={min(offset + limit, ultimo_offset)}"},
       "_last": {"href": f"{base_url}?_offset={ultimo_offset}"}
   }
   return jsonify({
       "usuarios": usuarios,
       "_links": links
       }), 200

@app.route("/usuarios", methods = ["POST"])
def agregar_usuario():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    data = request.json
    nombre = data.get("nombre")
    email = data.get("email")
    if not nombre or not email:
        return mostrar_status_code(400)

    cursor.execute("""INSERT INTO usuarios(nombre,email)VALUES(%s, %s)""",(nombre,email))
    conn.commit()
    cursor.close()
    conn.close()
    return mostrar_status_code(201)

@app.route("/usuarios/<int:id>", methods = ["GET"])
def obtener_usuario_por_id(id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM usuarios WHERE id = %s",(id,))
    usuario= cursor.fetchone()
    cursor.close()
    conn.close()
    if not usuario:
        return mostrar_status_code(404)
    return jsonify({"usuario": usuario})

@app.route("/usuarios/<int:id>", methods = ["PUT"])
def reemplazar_usuario_por_id(id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    data = request.json
    nombre = data.get("nombre")
    email = data.get("email")
    if not nombre:
        return mostrar_status_code(400)
    cursor.execute( """UPDATE usuarios SET nombre = %s, email = %s WHERE id = %s """,(nombre,email,id,))
    conn.commit()
    cursor.close()
    conn.close()
    return mostrar_status_code(204)

@app.route("/usuarios/<int:id>", methods = ["DELETE"])
def borrar_usuario(id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""DELETE FROM usuarios WHERE id = %s""",(id,))
    conn.commit()
    cursor.close()
    conn.close()
    return mostrar_status_code(204)

@app.route("/ranking", methods = ["GET"])
def mostrar_puntaje():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""SELECT usuarios.nombre, ranking.puntos FROM usuarios INNER JOIN ranking ON usuarios.id = ranking.id_usuario""")
    usuarios_con_puntaje = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify({"ranking": usuarios_con_puntaje}), 200

if __name__ == '__main__':
    app.run(port=8080, debug=True)

