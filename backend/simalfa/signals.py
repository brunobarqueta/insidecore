from django.db.models.signals import post_migrate
from django.dispatch import receiver
from simalfa.models.tenant import Tenant

@receiver(post_migrate)
def criar_tenant_default(sender, **kwargs):
    if kwargs.get('app_config').name == 'simalfa':
        if not Tenant.objects.exists():
            Tenant.objects.create(code='1', name='Rocha Terminais Portuários e Logística', guid = '9539aec6-1102-4658-8e82-ab5cec5c4f7b')