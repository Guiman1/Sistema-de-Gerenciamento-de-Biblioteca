from configdb import db
from modelos.emprestimo import Emprestimo

class EmprestimoDAO:

    @staticmethod
    def criar_emprestimo(emprestimo):
        db.session.add(emprestimo)
        db.session.commit()

    @staticmethod
    def buscar_emprestimo_id(emprestimo_id):
        return db.session.get(Emprestimo, emprestimo_id)

    @staticmethod
    def listar_emprestimos():
        return Emprestimo.query.all()

    @staticmethod
    def atualizar_emprestimo(emprestimo):
        db.session.add(emprestimo)
        db.session.commit()