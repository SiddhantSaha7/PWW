# from website import create_app

import pymysql
pymysql.install_as_MySQLdb()
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from models import db, PUBLIC_ACCESS_VIEW
from config import Config



#app = create_app()
app = Flask (__name__)
app.config.from_object(Config)
db.init_app(app)

@app.route('/home', methods=['GET','POST'])
def landing_page():
    data = PUBLIC_ACCESS_VIEW.query.all()
    return render_template('landing_page.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
