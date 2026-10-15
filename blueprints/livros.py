from flask import Blueprint, render_template, request, redirect, url_for, flash

from configdb import db
from modelos.livro import Livro
from services.livro_service import LivroService

livros_bp = Blueprint('livros', __name__)

@livros_bp.route('/livros', methods=['GET', 'POST'])
def listar_livros():
    if request.method == 'POST':
        titulo = request.form['titulo']
        autor = request.form['autor']
        isbn = request.form.get('isbn')
        genero = request.form.get('categoria')
        ano = request.form.get('ano_publicacao')
        quantidade_total = int(request.form.get('quantidade_total', 1))

        novo_livro = Livro(
            titulo=titulo,
            autor=autor,
            isbn=isbn,
            genero=genero,
            ano_publicacao=int(ano) if ano else None,
            total_exemplares=quantidade_total,
            total_disponivel=quantidade_total,
        )

        db.session.add(novo_livro)
        db.session.commit()
        flash('Livro cadastrado com sucesso', 'sucesso')
        return redirect(url_for('livros.listar_livros'))

    busca = request.args.get('busca', '')

    if busca:
        livros = Livro.query.filter(
            Livro.titulo.ilike('%' + busca + '%') |
            Livro.autor.ilike('%' + busca + '%')
        ).all()
    else:
        livros = Livro.query.all()

    return render_template('livros.html', livros=livros)

@livros_bp.route('/livros/editar/<int:id>', methods=['GET', 'POST'])
def editar_livro(id):
    flash('Edição ainda não implementada', 'erro')
    return redirect(url_for('livros.listar_livros'))

@livros_bp.route('/livros/excluir/<int:id>', methods=['POST'])
def excluir_livro(id):
    mensagem = LivroService.remover_livro(id)
    flash(mensagem, 'sucesso' if 'sucesso' in mensagem.lower() else 'erro')
    return redirect(url_for('livros.listar_livros'))