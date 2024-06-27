from flask import Flask, render_template, request

app = Flask(__name__)

from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:@localhost/vehiculos_db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)


from models import Marca, Tipo
listado_productos = [
    dict(
        name=dict(
            first='Parlante',
        ),
        ),

    dict(
        name=dict(
            first='cargador'
        ),
        ),
]


@app.route('/') # app es la instancia, route el metodo, '/' es el disparador
def index():
    return render_template(
        'index.html',
    )


@app.route('/productos')
def productos():
    listado = listado_productos    
    return render_template(
        'productos.html',
        listado = listado
        )

@app.route('/add_productos', methods=['GET', 'POST'])
def add_productos(): 
    if request.method == 'POST':
                    
        first_name = request.form['nombre'] 
        producto = dict(
            name=dict(
                first=first_name
            )
        )
        listado_productos.append(producto)
    return render_template('add_productos.html')







