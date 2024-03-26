import psycopg2
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from Elaine French in 3308'

@app.route('/db_test')
def test():
    conn = psycopg2.connect("postgres://lab10_database_92pn_user:tZV2KiVcJT0fA9VB1hN1xbVdXw1CzT5n@dpg-co1jr2o21fec73d362s0-a/lab10_database_92pn")
    conn.close()
    return "Database Connection Successful"

@app.route('/db_create')
def create():
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
    return "Basketball Table Successfully Created"

@app.route('/db_insert')
def insert():
    conn = psycopg2.connect("postgres://lab10_database_92pn_user:tZV2KiVcJT0fA9VB1hN1xbVdXw1CzT5n@dpg-co1jr2o21fec73d362s0-a/lab10_database_92pn")
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO Basketball (First, Last, City, Name, Number)
        Values
        ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
        ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
        ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
        ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2);
        ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Populated"

@app.route('/db_select')
def select():
    conn = psycopg2.connect("postgres://lab10_database_92pn_user:tZV2KiVcJT0fA9VB1hN1xbVdXw1CzT5n@dpg-co1jr2o21fec73d362s0-a/lab10_database_92pn")
    cur = conn.cursor()
    cur.execute('''
        SELECT * FROM Basketball;
        ''')
    records = cur.fetchall()
    conn.close()
    response_string = "<table>"
    for record in records:
        response_string += "<tr>"
        for info in record:
            response_string += "<td>{}</td>".format(info)
        response_string += "</tr>"
    response_string += "</table"
    return response_string

@app.route('/db_drop')
def drop():
    conn = psycopg2.connect("postgres://lab10_database_92pn_user:tZV2KiVcJT0fA9VB1hN1xbVdXw1CzT5n@dpg-co1jr2o21fec73d362s0-a/lab10_database_92pn")
    cur = conn.cursor()
    cur.execute("DROP TABLE Basketball;")
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Dropped"
    
    