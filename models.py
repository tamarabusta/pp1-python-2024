from app import db

class Marca(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(30), nullable=False)
    
    def _str_(self):
        return self.nombre
    
class Tipo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(30), nullable=False)
    
    def _str_(self):
        return self.nombre 
    
    class Vehiculo(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        modelo= db. Column(db.String(30), nullable=False)
        cilindrada = db.column(db.Integer)
        tipo_id = db.Column(db.Integer, db.ForeignKey('tipo.id'), nullable=False)
        marca_id = db.Column(db.Integer, db.ForeignKey('marca.id'), nullable=False)
        
        tipo = db.relationship("Tipo", backref=db.backref("Vehiculos", lazy=True))
        marca = db.relationship("Marca", backref=db.backref("Vehiculos", lazy=True))
        
        def _str_(self):
            return self.modelo