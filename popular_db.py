from app import create_app, db
from app.models import User, Pacote

app = create_app()

with app.app_context():
    print("Criando todas as tabelas do banco de dados...")
    db.create_all()
    print("Tabelas criadas.")

    if User.query.filter_by(email='admin@agencia.com').first() is None:
        print("Criando usuário administrador...")
        admin = User(nome='Administrador', email='admin@agencia.com', perfil='admin')
        admin.set_password('admin123')
        db.session.add(admin)
        print("Usuário administrador criado.")
    else:
        print("Usuário administrador já existe.")

    if Pacote.query.count() == 0:
        from datetime import date
        print("Criando pacotes de exemplo...")
        p1 = Pacote(destino='Paris, França', data_inicio=date(2025, 10, 20), data_fim=date(2025, 10, 27), preco=5500.00, vagas_total=10)
        p2 = Pacote(destino='Tóquio, Japão', data_inicio=date(2025, 11, 5), data_fim=date(2025, 11, 15), preco=8200.00, vagas_total=5)
        db.session.add(p1)
        db.session.add(p2)
        print("Pacotes de exemplo criados.")
    else:
        print("Pacotes de exemplo já existem.")

    db.session.commit()
    print("Processo finalizado com sucesso.")