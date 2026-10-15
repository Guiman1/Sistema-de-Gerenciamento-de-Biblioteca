from modelos import livro
from reposit.livroDAO import LivroDAO
from modelos.livro import Livro

class LivroService:


    @staticmethod
    def cadastrar_livro(livro):

        if livro.total_disponivel > livro.total_exemplares:
            return "A quantidade disponível não pode ser maior que o total de exemplares."

        if livro.total_exemplares < 0 or livro.total_disponivel < 0:
            return "As quantidades não podem ser negativas."

        livro_existente = LivroDAO.buscar_isbn(livro.isbn)

        if livro_existente:
            return "Já tem uma ISBN cadastrada."
        else:
            LivroDAO.salvar_livro(livro)
            return "Este livro foi cadastrado com successo."

    @staticmethod
    def listar_livros():
        return LivroDAO.listar_livros()

    @staticmethod
    def buscar_livro_id(livro_id):
        livro = LivroDAO.buscar_livro_id(livro_id)

        if livro is None:
            return None

        return livro

    @staticmethod
    def remover_livro(livro_id):
          livro = LivroDAO.buscar_livro_id(livro_id)

          if livro:
            LivroDAO.remover_livro(livro)
            return "Livro removido com sucesso."
          else:
            return "Esse livro não existe, tente outro."

    @staticmethod
    def pesquisar_livros(livro_titulo):
        return LivroDAO.pesquisar_livro(livro_titulo)

    @staticmethod
    def atualizar_livro(livro_id, total_exemplares, total_disponivel):
        livro = LivroDAO.buscar_livro_id(livro_id)

        if livro is None:
            return "Livro não encontrado."

        elif total_disponivel > total_exemplares:
            return "A quantidade disponível não pode ser maior que o total de exemplares."

        elif total_exemplares < 0 or total_disponivel < 0:
            return "As quantidades não podem ser negativas."

        else:
            livro.total_exemplares = total_exemplares
            livro.total_disponivel = total_disponivel

            LivroDAO.atualizar_livro(livro)

            return "Livro atualizado com sucesso."