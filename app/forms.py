from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import (StringField, PasswordField, BooleanField, SubmitField, 
                     IntegerField, FloatField, DateField)
from wtforms.validators import DataRequired, Email, Length, NumberRange
from app.models import User

# Formulário de Login
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Senha', validators=[DataRequired()])
    remember_me = BooleanField('Lembrar-me')
    submit = SubmitField('Entrar')

# Formulário para Pacotes de Viagem
class PacoteForm(FlaskForm):
    destino = StringField('Destino', validators=[DataRequired()])
    data_inicio = DateField('Data de Início', format='%Y-%m-%d', validators=[DataRequired()])
    data_fim = DateField('Data de Fim', format='%Y-%m-%d', validators=[DataRequired()])
    preco = FloatField('Preço', validators=[DataRequired(), NumberRange(min=0)])
    vagas_total = IntegerField('Total de Vagas', validators=[DataRequired(), NumberRange(min=1)])
    submit = SubmitField('Salvar Pacote')

# Formulário para Reservas
class ReservaForm(FlaskForm):
    nome_cliente = StringField('Nome do Cliente', validators=[DataRequired()])
    email_cliente = StringField('Email do Cliente', validators=[DataRequired(), Email()])
    submit = SubmitField('Confirmar Reserva')

# Formulário para Edição de Perfil
class ProfileForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired(), Length(min=2, max=100)])
    foto_perfil = FileField('Atualizar Foto de Perfil', validators=[FileAllowed(['jpg', 'jpeg', 'png', 'gif'], 'Apenas imagens são permitidas!')])
    submit = SubmitField('Salvar Alterações')