from configdb import db
from datetime import datetime

class Emprestimo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    livro_id = db.Column(db.Integer, db.ForeignKey('livro.id'), nullable=False,)
    usuario_id = db.Column(db.Integer, db.ForeignKey('livro.id'), nullable=False,)
    data_emprestimo = db.Column(db.DateTime, nullable=False, default=datetime.now)
    data_devolucao = db.Column(db.DateTime, nullable=True)
    status = db.Column(db.Boolean, nullable=False, default=False)