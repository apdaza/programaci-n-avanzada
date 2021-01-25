from flask import Flask, request, url_for, redirect, render_template, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///productos.db'
app.config['SECRET_KEY'] = "123"

db = SQLAlchemy(app)

class producto(db.Model):
    id = db.Column("producto_id", db.Integer, primary_key=True)
    producto_nombre = db.Column(db.String(100))
    producto_valor = db.Column(db.Integer)
    producto_cantidad = db.Column(db.Integer)
    
    def __init__(self, nombre, valor, cantidad):
        self.producto_nombre = nombre
        self.producto_valor = valor
        self.producto_cantidad = cantidad

@app.route("/")
def principal():
    return producto.query.all()

@app.route("/agregar/<nombre>")
def agregar(nombre):
    datos = {"producto_nombre": nombre, 
             "producto_cantidad": 100,
             "producto_valor": 10
    }

    p = producto(datos)
    db.session.add(p)
    db.session.commit()

if __name__ == "__main__":
    db.create_all()
    app.run()



