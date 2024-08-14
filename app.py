from flask import Flask, render_template, redirect, request

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from forms import MarcaForm 
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/vehiculos_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models import Marca, Tipo, Vehiculo


vehiculos_json = {

  "vehiculos": [
    {
      "tipo": "Auto",
      "marca": "Toyota",
      "modelo": "Corolla",
      "cilindrada": "1800cc",
      "precio": "20000"
    },
    {
      "tipo": "Auto",
      "marca": "Honda",
      "modelo": "Civic",
      "cilindrada": "2000cc",
      "precio": "22000"
    },
    {
      "tipo": "Auto",
      "marca": "Ford",
      "modelo": "Focus",
      "cilindrada": "1600cc",
      "precio": "18000"
    },
    {
      "tipo": "Auto",
      "marca": "Chevrolet",
      "modelo": "Malibu",
      "cilindrada": "2500cc",
      "precio": "24000"
    },
    {
      "tipo": "Auto",
      "marca": "BMW",
      "modelo": "Serie 3",
      "cilindrada": "3000cc",
      "precio": "35000"
    },
    {
      "tipo": "Auto",
      "marca": "Audi",
      "modelo": "A4",
      "cilindrada": "2000cc",
      "precio": "33000"
    },
    {
      "tipo": "Auto",
      "marca": "Mercedes-Benz",
      "modelo": "Clase C",
      "cilindrada": "2200cc",
      "precio": "37000"
    },
    {
      "tipo": "Auto",
      "marca": "Hyundai",
      "modelo": "Elantra",
      "cilindrada": "2000cc",
      "precio": "19000"
    },
    {
      "tipo": "Motocicleta",
      "marca": "Yamaha",
      "modelo": "YZF-R3",
      "cilindrada": "321cc",
      "precio": "5000"
    },
    {
      "tipo": "Motocicleta",
      "marca": "Kawasaki",
      "modelo": "Ninja 400",
      "cilindrada": "399cc",
      "precio": "6000"
    }
  ]
}



@app.route("/")
def index():
    return render_template(
        'index.html'
    )

@app.route("/info")
def info():
    return render_template(
        'info.html'
    )

@app.route("/vehiculos")
def vehiculos():
    vehiculos_query = Vehiculo.query.all()
    print(vehiculos_query)
    return render_template(
        'vehiculos.html',
        vehiculos = vehiculos_query
    )

@app.route('/crear_vehiculo', methods=['POST', 'GET'])
def agregar_vehiculo():
    # EN SU METODO GET -> crear_vehiculo.html
    if request.method == 'GET':
        return render_template(
            'crear_vehiculo.html'
        )
    
    # EN SU METODO POST -> tomar la info que viene desde crear_vehiculo.html y 
    # agregarla a vehiculos_json e irse nuevamente al listado
    if request.method == 'POST':
        data = request.form
        tipo = data.get('tipo_vehiculo')
        marca = data.get('marca_vehiculo')
        modelo = data.get('modelo_vehiculo')
        precio = data.get('precio_vehiculo')
        cilindrada = data.get('cilindrada_vehiculo')
        
        nuevo_vehiculo = dict(
            marca=marca,
            tipo=tipo,
            modelo=modelo,
            precio=precio,
            cilindrada=cilindrada
        )

        vehiculos_json.get('vehiculos').append(nuevo_vehiculo)
        return redirect('vehiculos')