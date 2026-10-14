from flask import Blueprint, render_template, request, redirect, url_for, flash
from datetime import datetime
from modelos.emprestimo import Emprestimo
from modelos.livro import Livro
from services.emprestimo_service import EmprestimoService
from reposit.livroDAO import LivroDAO

emprestimos_bp = Blueprint('emprestimos', __name__)

@emprestimos_bp.route('/emprestimos', methods=['GET', 'POST'])
def listar_emprestimos():
    if request.method == 'POST':
        livro_id = int(request.form.get('livro_id'))
        data_emp_str = request.form.get('data_emprestimo')
        data_prev_str = request.form.get('data_prevista_devolucao')

        novo_emprestimo = Emprestimo(
            livro_id=livro_id,
            data_emprestimo=datetime.strptime(data_emp_str, '%Y-%m-%d') if data_emp_str else datetime.now(),
            data_devolucao=datetime.strptime(data_prev_str, '%Y-%m-%d') if data_prev_str else None,
            status=False
        )

        mensagem = EmprestimoService.registrar_emprestimo(novo_emprestimo)
        flash(mensagem, 'success' if 'sucesso' in mensagem.lower() else 'error')
        return redirect(url_for('emprestimos.listar_emprestimos'))

    emprestimos = Emprestimo.query.all()
    livros = LivroDAO.listar_livros()
    return render_template('emprestimos.html', emprestimos=emprestimos, livros=livros, usuarios=[])