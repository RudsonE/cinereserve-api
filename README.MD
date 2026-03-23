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
* Swagger (drf-yasg)

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
POST /login/
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
  "refresh": "refresh_token",
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

* `GET /movies/{movie_id}/sessions/{session_id}/seats/` → mapa de assentos

---

### 🎟 Reservas

* `POST /movies/{movie_id}/sessions/{session_id}/reserve/` → reservar assento (requer JWT)

---

### 🎫 Meus Tickets

* `GET /movies/{movie_id}/sessions/my-tickets/` → lista os tickets do usuário autenticado

---

### 👤 Usuário

* `POST /login/` → autenticação

---

## 📚 Documentação da API

A documentação interativa está disponível via Swagger:

```
http://localhost:8000/swagger/
```

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

* Não é possível reservar o mesmo assento duas vezes

* Apenas usuários autenticados podem realizar reservas

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

## 💽 Banco de Dados

O projeto utiliza SQLite por padrão para facilitar a execução local.

A utilização de PostgreSQL pode ser configurada para ambientes de produção.

---

## 📌 Observações

* Projeto desenvolvido como desafio técnico backend da b2bit
* Foco em arquitetura, organização e boas práticas REST

---

## 👨‍💻 Autor

Rudson Emanoel