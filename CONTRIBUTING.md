# Guide de Contribution - Kaba-Delivery (To-Do App)

Merci de contribuer à ce projet ! Ce document définit les règles de développement et de gestion du versioning pour notre équipe, conformément aux exigences de l'entreprise AFRIQ-LOGISTIX.

## 1. Stratégie de Branches (Gitflow simplifié)
- **`main`** : La branche de production. Elle doit toujours être stable et déployable.
- **`develop`** : La branche d'intégration. Toutes les nouvelles fonctionnalités y sont fusionnées en premier.
- **`feature/*`** : Les branches de fonctionnalités (ex: `feature/api-delivery`). Elles doivent être créées à partir de `develop`.
- **`hotfix/*`** : Les branches de correction de bugs critiques. Créées à partir de `main` et fusionnées dans `main` et `develop`.

## 2. Processus de Pull Request (Merge Request)
- Les Push forcés (`--force`) sur `main` et `develop` sont **strictement interdits**.
- Tout code doit passer par une Pull Request (PR) pour être fusionné dans `main` ou `develop`.
- Une PR doit obligatoirement :
  - Passer tous les tests automatisés du pipeline CI/CD (Lint, Tests unitaires, SonarQube).
  - Être approuvée par au moins un autre développeur de l'équipe (Code Review).

## 3. Convention de Nommage des Commits (Conventional Commits)
Afin d'automatiser la génération de changelogs et de clarifier l'historique, nous utilisons la convention *Conventional Commits*. Chaque message de commit doit être structuré ainsi :

`<type>[optional scope]: <description>`

**Types autorisés :**
- `feat`: Une nouvelle fonctionnalité.
- `fix`: Une correction de bug.
- `docs`: Une modification de la documentation.
- `style`: Changements qui n'affectent pas la logique (espaces, formatage, etc.).
- `refactor`: Une modification du code qui n'ajoute ni fonctionnalité ni correction de bug.
- `test`: Ajout ou correction de tests.
- `chore`: Tâches de maintenance (ex: mise à jour des dépendances).

**Exemple :** `feat(api): ajouter la validation du JWT pour la route delivery`

## 4. Tests Locaux
Avant toute soumission de PR, assurez-vous que les tests locaux passent avec la commande :
```bash
python manage.py test
```
