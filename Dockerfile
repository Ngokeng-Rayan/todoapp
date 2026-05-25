# Étape 1 : Build (Builder Stage)
FROM python:3.10-slim AS builder

WORKDIR /app

# Définition des variables d'environnement
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Installation des dépendances système nécessaires pour certaines librairies Python
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copie et installation des dépendances Python
COPY requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/app/wheels -r requirements.txt


# Étape 2 : Production (Final Stage)
FROM python:3.10-slim

# Création d'un utilisateur non-root pour des raisons de sécurité (Exigence DevOps)
RUN addgroup --system appgroup && adduser --system --group appuser

WORKDIR /app

# Variables d'environnement pour la production
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Installation des dépendances système nécessaires à l'exécution (sans les outils de build)
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copie des wheels compilés depuis le builder et installation
COPY --from=builder /usr/src/app/wheels /wheels
COPY --from=builder /app/requirements.txt .
RUN pip install --no-cache /wheels/*

# Copie du code source de l'application
COPY . .

# Transfert de la propriété des fichiers à l'utilisateur non-root
RUN chown -R appuser:appgroup /app

# Passage sous l'utilisateur non-root
USER appuser

# Exposition du port
EXPOSE 8000

# Commande par défaut (utilisée si on lance le conteneur, mais non utilisée sur o2switch FTP)
CMD ["gunicorn", "core.wsgi:application", "--bind", "0.0.0.0:8000"]
