from django.apps import AppConfig

class AuthenticationConfig(AppConfig):
    name = 'LevelUp.apps.authentication'
    label = 'authentication'
    verbose_name = 'Authentication'

default_app_config = 'LevelUp.apps.authentication.AuthenticationConfig'
