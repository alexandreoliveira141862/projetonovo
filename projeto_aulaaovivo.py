from flask import Flask, render_template

from flask_sqlalchemy import SQLAlchemy

# Variavel de aplicação:
app = Flask(__name__)

# Configurando a conexao com o banco de dados. Como se estivese criando uma URl para acesso ao BD.
app.config['SQLALCHEMY_DATABASE_URI'] = \
'{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
    SGBD = 'mysql+mysqlconnector',
    usuario = 'root',
    senha = 'admin',
    servidor = 'localhost',
    database = 'estoque'
)

# a linha abaixo instancia o banco de dados:

db = SQLAlchemy(app) 

# a classe a baixo é a classe modelo da tabela do banco de dados:
class Produto(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    nome = db.Column(db.String(50), nullable = False)
    marca = db.Column(db.String(30), nullable = True)
    preço = db.Column(db.Float, nullable = False)

def __repr__(self):
    return '<Name %r>' % self.name #leitura campo por campo

# Criando uma rota:
@app.route('/live2')
def live():
    return "Bem vindo a nossa 2ª Live de Python! Com Daniel"

@app.route('/Lista')

def lista_produtos():

    lista_prod = Produto.query.order_by(Produto.id)

    return render_template("produtos.html", titulo = "Unifecaf", descricao = "Seu sonho, nossa meta!", 
                           produtos = lista_prod)

# Mantém a aplicação rodando:
app.run(debug=True) # obs: esta deve ser a ultima linha da aplicação.
