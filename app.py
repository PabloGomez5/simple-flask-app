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

    data = req_data["dataCompletaPartido"]


    # REGISTRA EN LA TABLA PARTIDOS
    #query = "INSERT INTO Partidos (numPartido, fecha, rival, campo, resultado, dorsal, "
    #query += "jugador, convocado, titular, minutos, posicion, asistencias, goles, amarillas, "
    #query += "roja, rendimiento, mvp) VALUES ("

    #query += f"{num_partido}, '{fecha}', '{rival}', '{campo}', '{resultado}', {dorsal},"
    #query += f"'{jugador}', {convocado}, {titular}, {minutos}, '{posicion}', {asistencias},"
    #query += f"{goles}, {amarillas}, {roja}, {rendimiento}, {mvp})"
    #SQLClient().run_update(query, None)

    query = "INSERT INTO Partidos (numPartido, fecha, rival, campo, resultado, dorsal, "
    query += "jugador, convocado, titular, minutos, asistencias, goles, amarillas, "
    query += "roja, rendimiento, mvp) VALUES ("

    query += f"{data[0]}, '{data[1]}', '{data[3]}', '{data[2]}', '{data[4]}', {data[5][0]},"
    query += f"'{data[5][1]}', {data[5][2]}, {data[5][4]}, {data[5][5]}, {data[5][7]},"
    query += f"{data[5][6]}, {data[5][8]}, {data[5][9]}, {data[5][10]}, {data[5][11]}),("

    query += f"{data[0]}, '{data[1]}', '{data[3]}', '{data[2]}', '{data[4]}', {data[6][0]},"
    query += f"'{data[6][1]}', {data[6][2]}, {data[6][4]}, {data[6][5]}, {data[6][7]},"
    query += f"{data[6][6]}, {data[6][8]}, {data[6][9]}, {data[6][10]}, {data[6][11]}),("

    query += f"{data[0]}, '{data[1]}', '{data[3]}', '{data[2]}', '{data[4]}', {data[7][0]},"
    query += f"'{data[7][1]}', {data[7][2]}, {data[7][4]}, {data[7][5]}, {data[7][7]},"
    query += f"{data[7][6]}, {data[7][8]}, {data[7][9]}, {data[7][10]}, {data[7][11]}),("

    query += f"{data[0]}, '{data[1]}', '{data[3]}', '{data[2]}', '{data[4]}', {data[8][0]},"
    query += f"'{data[8][1]}', {data[8][2]}, {data[8][4]}, {data[8][5]}, {data[8][7]},"
    query += f"{data[8][6]}, {data[8][8]}, {data[8][9]}, {data[8][10]}, {data[8][11]}),("

    # los data[8][n] a data[9][n]
    query += f"{data[0]}, '{data[1]}', '{data[3]}', '{data[2]}', '{data[4]}', {data[9][0]},"
    query += f"'{data[9][1]}', {data[9][2]}, {data[9][4]}, {data[9][5]}, {data[9][7]},"
    query += f"{data[9][6]}, {data[9][8]}, {data[9][9]}, {data[9][10]}, {data[9][11]}),("

    # los 8 a 10
    query += f"{data[0]}, '{data[1]}', '{data[3]}', '{data[2]}', '{data[4]}', {data[10][0]},"
    query += f"'{data[10][1]}', {data[10][2]}, {data[10][4]}, {data[10][5]}, {data[10][7]},"
    query += f"{data[10][6]}, {data[10][8]}, {data[10][9]}, {data[10][10]}, {data[10][11]}),("

    # 8 to 11
    query += f"{data[0]}, '{data[1]}', '{data[3]}', '{data[2]}', '{data[4]}', {data[11][0]},"
    query += f"'{data[11][1]}', {data[11][2]}, {data[11][4]}, {data[11][5]}, {data[11][7]},"
    query += f"{data[11][6]}, {data[11][8]}, {data[11][9]}, {data[11][10]}, {data[11][11]}),("

    # 8 to 12
    query += f"{data[0]}, '{data[1]}', '{data[3]}', '{data[2]}', '{data[4]}', {data[12][0]},"
    query += f"'{data[12][1]}', {data[12][2]}, {data[12][4]}, {data[12][5]}, {data[12][7]},"
    query += f"{data[12][6]}, {data[12][8]}, {data[12][9]}, {data[12][10]}, {data[12][11]}),("

    # 8 to 13
    query += f"{data[0]}, '{data[1]}', '{data[3]}', '{data[2]}', '{data[4]}', {data[13][0]},"
    query += f"'{data[13][1]}', {data[13][2]}, {data[13][4]}, {data[13][5]}, {data[13][7]},"
    query += f"{data[13][6]}, {data[13][8]}, {data[13][9]}, {data[13][10]}, {data[13][11]}),("

    # 8 to 14
    query += f"{data[0]}, '{data[1]}', '{data[3]}', '{data[2]}', '{data[4]}', {data[14][0]},"
    query += f"'{data[14][1]}', {data[14][2]}, {data[14][4]}, {data[14][5]}, {data[14][7]},"
    query += f"{data[14][6]}, {data[14][8]}, {data[14][9]}, {data[14][10]}, {data[14][11]}),("

    # 8 to 15
    query += f"{data[0]}, '{data[1]}', '{data[3]}', '{data[2]}', '{data[4]}', {data[15][0]},"
    query += f"'{data[15][1]}', {data[15][2]}, {data[15][4]}, {data[15][5]}, {data[15][7]},"
    query += f"{data[15][6]}, {data[15][8]}, {data[15][9]}, {data[15][10]}, {data[15][11]}),("

    # 8 to 16
    query += f"{data[0]}, '{data[1]}', '{data[3]}', '{data[2]}', '{data[4]}', {data[16][0]},"
    query += f"'{data[16][1]}', {data[16][2]}, {data[16][4]}, {data[16][5]}, {data[16][7]},"
    query += f"{data[16][6]}, {data[16][8]}, {data[16][9]}, {data[16][10]}, {data[16][11]}),("

    # 8 to 17
    query += f"{data[0]}, '{data[1]}', '{data[3]}', '{data[2]}', '{data[4]}', {data[17][0]},"
    query += f"'{data[17][1]}', {data[17][2]}, {data[17][4]}, {data[17][5]}, {data[17][7]},"
    query += f"{data[17][6]}, {data[17][8]}, {data[17][9]}, {data[17][10]}, {data[17][11]}),("

    # 8 to 18
    query += f"{data[0]}, '{data[1]}', '{data[3]}', '{data[2]}', '{data[4]}', {data[18][0]},"
    query += f"'{data[18][1]}', {data[18][2]}, {data[18][4]}, {data[18][5]}, {data[18][7]},"
    query += f"{data[18][6]}, {data[18][8]}, {data[18][9]}, {data[18][10]}, {data[18][11]}),("

    # 8 to 19
    query += f"{data[0]}, '{data[1]}', '{data[3]}', '{data[2]}', '{data[4]}', {data[19][0]},"
    query += f"'{data[19][1]}', {data[19][2]}, {data[19][4]}, {data[19][5]}, {data[19][7]},"
    query += f"{data[19][6]}, {data[19][8]}, {data[19][9]}, {data[19][10]}, {data[19][11]}),("

    # 8 to 20
    query += f"{data[0]}, '{data[1]}', '{data[3]}', '{data[2]}', '{data[4]}', {data[20][0]},"
    query += f"'{data[20][1]}', {data[20][2]}, {data[20][4]}, {data[20][5]}, {data[20][7]},"
    query += f"{data[20][6]}, {data[20][8]}, {data[20][9]}, {data[20][10]}, {data[20][11]}),("

    # 8 to 21
    query += f"{data[0]}, '{data[1]}', '{data[3]}', '{data[2]}', '{data[4]}', {data[21][0]},"
    query += f"'{data[21][1]}', {data[21][2]}, {data[21][4]}, {data[21][5]}, {data[21][7]},"
    query += f"{data[21][6]}, {data[21][8]}, {data[21][9]}, {data[21][10]}, {data[21][11]}),("

    # 8 to 22
    query += f"{data[0]}, '{data[1]}', '{data[3]}', '{data[2]}', '{data[4]}', {data[22][0]},"
    query += f"'{data[22][1]}', {data[22][2]}, {data[22][4]}, {data[22][5]}, {data[22][7]},"
    query += f"{data[22][6]}, {data[22][8]}, {data[22][9]}, {data[22][10]}, {data[22][11]}),("

    # 8 to 23
    query += f"{data[0]}, '{data[1]}', '{data[3]}', '{data[2]}', '{data[4]}', {data[23][0]},"
    query += f"'{data[23][1]}', {data[23][2]}, {data[23][4]}, {data[23][5]}, {data[23][7]},"
    query += f"{data[23][6]}, {data[23][8]}, {data[23][9]}, {data[23][10]}, {data[23][11]}),("

    # 8 to 24
    query += f"{data[0]}, '{data[1]}', '{data[3]}', '{data[2]}', '{data[4]}', {data[24][0]},"
    query += f"'{data[24][1]}', {data[24][2]}, {data[24][4]}, {data[24][5]}, {data[24][7]},"
    query += f"{data[24][6]}, {data[24][8]}, {data[24][9]}, {data[24][10]}, {data[24][11]}),("

    # 8 to 25
    query += f"{data[0]}, '{data[1]}', '{data[3]}', '{data[2]}', '{data[4]}', {data[25][0]},"
    query += f"'{data[25][1]}', {data[25][2]}, {data[25][4]}, {data[25][5]}, {data[25][7]},"
    query += f"{data[25][6]}, {data[25][8]}, {data[25][9]}, {data[25][10]}, {data[25][11]}),("

    # 8 to 26
    query += f"{data[0]}, '{data[1]}', '{data[3]}', '{data[2]}', '{data[4]}', {data[26][0]},"
    query += f"'{data[26][1]}', {data[26][2]}, {data[26][4]}, {data[26][5]}, {data[26][7]},"
    query += f"{data[26][6]}, {data[26][8]}, {data[26][9]}, {data[26][10]}, {data[26][11]})"

    print("--------------------->>>>>>>>>>>>><", query)

    # ACTUALIZA LA TABLA PLANTILLA ( JUGADORES )
    #query_plantilla = "UPDATE Jugadores SET numPartidos = numPartidos +"
    #query_plantilla += f"{convocado}, rendPartidos = "
    #query_plantilla += "(((SELECT SUM(rendimiento)  rendimientoTotal FROM Partidos WHERE jugador = "
    #query_plantilla += f"'{jugador}')) / numPartidos)  WHERE jugador = "
    #query_plantilla += f"'{jugador}'"
    #SQLClient().run_update(query_plantilla, None)

    # ACTUALIZA LA TABLA CONVOCATORIAS
    #query_convocatorias = "UPDATE Convocatoria SET convocado = convocado + "
    #query_convocatorias += f"{convocado} , desconvocado = desconvocado + "
    #query_convocatorias += f"{desconvocado}, titular = titular + "
    #query_convocatorias += f"{titular}, minutos = minutos + "
    #query_convocatorias += f"{minutos}, rendimiento = ((SELECT rendPartidos FROM Jugadores WHERE jugador = "
    #query_convocatorias += f"'{jugador}')) WHERE jugador = "
    #query_convocatorias += f"'{jugador}'"
    #SQLClient().run_update(query_convocatorias, None)

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
