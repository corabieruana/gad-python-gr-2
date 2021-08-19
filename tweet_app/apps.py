
#fisierul de configurare a aplciatiei. numele clasei va trebui pus in settings.py

from django.apps import AppConfig


class TweetAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tweet_app'
