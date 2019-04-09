import os

from flask import Flask, jsonify
import psycopg2
from psycopg2.extras import RealDictCursor



# Initialize application
app = Flask(__name__)


def connect_db():
    DB_USER = os.environ["DB_USER"]
    DB_PASSWORD = os.environ["DB_PASSWORD"]
    DB_HOST = "cognitivo.cfz4dq8w2iii.us-east-1.rds.amazonaws.com"
    print(DB_USER, DB_PASSWORD, DB_HOST)
    con = psycopg2.connect(
        user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=5432, dbname="cognitivo"
    )
    return con


@app.route("/")
def top_apps():
    con = connect_db()
    cursor = con.cursor(cursor_factory=RealDictCursor)
    sql = "SELECT * FROM app.citacoes_20190409"
    cursor.execute(sql)
    data = cursor.fetchall()
    return jsonify(data)
