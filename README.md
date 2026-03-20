# 🚀 Task Manager API

API RESTful para gerenciamento de tarefas com autenticação de usuários, desenvolvida com foco em boas práticas de backend e pronta para uso em portfólio profissional.

---

## 📷 Preview da API

![Swagger UI](docs.png)

> Interface interativa gerada automaticamente pelo FastAPI

---

## 📌 Sobre o Projeto

O **Task Manager API** é um sistema backend que permite:

* Cadastro de usuários
* Autenticação via token (JWT)
* Gerenciamento de tarefas (CRUD)
* Associação de tarefas a usuários

Este projeto foi desenvolvido com foco em:

* Estrutura profissional de backend
* Separação de responsabilidades (routers, schemas, crud)
* Boas práticas com FastAPI
* Preparação para ambiente real de produção

---

## 🛠️ Tecnologias Utilizadas

* Python 3.13
* FastAPI
* SQLAlchemy
* Pydantic v2
* SQLite (desenvolvimento)
* Poetry (gerenciamento de dependências)
* Uvicorn

---

## 📁 Estrutura do Projeto

```
app/
├── crud/
├── models/
├── routers/
├── schemas/
├── core/
├── database/
└── main.py
```

---

## 🔐 Autenticação

A autenticação é feita via **JWT (JSON Web Token)**.

Fluxo:

1. Usuário se registra
2. Faz login
3. Recebe um token
4. Usa o token para acessar rotas protegidas

---

## 📌 Funcionalidades

### 👤 Usuários

* [x] Registro de usuário
* [x] Login
* [x] Obter usuário autenticado (`/me`)

### ✅ Tarefas

* [x] Criar tarefa
* [x] Listar tarefas do usuário
* [x] Atualizar tarefa
* [x] Deletar tarefa

---

## ▶️ Como rodar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/RobertoJr98/task-manager-api.git
cd task-manager-api
```

---

### 2. Instale as dependências

```bash
poetry install
```

---

### 3. Ative o ambiente

```bash
poetry shell
```

---

### 4. Execute a aplicação

```bash
poetry run uvicorn app.main:app --reload
```

---

## 📍 Acesse a documentação

* Swagger UI: http://127.0.0.1:8000/docs
* Redoc: http://127.0.0.1:8000/redoc

---

## 🧠 Boas práticas aplicadas

* Arquitetura modular
* Separação em camadas (Router, Service/CRUD, Schema)
* Validação de dados com Pydantic
* Uso de dependências com FastAPI
* Código organizado e escalável

---

## 🚧 Próximas melhorias

* [ ] Deploy em produção (Render / Railway)
* [ ] Dockerização
* [ ] Banco PostgreSQL
* [ ] Testes automatizados (Pytest)
* [ ] Refresh Token
* [ ] Permissões e roles

---

## 👨‍💻 Autor

**Roberto Barboza da Silva Junior**
🔗 https://github.com/RobertoJr98

---

## 📄 Licença

Este projeto está sob a licença MIT.
