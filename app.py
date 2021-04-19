from flask import Flask, render_template, make_response, jsonify
from sql_client import SQLClient

app = Flask(__name__)


@app.route("/")
@app.route("/hello")
def do_string():
    return "Hello"


@app.route("/template_example")
def do_template():
    resp = make_response(render_template('index.html'))
    return resp


@app.route("/json_example")
def do_three():
    db_data = SQLClient().run_query("select * from test_table", None)

    resp = make_response(jsonify(db_data))
    return resp


def get_data_from_db():
    return {}


if __name__ == '__main__':
    app.run()
