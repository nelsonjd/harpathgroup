from os import environ
from flask import g
from . import app
import sqlite3

DATABASE = environ.get('DATABASE')

if not DATABASE:
    raise ValueError('no database location provided in env.')

print('database location used: ' + DATABASE)

def get_con():
    con = getattr(g, '_database', None)
    if con is None:
        con = g._database = sqlite3.connect(DATABASE)
    return con

def query_db(query, args=(), one=False):
    con = get_con()
    con.row_factory = sqlite3.Row
    cur = con.execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

@app.teardown_appcontext
def close_connection(exception):
    con = getattr(g, '_database', None)
    if con is not None:
        con.close()

def init_db():
    with app.app_context():
        con = get_con()
        with app.open_resource('schema.sql', mode='r') as f:
            con.cursor().executescript(f.read())
        con.commit()

# to run - from project directory, do this.
# >>> from harpathgroup.db_runner import init_db
# >>> init_db()