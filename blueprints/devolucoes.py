from flask import Blueprint, render_template, redirect, url_for, flash
from datetime import date
from modelos.emprestimo import Emprestimo
from services.emprestimo_service import EmprestimoService

devolucoes_bp = Blueprint('devolucoes', __name__)


@devolucoes_bp.route('/devolucoes', methods=['GET'])
def listar_devolucoes():
    emprestimos_pendentes = Emprestimo.query.filter_by(status=False).all()
    return render_template('devolucoes.html', emprestimos=emprestimos_pendentes, hoje=date.today())


@devolucoes_bp.route('/devolucoes/registrar/<int:id>', methods=['POST'])
def registrar_devolucao(id):
    emprestimo_obj = Emprestimo()
    emprestimo_obj.id = id

    mensagem = EmprestimoService.registrar_devolucao(emprestimo_obj)
    flash(mensagem, 'success' if 'devolvido' in mensagem.lower() else 'error')
    return redirect(url_for('devolucoes.listar_devolucoes'))