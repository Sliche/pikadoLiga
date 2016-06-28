from flask import Flask
from flask.ext.mysqldb import MySQL

app = Flask(__name__)
app.config.from_object('config.config')
mysql = MySQL(app)
mysql.init_app(app)


import controller
