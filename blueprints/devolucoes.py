from flask import Blueprint, render_template, redirect, url_for, flash
from datetime import datetime
from modelos.emprestimo import Emprestimo
from services.emprestimo_service import EmprestimoService
from reposit.emprestimoDAO import EmprestimoDAO

devolucoes_bp = Blueprint('devolucoes', __name__)

@devolucoes_bp.route('/devolucoes')
def listar_devolucoes():
    emprestimos = Emprestimo.query.filter_by(status=False).all()
    hoje = datetime.now().date()
    return render_template('devolucoes.html', emprestimos=emprestimos, hoje=hoje)

@devolucoes_bp.route('/devolucoes/registrar/<int:id>', methods=['POST'])
def registrar_devolucao(id):
    emprestimo = EmprestimoDAO.buscar_emprestimo_id(id)

    if emprestimo is None:
        flash('Empréstimo não encontrado.', 'erro')
        return redirect(url_for('devolucoes.listar_devolucoes'))

    mensagem = EmprestimoService.registrar_devolucao(emprestimo)
    flash(mensagem, 'sucesso' if 'sucesso' in mensagem.lower() else 'erro')
    return redirect(url_for('devolucoes.listar_devolucoes'))