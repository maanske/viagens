# Sistema de Gestão de Agência de Viagens

![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.2.2-black.svg)
![Database](https://img.shields.io/badge/Database-SQLite-blue.svg)
![Frontend](https://img.shields.io/badge/Frontend-Bootstrap%205-purple.svg)

Este projeto é um sistema web desenvolvido como solução para o desafio de avaliação da disciplina de Educação Profissional. O sistema simula uma plataforma para uma agência de viagens gerenciar seus pacotes turísticos e reservas de clientes, substituindo um processo manual e propenso a erros.

---

## CONTEXTUALIZAÇÃO DO PROBLEMA

Uma agência de viagens local enfrenta grandes desafios na gestão de pacotes turísticos e reservas de clientes devido à ausência de um sistema informatizado. O controle manual gera problemas como overbooking, dificuldade no acompanhamento de cancelamentos e falhas de comunicação. A diversidade de produtos (passagens, hospedagens, pacotes) aumenta a complexidade, tornando essencial uma solução tecnológica para garantir agilidade, organização e redução de erros operacionais.

## ✨ FUNCIONALIDADES PRINCIPAIS

- **🔐 Autenticação de Usuários:** Sistema de login seguro com diferenciação de perfis (Administrador e Atendente).
- **✈️ Gestão de Pacotes de Viagem:** Interface para Criar, Ler, Atualizar e Excluir (CRUD) pacotes de viagem com informações detalhadas (destino, período, preço, vagas, etc.).
- **🎟️ Gestão de Reservas:** Funcionalidade para registrar novas reservas para clientes e realizar o cancelamento das mesmas.
- **📊 Controle de Vagas:** Validação automática que impede overbooking, emitindo alertas visuais para pacotes com poucas vagas ou esgotados.
- **📋 Histórico de Operações:** Rastreabilidade completa das ações mais importantes, registrando o responsável, a ação e a data da movimentação.
- **👨‍💼 Gestão de Clientes:** Cadastro simplificado de clientes no momento da reserva.

## 🛠️ TECNOLOGIAS UTILIZADAS

O projeto foi construído com as seguintes tecnologias:

- **Backend:**
  - **Python 3:** Linguagem de programação principal.
  - **Flask:** Microframework web para a construção da aplicação.
  - **Flask-SQLAlchemy:** ORM para interação com o banco de dados.
  - **Flask-Login:** Gerenciamento de sessões de usuário e autenticação.
  - **Flask-WTF:** Criação e validação de formulários seguros.
  - **Werkzeug:** Ferramentas essenciais para aplicações WSGI (usado para hashing de senhas).
- **Frontend:**
  - **HTML5:** Linguagem de marcação para a estrutura das páginas.
  - **Bootstrap 5:** Framework CSS para estilização e responsividade.
- **Banco de Dados:**
  - **SQLite:** Banco de dados relacional embarcado, ideal para desenvolvimento e projetos de pequeno porte.

## 📁 ESTRUTURA DO PROJETO