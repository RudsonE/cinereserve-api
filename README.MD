# 🎬 CineReserve API

API RESTful desenvolvida para gerenciamento de reservas de cinema, permitindo que usuários visualizem filmes, sessões, assentos disponíveis e realizem reservas de forma segura.

---

## 🚀 Tecnologias utilizadas

* Python 3
* Django
* Django REST Framework
* JWT Authentication
* PostgreSQL (ou SQLite para desenvolvimento)
* Poetry
* Docker

---

## ⚙️ Como rodar o projeto

### 1. Clonar repositório

```bash
git clone https://github.com/RudsonE/cinereserve-api.git
cd cinereserve
```

---

### 2. Instalar dependências

```bash
poetry install
```

---

### 3. Ativar ambiente

```bash
poetry env activate
```

ou

```bash
poetry run python
```

---

### 4. Rodar migrações

```bash
poetry run python manage.py migrate
```

---

### 5. Criar super usuário

```bash
poetry run python manage.py createsuperuser
```

---

### 6. Rodar servidor

```bash
poetry run python manage.py runserver
```

---

## 🔐 Autenticação

A API utiliza autenticação via JWT.

### Login

```http
POST /login
```

Body:

```json
{
  "username": "seu_usuario",
  "password": "sua_senha"
}
```

Resposta:

```json
{
  "access": "token_jwt"
}
```

---

## 📌 Endpoints

### 🎬 Filmes

* `GET /movies/` → lista todos os filmes
* `GET /movies/{id}/` → detalhes de um filme

---

### 🎥 Sessões

* `GET /movies/{movie_id}/sessions/` → lista sessões de um filme

---

### 💺 Assentos

* `GET /sessions/{id}/seats/` → mapa de assentos

---

### 🎟 Reservas

* `POST /sessions/{id}/reserve/` → reservar assento

---

### 👤 Usuário

* `POST /login/` → autenticação

---

## 🧠 Regras de negócio

* Um assento pode estar:

  * available
  * reserved
  * purchased

* Reservas são associadas a:

  * usuário
  * sessão
  * assento

---

## 📄 Estrutura do projeto

```
cinereserve/
 ├── movies/
 ├── showtimes/
 ├── reservations/
 ├── cinereserve/
 ├── manage.py
 ├── pyproject.toml
```

---

## 🐳 Docker (opcional)

```bash
docker-compose up --build
```

---

## 🧪 Testes

```bash
poetry run python manage.py test
```

---

## 📌 Observações

* Projeto desenvolvido como desafio técnico backend da b2bit
* Foco em arquitetura, organização e boas práticas REST

---

## 👨‍💻 Autor

Rudson Emanoel
