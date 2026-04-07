# 🚀 Task Manager API

API RESTful para gerenciamento de tarefas com autenticação de usuários, desenvolvida com foco em boas práticas de backend e pronta para uso em produção.

---

## 🌐 Deploy

🔗 https://task-manager-api-7o0u.onrender.com  

📄 Documentação interativa (Swagger):  
👉 https://task-manager-api-7o0u.onrender.com/docs  

---

## 📷 Preview da API

![Swagger UI](docs.png)

---

## ⚙️ Tecnologias

- Python
- FastAPI
- SQLAlchemy
- PostgreSQL
- Alembic (migrations)
- JWT Authentication
- Render (deploy)

---

## 🔐 Funcionalidades

- Cadastro de usuário
- Login com autenticação JWT
- Endpoint protegido (`/auth/me`)
- CRUD completo de tarefas
- Relacionamento usuário ↔ tarefas
- Proteção de rotas com autenticação
- Validação de dados com Pydantic

---

## 📌 Endpoints principais

### 🔑 Auth

- `POST /auth/register` → Criar usuário  
- `POST /auth/login` → Login e geração de token  
- `GET /auth/me` → Usuário autenticado  

### ✅ Tasks (protegido)

- `POST /tasks` → Criar tarefa  
- `GET /tasks` → Listar tarefas do usuário  
- `PUT /tasks/{id}` → Atualizar tarefa  
- `DELETE /tasks/{id}` → Deletar tarefa  

---

## 🔒 Autenticação

A API utiliza JWT (JSON Web Token).

### Passos:

1. Faça login em `/auth/login`
2. Copie o token retornado
3. Clique em **Authorize** no Swagger
4. Use o formato:

```
Bearer SEU_TOKEN
```

---

## 🛠️ Como rodar o projeto

```bash
# Clonar repositório
git clone https://github.com/RobertoJr98/task-manager-api.git

# Entrar na pasta
cd task-manager-api

# Instalar dependências
poetry install

# Rodar aplicação
poetry run uvicorn app.main:app --reload
```

---

## ⚙️ Variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
DATABASE_URL=postgresql+psycopg2://user:password@localhost:5432/db_name
SECRET_KEY=sua_chave_secreta
DEBUG=True
```

---

## 📦 Banco de dados

- PostgreSQL
- Migrations com Alembic

```bash
alembic upgrade head
```

---

## 🧪 Testes (em desenvolvimento)

```bash
pytest
```

---

## 📈 Melhorias futuras

- Testes automatizados completos
- Dockerização
- CI/CD
- Paginação de tarefas
- Refresh Token
- Rate limiting

---

## 👨‍💻 Autor

**Roberto Barboza da Silva Junior**

- GitHub: https://github.com/RobertoJr98

---

## 💡 Sobre o projeto

Este projeto foi desenvolvido com foco em prática real de backend, aplicando conceitos como:

- Arquitetura em camadas (routers, services, models)
- Autenticação segura com JWT
- Integração com banco de dados relacional
- Deploy em ambiente cloud (Render)
