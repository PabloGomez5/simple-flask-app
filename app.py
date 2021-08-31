from flask import Flask, make_response, jsonify, request
from flask_cors import CORS
import json
import decimal
from datetime import datetime
from sql_client import SQLClient

app = Flask(__name__)
CORS(app)


def output_formatter(obj):
    """Convert decimals to a string"""
    if isinstance(obj, decimal.Decimal):
        return str(obj)
    if isinstance(obj, datetime.datetime):
        return str(obj)
    if isinstance(obj, datetime.date):
        return str(obj)


# Returna el mas utilizado
@app.route("/getMasUtilizado")
def get_mas_utilizado():
    db_data = SQLClient().run_query("SELECT jugador, SUM(minutos)  minutosTotal FROM Partidos GROUP BY  "
                                    "jugador ORDER BY minutosTotal DESC;", None)
    print(db_data)
    data = json.dumps(db_data, default=output_formatter)
    resp = make_response(data)

    return resp


# Returna el pichichi del equipo
@app.route("/getPichichi")
def get_pichichi():
    db_data = SQLClient().run_query("SELECT jugador, SUM(goles) golesTotal FROM Partidos GROUP BY "
                                    " jugador ORDER BY golesTotal DESC;", None)
    print(db_data)
    data = json.dumps(db_data, default=output_formatter)
    resp = make_response(data)

    return resp


@app.route("/")
@app.route("/hello")
def do_string():
    return "Hello"


# Returna la tabla convocatoria
@app.route("/getConvocatoria")
def get_convocatoria():
    db_data = SQLClient().run_query("select * from Convocatoria", None)

    resp = make_response(jsonify(db_data))
    return resp


# Returna la tablas 3 ultimos entrenos....
@app.route("/getTresUltEntrenos")
def getTresUltEntrenos():
    # num_entrenos_list = SQLClient().run_query("SELECT numEntrenamiento from Entrenamientos WHERE dorsal=1", None)
    # num1 = len(num_entrenos_list)
    # num2 = (num1 - 1)
    # num3 = (num1 - 2)
    query = "select numEntrenamiento,jugador,asistencia,rendimiento from Entrenamientos where numEntrenamiento = 2 " \
            "OR numEntrenamiento = 1 OR numEntrenamiento = 0 "
    # TODO PREGUNTAR A WARREN
    db_data = SQLClient().run_query(query, None)

    resp = make_response(jsonify(db_data))
    return resp


# Returna jugadores con dorsal y posicion
@app.route("/getJugadoresPlantilla")
def get_jugadores():
    db_data = SQLClient().run_query("select dorsal, jugador, posicion, numEntrenamientos from Jugadores", None)

    resp = make_response(jsonify(db_data))
    return resp


# Returna un jugador en función del dorsal...
@app.route("/getJugadorCompletaEntrenos", methods=['POST'])
def get_jugador_completa_entrenos():
    req_data = request.get_json()
    jugador = req_data["jugador"]

    db_data = SQLClient().run_query("select numEntrenamiento, fecha, asistencia, rendimiento from Entrenamientos "
                                    "where jugador = '" + jugador + "'", None)

    resp = make_response(jsonify(db_data))
    return resp


# Returna un jugador en función del dorsal...
@app.route("/getJugadorCompletaPartidos", methods=['POST'])
def get_jugador_completa_partidos():
    req_data = request.get_json()
    jugador = req_data["jugador"]

    # CAMBIAR EL SELECT A LO DE PARTIDOS
    db_data = SQLClient().run_query("select * from Partidos where jugador = '" + jugador + "'", None)

    resp = make_response(jsonify(db_data))
    return resp


# Returna la lista de rivales
@app.route("/getCalendarioRivals")
def get_calendario_rivals():
    db_data = SQLClient().run_query("select rival, campo, fecha from Calendario", None)

    resp = make_response(jsonify(db_data))
    return resp


# Returna la lista de rivales
@app.route("/getPlantillaData")
def get_plantilla_data():
    db_data = SQLClient().run_query("select * from Jugadores", None)

    resp = make_response(jsonify(db_data))
    return resp


# Returna un jugador en función del dorsal...
@app.route("/getPartidoData", methods=['POST'])
def get_partido_data():
    req_data = request.get_json()
    partido = req_data["partido"]

    partido_data = partido.split(',')

    # CAMBIAR EL SELECT A LO DE PARTIDOS
    db_data = SQLClient().run_query("select * from Partidos where rival = '" + partido_data[0] + "' AND campo = '"
                                    + partido_data[1] + "'", None)

    resp = make_response(jsonify(db_data))
    return resp


# Returna las tarjetas del banquillo...
@app.route("/getBanquillo")
def get_banquillo():
    db_data = SQLClient().run_query("select * from Entrenadores", None)

    resp = make_response(jsonify(db_data))
    return resp


# Returna el jugador con mas asistencias
@app.route("/getAsistente")
def get_asistente():
    db_data = SQLClient().run_query("select * from Entrenadores", None)

    resp = make_response(jsonify(db_data))
    return resp


# Returna Mas amarillas
@app.route("/getMasAmarillas")
def get_mas_Amarillas():
    db_data = SQLClient().run_query("select * from Entrenadores", None)

    resp = make_response(jsonify(db_data))
    return resp


# Returna Mas tarjetas rojas
@app.route("/getMasRojas")
def get_mas_rojas():
    db_data = SQLClient().run_query("select * from Entrenadores", None)

    resp = make_response(jsonify(db_data))
    return resp


if __name__ == '__main__':
    app.run()
