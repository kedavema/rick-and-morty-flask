from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import requests

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# Database model
class Personaje(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    estado = db.Column(db.String(100))
    especie = db.Column(db.String(100))
    imagen = db.Column(db.String(250))

    def __init__(self, nombre, estado, especie, imagen):
        self.nombre = nombre
        self.estado = estado
        self.especie = especie
        self.imagen = imagen

    def __repr__(self):
        return f'<Personaje: {self.nombre}>'
  

# Endpoint principal de la aplicación
@app.route('/')
def index():
    respuesta = requests.get("https://rickandmortyapi.com/api/character").json()
    personajes = respuesta["results"]
    return render_template("index.html", personajes=personajes)
  

# Endpoint para guardar un personaje en la base de datos
@app.route('/guardar-personaje', methods=['POST'])
def guardar_personaje():
    nombre = request.form['nombre']
    estado = request.form['estado']
    especie = request.form['especie']
    imagen = request.form['imagen']
    personaje = Personaje(nombre=nombre, estado=estado, especie=especie, imagen=imagen)
    db.session.add(personaje)
    db.session.commit()
    return redirect(url_for('lista_personajes'))
  

# Endpoint para listar los personajes guardados en la base de datos  
@app.route('/lista-personajes')
def lista_personajes():
    personajes = Personaje.query.all()
    return render_template("lista_personajes.html", personajes=personajes)
  