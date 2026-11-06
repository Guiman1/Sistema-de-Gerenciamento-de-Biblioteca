from configdb import db
from modelos.livro import Livro
from modelos.emprestimo import Emprestimo

class LivroDAO:

    @staticmethod
    def salvar_livro(livro):
        db.session.add(livro)
        db.session.commit()

    @staticmethod
    def listar_livros():
        return Livro.query.all()

    @staticmethod
    def buscar_livro_id(id):
        return db.session.get(Livro, id)

    @staticmethod
    def remover_livro(livro):
        try:
            Emprestimo.query.filter_by(livro_id=livro.id).delete()
            db.session.delete(livro)
            db.session.commit()
        except Exception:
            db.session.rollback()
            raise

    @staticmethod
    def atualizar_livro(livro):
        db.session.add(livro)
        db.session.commit()

    @staticmethod
    def buscar_isbn(isbn):
        return Livro.query.filter_by(isbn=isbn).first()

    @staticmethod
    def pesquisar_livro(titulo):
        return Livro.query.filter(
            db.or_(
                Livro.titulo.ilike('%' + titulo + '%'),
                Livro.autor.ilike('%' + titulo + '%')
            )
        ).all()