from django.apps import AppConfig


class TrialsConfig(AppConfig):
    name = 'LevelUp.apps.trials'
    label = 'trials'
    verbose_name = 'Trials'

default_app_config = 'LevelUp.apps.trials.TrialsConfig'
