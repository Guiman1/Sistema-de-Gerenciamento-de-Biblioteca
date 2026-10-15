from flask import Flask, render_template
from configdb import db

from blueprints.livros import livros_bp
from blueprints.emprestimos import emprestimos_bp
from blueprints.devolucoes import devolucoes_bp

app = Flask(__name__)
app.secret_key = '0600e86f9cb358d7980de6652ac9d8041f0b121f14aa2108'

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost:5432/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.register_blueprint(livros_bp)
app.register_blueprint(emprestimos_bp)
app.register_blueprint(devolucoes_bp)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('base.html')

if __name__ == '__main__':
    app.run(debug=True)