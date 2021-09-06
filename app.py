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


@app.route("/")
@app.route("/hello")
def do_string():
    return "Hello"


# Returna el mas utilizado
@app.route("/getMasUtilizado")
def get_mas_utilizado():
    db_data = SQLClient().run_query("SELECT jugador, SUM(minutos)  minutosTotal FROM Partidos GROUP BY  "
                                    "jugador ORDER BY minutosTotal DESC;", None)
    data = json.dumps(db_data, default=output_formatter)
    resp = make_response(data)

    return resp


# Returna el pichichi del equipo
@app.route("/getPichichi")
def get_pichichi():
    db_data = SQLClient().run_query("SELECT jugador, SUM(goles) golesTotal FROM Partidos GROUP BY "
                                    " jugador ORDER BY golesTotal DESC;", None)
    data = json.dumps(db_data, default=output_formatter)
    resp = make_response(data)

    return resp


# Returna el max asistente del equipo
@app.route("/getAsistente")
def get_mas_asistente():
    db_data = SQLClient().run_query("SELECT jugador, SUM(asistencias) asistenciasTotal FROM Partidos GROUP BY "
                                    " jugador ORDER BY asistenciasTotal DESC;", None)
    data = json.dumps(db_data, default=output_formatter)
    resp = make_response(data)

    return resp


# Returna el jugador con + tarjetas amarillas del equipo
@app.route("/getMasAmarillas")
def get_mas_amarillas():
    db_data = SQLClient().run_query("SELECT jugador, SUM(amarillas) amarillasTotal FROM Partidos GROUP BY "
                                    " jugador ORDER BY amarillasTotal DESC;", None)
    data = json.dumps(db_data, default=output_formatter)
    resp = make_response(data)

    return resp


# Returna el jugador con + tarjetas rojas del equipo
@app.route("/getMasRojas")
def get_mas_rojas():
    db_data = SQLClient().run_query("SELECT jugador, SUM(roja) rojasTotal FROM Partidos GROUP BY "
                                    " jugador ORDER BY rojasTotal DESC;", None)
    data = json.dumps(db_data, default=output_formatter)
    resp = make_response(data)

    return resp


# Returna la tabla convocatoria
@app.route("/getConvocatoria")
def get_convocatoria():
    db_data = SQLClient().run_query("select * from Convocatoria", None)

    resp = make_response(jsonify(db_data))
    return resp


# Returna rendimiento medio entreno
@app.route("/getRendEntrenamientos")
def get_rend_entrenamientos():
    rendimiento_total = SQLClient().run_query("SELECT SUM(rendimiento) rendimientoTotal FROM Entrenamientos ORDER BY "
                                              "rendimientoTotal DESC", None)

    filas = SQLClient().run_query("SELECT count('jugador') FROM Entrenamientos", None)

    result = rendimiento_total[0]['rendimientoTotal'] / filas[0]["count('jugador')"]

    result_entero = round(result)

    data = json.dumps(result_entero, default=output_formatter)
    resp = make_response(data)

    return resp


# Returna rendimiento medio partido
@app.route("/getRendPartidos")
def get_rend_partidos():
    rendimiento_total = SQLClient().run_query("SELECT SUM(rendimiento) rendimientoTotal FROM Partidos ORDER BY "
                                              "rendimientoTotal DESC", None)

    filas = SQLClient().run_query("SELECT count('jugador') FROM Partidos", None)

    result = rendimiento_total[0]['rendimientoTotal'] / filas[0]["count('jugador')"]

    result_entero = round(result)

    data = json.dumps(result_entero, default=output_formatter)
    resp = make_response(data)

    return resp


# Returna la tablas 3 ultimos entrenos....
@app.route("/getTresUltEntrenos")
def get_tres_ult_entrenos():
    num_entrenos_list = SQLClient().run_query("SELECT numEntrenamiento from Entrenamientos WHERE dorsal=1", None)
    num1 = len(num_entrenos_list)
    num2 = (num1 - 1)
    num3 = (num1 - 2)
    query = "select numEntrenamiento,jugador,asistencia,rendimiento from Entrenamientos where numEntrenamiento = "
    query += f"{num1} OR numEntrenamiento = "
    query += f"{num2} OR numEntrenamiento = "
    query += f"{num3}"

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


# REGISTRO DE UN PARTIDO
@app.route("/registerMatch", methods=['POST'])
def registrar_match():
    req_data = request.get_json()

    num_partido = req_data["numeroPartido"]
    fecha = req_data["fecha"]
    campo = req_data["campo"]
    rival = req_data["rival"]
    resultado = req_data["resultado"]
    dorsal = req_data["dorsal"]
    jugador = req_data["jugador"]
    posicion = req_data["posicion"]
    convocado = req_data["convocado"]
    titular = req_data["titular"]
    minutos = req_data["minutos"]
    asistencias = req_data["asistencias"]
    goles = req_data["goles"]
    amarillas = req_data["amarillas"]
    roja = req_data["roja"]
    rendimiento = req_data["rendimiento"]
    mvp = req_data["mvp"]
    desconvocado = req_data["desconvocado"]

    # REGISTRA EN LA TABLA PARTIDOS
    query = "INSERT INTO Partidos (numPartido, fecha, rival, campo, resultado, dorsal, "
    query += "jugador, convocado, titular, minutos, posicion, asistencias, goles, amarillas, "
    query += "roja, rendimiento, mvp) VALUES ("
    query += f"{num_partido}, '{fecha}', '{rival}', '{campo}', '{resultado}', {dorsal},"
    query += f"'{jugador}', {convocado}, {titular}, {minutos}, '{posicion}', {asistencias},"
    query += f"{goles}, {amarillas}, {roja}, {rendimiento}, {mvp})"
    SQLClient().run_update(query, None)

    # ACTUALIZA LA TABLA PLANTILLA ( JUGADORES )
    query_plantilla = "UPDATE Jugadores SET numPartidos = numPartidos +"
    query_plantilla += f"{convocado}, rendPartidos = "
    query_plantilla += "(((SELECT SUM(rendimiento)  rendimientoTotal FROM Partidos WHERE jugador = "
    query_plantilla += f"'{jugador}')) / numPartidos)  WHERE jugador = "
    query_plantilla += f"'{jugador}'"
    SQLClient().run_update(query_plantilla, None)

    # ACTUALIZA LA TABLA CONVOCATORIAS
    query_convocatorias = "UPDATE Convocatoria SET convocado = convocado + "
    query_convocatorias += f"{convocado} , desconvocado = desconvocado + "
    query_convocatorias += f"{desconvocado}, titular = titular + "
    query_convocatorias += f"{titular}, minutos = minutos + "
    query_convocatorias += f"{minutos}, rendimiento = ((SELECT rendPartidos FROM Jugadores WHERE jugador = "
    query_convocatorias += f"'{jugador}')) WHERE jugador = "
    query_convocatorias += f"'{jugador}'"
    SQLClient().run_update(query_convocatorias, None)

    resp = make_response(jsonify("Registrado Exitosamente"))
    return resp


# REGISTRO DE UN ENTRENO
@app.route("/registerNewPractice", methods=['POST'])
def registrar_practise():
    req_data = request.get_json()

    num_entreno = req_data["numeroEntrenamiento"]
    fecha = req_data["fecha"]
    dia = req_data["dia"]
    dorsal = req_data["dorsal"]
    jugador = req_data["jugador"]
    asistencia = req_data["asistencia"]
    rendimiento = req_data["rendimiento"]

    # REGISTRA EN LA TABLA ENTRENAMIENTOS
    query = "INSERT INTO Entrenamientos (numEntrenamiento, fecha, dia, dorsal, "
    query += "jugador, asistencia, rendimiento) VALUES ("
    query += f"{num_entreno}, '{fecha}', '{dia}',{dorsal},"
    query += f"'{jugador}', {asistencia}, {rendimiento})"
    SQLClient().run_update(query, None)

    # ACTUALIZA LA TABLA PLANTILLA ( JUGADORES )
    query_plantilla = "UPDATE Jugadores SET numEntrenamientos = numEntrenamientos +"
    query_plantilla += f"{asistencia}, rendEntrenamientos = "
    query_plantilla += "(((SELECT SUM(rendimiento)  rendimientoTotal FROM Entrenamientos WHERE jugador = "
    query_plantilla += f"'{jugador}')) / numEntrenamientos)  WHERE jugador = "
    query_plantilla += f"'{jugador}'"
    SQLClient().run_update(query_plantilla, None)
    print(query_plantilla)

    resp = make_response(jsonify("Registrado Exitosamente"))
    return resp


if __name__ == '__main__':
    app.run()
