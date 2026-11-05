from flask import Blueprint, render_template, request, redirect, url_for, session, flash

login_bp = Blueprint('login', __name__)

EMAIL = 'admin@gmail.com'
SENHA = 'admin'

@login_bp.before_app_request
def exigir_login():
    if request.blueprint == 'login' or request.endpoint == 'static':
        return
    if not session.get('logado'):
        return redirect(url_for('login.entrar'))

@login_bp.route('/login',methods=['GET','POST'])
def entrar():
    if request.method == 'POST':
        if request.form['email'] == EMAIL and request.form['senha'] == SENHA:
            session['logado'] = True
            return redirect(url_for('index'))
        flash('Email ou senha inválidos.', 'error')
    return render_template('login.html')

@login_bp.route('/logout')
def sair():
    session.clear()
    return redirect(url_for('login.entrar'))