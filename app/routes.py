import os
from flask import Blueprint, render_template, flash, redirect, url_for, request, current_app
from werkzeug.utils import secure_filename
from app import db
from app.forms import LoginForm, PacoteForm, ReservaForm, ProfileForm 
from app.models import User, Pacote, Cliente, Reserva, Historico
from flask_login import login_user, logout_user, current_user, login_required
from datetime import datetime

bp = Blueprint('main', __name__)

def registrar_historico(descricao):
    hist = Historico(descricao=descricao, usuario_id=current_user.id)
    db.session.add(hist)

def salvar_foto(form_foto):
    """Salva a foto de perfil de forma segura e retorna o nome do arquivo."""
    filename = secure_filename(form_foto.filename)
    caminho_completo = os.path.join(current_app.root_path, 'static/profile_pics', filename)
    os.makedirs(os.path.dirname(caminho_completo), exist_ok=True)
    form_foto.save(caminho_completo)
    return filename

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Email ou senha inválidos.', 'danger')
            return redirect(url_for('main.login'))
        login_user(user, remember=form.remember_me.data)
        flash(f'Bem-vindo, {user.nome}!', 'success')
        return redirect(url_for('main.index'))
    return render_template('login.html', title='Login', form=form)

@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.login'))

@bp.route('/')
@login_required
def index():
    total_pacotes = Pacote.query.count()
    total_reservas = Reserva.query.filter_by(status='Ativa').count()
    return render_template('index.html', title='Dashboard', total_pacotes=total_pacotes, total_reservas=total_reservas)

@bp.route('/perfil')
@login_required
def perfil():
    return render_template('perfil.html', title='Meu Perfil')

@bp.route('/perfil/editar', methods=['GET', 'POST'])
@login_required
def editar_perfil():
    form = ProfileForm()
    if form.validate_on_submit():
        if form.foto_perfil.data:
            nome_arquivo = salvar_foto(form.foto_perfil.data)
            current_user.foto_perfil = nome_arquivo
        current_user.nome = form.nome.data
        db.session.commit()
        flash('Seu perfil foi atualizado com sucesso!', 'success')
        return redirect(url_for('main.perfil'))
    elif request.method == 'GET':
        form.nome.data = current_user.nome
    
    foto_perfil_url = url_for('static', filename='profile_pics/' + (current_user.foto_perfil or 'default.png'))
    return render_template('perfil_editar.html', title='Editar Perfil', form=form, foto_perfil_url=foto_perfil_url)

@bp.route('/pacotes')
@login_required
def pacotes():
    lista_pacotes = Pacote.query.order_by(Pacote.data_inicio.asc()).all()
    return render_template('pacotes.html', title='Pacotes de Viagem', pacotes=lista_pacotes)

@bp.route('/pacote/novo', methods=['GET', 'POST'])
@login_required
def criar_pacote():
    form = PacoteForm()
    if form.validate_on_submit():
        novo_pacote = Pacote(destino=form.destino.data, data_inicio=form.data_inicio.data, data_fim=form.data_fim.data, preco=form.preco.data, vagas_total=form.vagas_total.data)
        db.session.add(novo_pacote)
        registrar_historico(f"Criou o pacote para {novo_pacote.destino}")
        db.session.commit()
        flash('Pacote criado com sucesso!', 'success')
        return redirect(url_for('main.pacotes'))
    return render_template('form_pacote.html', title='Novo Pacote', form=form, legenda='Novo Pacote')

@bp.route('/pacote/editar/<int:id>', methods=['GET', 'POST'])
@login_required
def editar_pacote(id):
    pacote = Pacote.query.get_or_404(id)
    form = PacoteForm(obj=pacote)
    if form.validate_on_submit():
        pacote.destino = form.destino.data
        pacote.data_inicio = form.data_inicio.data
        pacote.data_fim = form.data_fim.data
        pacote.preco = form.preco.data
        pacote.vagas_total = form.vagas_total.data
        registrar_historico(f"Editou o pacote {pacote.id} - {pacote.destino}")
        db.session.commit()
        flash('Pacote atualizado com sucesso!', 'success')
        return redirect(url_for('main.pacotes'))
    return render_template('form_pacote.html', title='Editar Pacote', form=form, legenda='Editar Pacote')

@bp.route('/reservas/<int:pacote_id>', methods=['GET', 'POST'])
@login_required
def gerenciar_reservas(pacote_id):
    pacote = Pacote.query.get_or_404(pacote_id)
    form = ReservaForm()
    
    if form.validate_on_submit():
        if pacote.vagas_disponiveis <= 0:
            flash('Este pacote não possui mais vagas disponíveis!', 'danger')
            return redirect(url_for('main.gerenciar_reservas', pacote_id=pacote.id))
            
        cliente = Cliente.query.filter_by(email=form.email_cliente.data).first()
        if not cliente:
            cliente = Cliente(nome=form.nome_cliente.data, email=form.email_cliente.data)
            db.session.add(cliente)
            db.session.commit()

        nova_reserva = Reserva(cliente_id=cliente.id, pacote_id=pacote.id, usuario_id=current_user.id)
        pacote.vagas_ocupadas += 1
        db.session.add(nova_reserva)
        registrar_historico(f"Criou reserva para o cliente {cliente.nome} no pacote {pacote.destino}")
        db.session.commit()
        flash('Reserva realizada com sucesso!', 'success')
        return redirect(url_for('main.gerenciar_reservas', pacote_id=pacote.id))

    reservas = Reserva.query.filter_by(pacote_id=pacote.id).order_by(Reserva.data_reserva.desc()).all()
    return render_template('reservas.html', title=f'Reservas para {pacote.destino}', pacote=pacote, reservas=reservas, form=form)

@bp.route('/reserva/cancelar/<int:reserva_id>', methods=['POST'])
@login_required
def cancelar_reserva(reserva_id):
    reserva = Reserva.query.get_or_404(reserva_id)
    if reserva.status == 'Ativa':
        reserva.status = 'Cancelada'
        reserva.pacote.vagas_ocupadas -= 1
        registrar_historico(f"Cancelou a reserva {reserva.id} do cliente {reserva.cliente.nome}")
        db.session.commit()
        flash('Reserva cancelada com sucesso.', 'success')
    else:
        flash('Esta reserva já está cancelada.', 'info')
    return redirect(url_for('main.gerenciar_reservas', pacote_id=reserva.pacote_id))