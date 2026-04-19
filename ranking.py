from flask import Blueprint, jsonify
from dataBase.db import get_connection
from status_codes import mostrar_status_code


ranking_bp = Blueprint("ranking", __name__)

@ranking_bp.route("", methods = ["GET"])
def mostrar_puntaje():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""SELECT usuarios.nombre, ranking.puntos FROM usuarios INNER JOIN ranking ON usuarios.id = ranking.id_usuario""")
    usuarios_con_puntaje = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify({"ranking": usuarios_con_puntaje}), 200