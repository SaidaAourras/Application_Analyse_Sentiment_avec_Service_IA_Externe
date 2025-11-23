# 🚀 Backend – API d’Analyse de Sentiment (FastAPI)

![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)

---

## 🧠 Description du Backend

Ce backend est une API REST développée avec **FastAPI**.  
Il permet :

- d’analyser le **sentiment d’un texte**
- d’utiliser un modèle **Hugging Face** externe
- de gérer l'authentification via **JWT**
- de stocker les utilisateurs et les analyses dans une **base PostgreSQL**

Le backend est totalement **conteneurisé avec Docker**, ce qui permet une installation simple et portable.

---

## 📦 Fonctionnalités Principales

- Analyse de sentiment via Hugging Face  
- Authentification JWT (login + token)  
- Gestion des utilisateurs  
- Sauvegarde des analyses dans PostgreSQL  
- Documentation automatique Swagger  
- Version Docker prête pour production  

Documentation Swagger :  
👉 [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 📂 Structure du Backend

    Application_Analyse_Sentiment_avec_Service_IA_Externe/
    │
    ├── app/
    ├── main.py # Point d’entrée FastAPI , Endpoints organisés
    ├── auth.py # Login + JWT
    ├── models.py # Tables SQLAlchemy
    ├── database.py # Connexion PostgreSQL
    ├── inference_providers.py # Appels Hugging Face API
    ├── test_unitaires.py
    ├── requirements.txt
    ├── Dockerfile
    ├── .env.example
    └── README.md


---

## ⚙️ Installation Locale (Développeurs)

```bash
git clone https://github.com/SaidaAourras/Application_Analyse_Sentiment_avec_Service_IA_Externe.git
cd Application_Analyse_Sentiment_avec_Service_IA_Externe

python -m venv venv
source venv/bin/activate     # Windows: venv\Scripts\activate

pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

API disponible sur :
👉 http://localhost:8000

---

## 🔐 Configuration (.env)

Fichier .env recommandé :

    # JWT
    SECRET_KEY=votre_cle_secrete
    ALGORITHM=HS256

    # Hugging Face
    HUGGINGFACE_API_KEY=hf_votre_cle_api
    HF_TOKEN=hf_votre_cle_api

    # Base de données PostgreSQL
    DATABASE_URL=postgresql://user:password@postgres:5432/sentimentdb

- Dans Docker, le host doit être postgres
- En local, vous pouvez utiliser localhost

## 🐳 Exécution avec Docker

### 1 - Construire l’image 

    docker build -t sentiment-backend .

### 2 - Lancer le conteneur (Docker seul)

    docker run -d \
        --name backend \
        -p 8000:8000 \
        --env-file .env \
        sentiment-backend

### 3 - Lancer avec PostgreSQL et un réseau Docker

    docker network create monreseau

- PostgreSQL :

        docker run -d \
        --name postgres \
        --network monreseau \
        -e POSTGRES_USER=user \
        -e POSTGRES_PASSWORD=password \
        -e POSTGRES_DB=sentimentdb \
        postgres:15

- Backend :

        docker run -d \
        --name backend \
        --network monreseau \
        -p 8000:8000 \
        --env-file .env \
        sentiment-backend
  
- Accéder à la base de données PostgreSQL
  
      # Lancer une session psql dans le conteneur postgres
      docker exec -it <name_container_postgres> psql -U POSTGRES_USER -d POSTGRES_DB
  
  Une fois connecté, tu peux exécuter des commandes SQL classiques :
  
  ``` bash
        -- Lister les tables
        \dt
        
        -- Voir les données d'une table
        SELECT * FROM users;
        
        -- Quitter psql
        \q
  ```

## 📡 Endpoints Principaux

#### 🔑 POST /login

Authentification utilisateur

- Request :

        {"username": "admin", "password": "password123"}

- Response :

        {"access_token": "eyJhb...", "token_type": "bearer"}

#### 🧠 POST /sentiment (protégé JWT)

- Headers :

        Authorization: Bearer <token>


- Body :

        {"text": "C’est un excellent produit !"}


- Response :

        {
        "text": "C’est un excellent produit !",
        "score": 5
        }

## 🧪 Tests

    pytest -v 

---

## 👩‍💻 **AOURRAS Saida**







