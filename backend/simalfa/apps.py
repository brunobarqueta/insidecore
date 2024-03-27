from django.apps import AppConfig

class SimalfaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'simalfa'
    
    def ready(self):
        import simalfa.signals
