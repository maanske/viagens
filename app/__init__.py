from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# Instanciando as extensões
db = SQLAlchemy()
migrate = Migrate()
# CORREÇÃO: A variável agora se chama 'login' para corresponder ao import no models.py
login = LoginManager() 
login.login_view = 'main.login'
login.login_message = 'Por favor, faça login para acessar esta página.'
login.login_message_category = 'info'

def create_app(config_class=Config):
    """Cria e configura a instância da aplicação Flask."""
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Inicializa as extensões com a aplicação
    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)

    # Importa os blueprints e modelos DENTRO da função para evitar importação circular
    from app.routes import bp as main_blueprint
    app.register_blueprint(main_blueprint)

    # Garante que os modelos sejam reconhecidos pela aplicação
    from app import models

    return app