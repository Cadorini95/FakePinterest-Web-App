from flask            import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login      import LoginManager
from flask_bcrypt     import Bcrypt

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]  = "sqlite:///comunidade.db"
app.config["SECRET_KEY"]               = "06b5005512f8189cb4b6d4684da46f73"         ## SENHA CRIPTOGRADA DE CONFIGURAÇÃO DA APLICAÇÃO
app.config["UPLOAD_FOLDER"]            = "static/fotos_posts"                       ## CONFIGURAÇÃO DA PASTA PADRÃO PARA UPLOAD DE FOTOS

database      = SQLAlchemy(app)
bcrypt        = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "homepage" 

from fakepinterest import routes