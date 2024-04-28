from django.apps import AppConfig
# from django.db.models.signals import post_save


class MyProfileConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'my_profile'
    
    def ready(self):
        import my_profile.signals
