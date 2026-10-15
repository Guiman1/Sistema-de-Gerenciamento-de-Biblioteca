from configdb import db

class Livro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    autor = db.Column(db.String(50), nullable=False)
    genero = db.Column(db.String(20), nullable=False)
    ano_publicacao = db.Column(db.Integer)
    total_exemplares = db.Column(db.Integer, nullable=False, default=0)
    total_disponivel = db.Column(db.Integer, nullable=False, default=0)
    isbn = db.Column(db.String(13), nullable=False, unique=True)
