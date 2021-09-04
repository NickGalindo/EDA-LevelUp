from django.apps import AppConfig


class IncreaseLevelConfig(AppConfig):
    name = 'LevelUp.apps.increaseLevel'
    label = 'increaseLevel'
    verbose_name = 'IncreaseLevel'

default_app_config = 'LevelUp.apps.increaseLevel.IncreaseLevelConfig'
