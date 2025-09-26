from app import create_app, db
from app.models import User, Pacote
from datetime import date

app = create_app()

def popular_banco():
    """Cria tabelas e popula com dados iniciais se estiverem vazias."""
    print("Iniciando processo de população do banco de dados...")
    
    db.create_all()
    print("Verificação de tabelas concluída.")

    if not User.query.filter_by(email='admin@agencia.com').first():
        print("Criando usuário administrador...")
        admin = User(nome='Administrador', email='admin@agencia.com', perfil='admin')
        admin.set_password('admin123')
        db.session.add(admin)
        print("Usuário administrador criado.")
    else:
        print("Usuário administrador já existe.")

    if Pacote.query.count() == 0:
        print("Criando pacotes de exemplo...")
        pacotes = [
            Pacote(destino='Paris, França', data_inicio=date(2025, 10, 20), data_fim=date(2025, 10, 27), preco=5500.00, vagas_total=10),
            Pacote(destino='Tóquio, Japão', data_inicio=date(2025, 11, 5), data_fim=date(2025, 11, 15), preco=8200.00, vagas_total=5),
            Pacote(destino='Fernando de Noronha, Brasil', data_inicio=date(2026, 1, 10), data_fim=date(2026, 1, 17), preco=4800.00, vagas_total=15)
        ]
        db.session.add_all(pacotes)
        print(f"{len(pacotes)} pacotes de exemplo criados.")
    else:
        print("Pacotes de exemplo já existem.")

    db.session.commit()
    print("\nProcesso finalizado com sucesso!")

if __name__ == '__main__':
    with app.app_context():
        popular_banco()