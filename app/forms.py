from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, FloatField, DateField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError, NumberRange
from app.models import User

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Senha', validators=[DataRequired()])
    remember_me = BooleanField('Lembrar-me')
    submit = SubmitField('Entrar')

class PacoteForm(FlaskForm):
    destino = StringField('Destino', validators=[DataRequired()])
    data_inicio = DateField('Data de Início', format='%Y-%m-%d', validators=[DataRequired()])
    data_fim = DateField('Data de Fim', format='%Y-%m-%d', validators=[DataRequired()])
    preco = FloatField('Preço', validators=[DataRequired(), NumberRange(min=0)])
    vagas_total = IntegerField('Total de Vagas', validators=[DataRequired(), NumberRange(min=1)])
    submit = SubmitField('Salvar Pacote')

class ReservaForm(FlaskForm):
    nome_cliente = StringField('Nome do Cliente', validators=[DataRequired()])
    email_cliente = StringField('Email do Cliente', validators=[DataRequired(), Email()])
    submit = SubmitField('Confirmar Reserva')