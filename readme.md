# 🌍 Sistema de Gestão de Agência de Viagens

![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.2.2-black.svg)
![Database](https://img.shields.io/badge/Database-SQLite-blue.svg)
![Frontend](https://img.shields.io/badge/Frontend-Bootstrap%205-purple.svg)

Este projeto é um sistema web desenvolvido como solução para o desafio de avaliação da disciplina de Educação Profissional.  
O sistema simula uma plataforma para uma agência de viagens gerenciar seus pacotes turísticos e reservas de clientes, substituindo um processo manual e propenso a erros.

---

## 📌 Contextualização do Problema

Uma agência de viagens local enfrenta grandes desafios na gestão de pacotes turísticos e reservas de clientes devido à ausência de um sistema informatizado.  
O controle manual gera problemas como **overbooking**, dificuldade no acompanhamento de cancelamentos e falhas de comunicação.  

A diversidade de produtos (passagens, hospedagens, pacotes) aumenta a complexidade, tornando essencial uma solução tecnológica para garantir **agilidade, organização e redução de erros operacionais**.

---

## ✨ Funcionalidades Principais

- **🔐 Autenticação de Usuários:** Login seguro com diferenciação de perfis (Administrador e Atendente).  
- **✈️ Gestão de Pacotes de Viagem:** CRUD completo com informações detalhadas (destino, período, preço, vagas, etc.).  
- **🎟️ Gestão de Reservas:** Registro e cancelamento de reservas de clientes.  
- **📊 Controle de Vagas:** Validação automática contra overbooking, com alertas para pacotes com poucas vagas ou esgotados.  
- **📋 Histórico de Operações:** Registro das principais ações (usuário, ação e data).  
- **👨‍💼 Gestão de Clientes:** Cadastro simplificado no momento da reserva.  

---

## 🛠️ Tecnologias Utilizadas

- **Backend**
  - Python 3
  - Flask
  - Flask-SQLAlchemy
  - Flask-Login
  - Flask-WTF
  - Werkzeug

- **Frontend**
  - HTML5
  - Bootstrap 5

- **Banco de Dados**
  - SQLite  

---

## 📁 Estrutura do Projeto

```text
agencia_viagens/
├── app/
│   ├── __init__.py      # Inicializador da aplicação Flask e Blueprints
│   ├── models.py        # Modelos do banco de dados (ORM)
│   ├── routes.py        # Definição das rotas e lógica das views
│   ├── forms.py         # Classes de formulários (Flask-WTF)
│   ├── templates/       # Arquivos HTML (Jinja2)
│   └── static/          # Arquivos estáticos (CSS, JS, Imagens)
├── venv/                # Ambiente virtual do Python
├── run.py               # Ponto de entrada para executar a aplicação
├── config.py            # Configurações da aplicação (chaves, URI do DB)
├── requirements.txt     # Lista de dependências Python
├── popular_db.py        # Script para criar e popular o banco de dados
└── agencia.db           # Arquivo do banco de dados SQLite
```
---
## 🚀 Guia de Instalação e Execução
Siga os passos abaixo para configurar e executar o projeto em seu ambiente local.
- **1. Pré-requisitos**
    - Python 3.8+
    - Git

- **2. Clone o Repositório**
    - git clone <URL_DO_SEU_REPOSITORIO>
    - cd agencia_viagens

- **3. Crie e Ative o Ambiente Virtual**
- Windows:
    - python -m venv venv
    - .\venv\Scripts\activate

- macOS / Linux:   
    - python3 -m venv venv
    - source venv/bin/activate

- **4. Instale as Dependências**
    - pip install -r requirements.txt

- **5. Crie e Popule o Banco de Dados**
    - python popular_db.py

- **6. Execute a Aplicação**
    - flask run

- **7. Acesse o Sistema**
    - Abra o navegador e acesse: *http://127.0.0.1:5000*

- **🔑 Credenciais de Acesso (Admin)**

- **Email:** *admin@agencia.com*

- **Senha:** *admin123*