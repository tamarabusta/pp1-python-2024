from app import db

class Marca(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(30), nullable=False)

    def __str__(self):
        return self.nombre

class Tipo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(30), nullable=False)

    def __str__(self):
        return self.nombre
    
class Vehiculo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    modelo = db.Column(db.Integer)
    cilindrada = db.Column(db.Integer)

    marca_id = db.Column(db.Integer, db.ForeignKey('marca.id'), nullable=False) 
    tipo_id = db.Column(db.Integer, db.ForeignKey('tipo.id'), nullable=False)
    
    tipo = db.relationship('Tipo', backref=db.backref('vehiculos', lazy=True))  
    marca = db.relationship('Marca', backref=db.backref('vehiculos', lazy=True))  


