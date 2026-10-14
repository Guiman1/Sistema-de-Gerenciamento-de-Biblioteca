from flask import Blueprint, render_template, request, redirect, url_for, flash

from modelos.livro import Livro
from services.livro_service import LivroService

livros_bp = Blueprint('livros', __name__)

@livros_bp.route('/livros', methods=['GET', 'POST'])
def listar_livros():
    if request.method == 'POST':
        titulo = request.form['titulo']
        autor = request.form['autor']
        isbn = request.form['isbn']
        categoria = request.form['categoria']
        ano = request.form['ano']
        quantidade_total = int(request.form.get['quantidade_total', 1])

        novo_livro = Livro(
            titulo = titulo,
            autor = autor,
            isbn = isbn,
            tipo = categoria,
            ano_publicacao = int(ano) if ano else None,
            total_exemplares = quantidade_total,
            total_disponivel = quantidade_total,
        )

@livros_bp.route('/livros/editar/<int:id>', methods=['GET', 'POST'])
def editar_livro(id):
    pass

@livros_bp.route('/livros/excluir/<int:id>', methods=['GET', 'POST'])
def excluir_livro(id):
    mensagem = LivroService.remover_livro(id)
    flash(mensagem, 'Sucesso' if 'sucesso' in mensagem.lower() else 'Algo deu errado')
    return redirect(url_for('livros.listar_livro_bp'))