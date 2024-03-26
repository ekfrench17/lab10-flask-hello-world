import psycopg2
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from Elaine French in 3008'

@app.route('/db_test')
def db_test():
    conn = psycopg2.connect("postgres://lab10_database_92pn_user:tZV2KiVcJT0fA9VB1hN1xbVdXw1CzT5n@dpg-co1jr2o21fec73d362s0-a/lab10_database_92pn")
    conn.close()
    return "Database Connection Successful"

@app.route('db_create')
def db_create():
    conn = psycopg2.connect("postgres://lab10_database_92pn_user:tZV2KiVcJT0fA9VB1hN1xbVdXw1CzT5n@dpg-co1jr2o21fec73d362s0-a/lab10_database_92pn")
    cur = conn.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS Basketball(
        First varchar(255),
        Last varchar(255),
        City varchar(255),
        Name varchar(255),
        Number int
        );
        ''')
    conn.commit()
    conn.close()
    return "Basketball table successfully created"