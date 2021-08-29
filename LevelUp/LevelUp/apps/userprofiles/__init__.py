from django.apps import AppConfig


class UserprofilesConfig(AppConfig):
    name = 'LevelUp.apps.userprofiles'
    label = 'userprofiles'
    verbose_name = 'UserProfiles'

default_app_config = 'LevelUp.appd.userprofiles.UserprofilesConfig'
