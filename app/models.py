from app import db, login # Renomeado para 'login' para consistência
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime

# O user_loader deve usar a instância do LoginManager
@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    senha_hash = db.Column(db.String(128))
    perfil = db.Column(db.String(20), nullable=False, default='atendente')
    
    # --- CORREÇÃO APLICADA AQUI ---
    # Adiciona o campo para a foto de perfil com um valor padrão.
    foto_perfil = db.Column(db.String(100), nullable=False, default='default.png')

    def set_password(self, password):
        self.senha_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.senha_hash, password)

class Pacote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    destino = db.Column(db.String(150), nullable=False)
    data_inicio = db.Column(db.Date, nullable=False)
    data_fim = db.Column(db.Date, nullable=False)
    preco = db.Column(db.Float, nullable=False)
    vagas_total = db.Column(db.Integer, nullable=False)
    vagas_ocupadas = db.Column(db.Integer, default=0)
    reservas = db.relationship('Reserva', backref='pacote', lazy='dynamic')
    
    @property
    def vagas_disponiveis(self):
        return self.vagas_total - self.vagas_ocupadas

class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    telefone = db.Column(db.String(20))
    reservas = db.relationship('Reserva', backref='cliente', lazy='dynamic')

class Reserva(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data_reserva = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), nullable=False, default='Ativa')
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'), nullable=False)
    pacote_id = db.Column(db.Integer, db.ForeignKey('pacote.id'), nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) 

class Historico(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data_movimentacao = db.Column(db.DateTime, default=datetime.utcnow)
    descricao = db.Column(db.String(255), nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    usuario = db.relationship('User')