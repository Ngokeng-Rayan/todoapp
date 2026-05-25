import os
import sys

# Ajouter le répertoire de base au chemin Python
sys.path.insert(0, os.path.dirname(__file__))

# Définir le module de configuration Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

# Importer l'application WSGI de Django
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
