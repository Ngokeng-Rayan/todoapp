import os
import sys

# Ajouter le répertoire de base au chemin Python
sys.path.insert(0, os.path.dirname(__file__))

# Importer l'application WSGI configurée par Django
from core.wsgi import application
