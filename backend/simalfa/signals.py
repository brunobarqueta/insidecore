from django.db.models.signals import post_migrate
from django.dispatch import receiver
from backend.settings import DEBUG
from simalfa.models.tenant import Tenant
from simalfa.models.metrics import Metrics
from simalfa.models.formula import Formula

@receiver(post_migrate)
def create_defaults(sender, **kwargs):
    if kwargs.get('app_config').name == 'simalfa':
        if not Tenant.objects.exists():
            Tenant.objects.create(code='1', name='Rocha Terminais Portuários e Logística', guid = '9539aec6-1102-4658-8e82-ab5cec5c4f7b')
    
    if DEBUG:
        if not Metrics.objects.exists():
            Metrics.objects.create(description='valor_cif', type='str', service='mock metrics srv')
            Metrics.objects.create(description='numero dias', type='str', service='mock metrics srv')
            Metrics.objects.create(description='taxa serviço', type='str', service='mock metrics srv')
            
        if not Formula.objects.exists():
            Formula.objects.create(description='mock formula_fcl desc', expression='não sei mock fcl')
            Formula.objects.create(description='mock formula_lcl desc', expression='não sei mock lcl')
        