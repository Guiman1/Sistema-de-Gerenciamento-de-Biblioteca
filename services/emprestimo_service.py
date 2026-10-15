from reposit.emprestimoDAO import EmprestimoDAO
from reposit.livroDAO import LivroDAO
from datetime import datetime

class EmprestimoService:

    @staticmethod
    def registrar_emprestimo(emprestimo):
        livro = LivroDAO.buscar_livro_id(emprestimo.livro_id)

        if livro is None:
            return "Nenhum livro cadastrado."

        elif livro.total_disponivel <= 0:
            return "Não hã nenhum livro disponível no momento."

        else:
            livro.total_disponivel -= 1
            LivroDAO.atualizar_livro(livro)
            EmprestimoDAO.criar_emprestimo(emprestimo)
            return "Emprestimo criado com sucesso!"

    @staticmethod
    def registrar_devolucao(emprestimo):
        emprestimo = EmprestimoDAO.buscar_emprestimo_id(emprestimo.id)


        if emprestimo is None:
            return "Não foi feito nenhum empréstimo."

        livro = LivroDAO.buscar_livro_id(emprestimo.livro_id)

        if livro is None:
            return "Nenhum livro cadastrado."

        if emprestimo.status == True:
            return "Esse livro ja fói devolvido!"

        elif emprestimo.status == False:
            emprestimo.data_devolucao = datetime.now()
            emprestimo.status = True
            livro.total_disponivel += 1
            LivroDAO.atualizar_livro(livro)
            EmprestimoDAO.atualizar_emprestimo(emprestimo)
            return "Livro devolvido com sucesso!"