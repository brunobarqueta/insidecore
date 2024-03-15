from django.db.models.signals import post_migrate
from django.dispatch import receiver
from backend.settings import DEBUG
from simalfa.models.tenant import Tenant
from simalfa.models.metrics import Metrics
from simalfa.models.formula import Formula
from django.db import transaction

@receiver(post_migrate)
def create_defaults(sender, **kwargs):
    with transaction.atomic():
        if kwargs.get('app_config').name == 'simalfa':
            if not Tenant.objects.exists():
                tenant = Tenant.objects.create(code='1', name='Rocha Terminais Portuários e Logística', guid = '9539aec6-1102-4658-8e82-ab5cec5c4f7b')
            else:
                tenant = Tenant.objects.first()
    
            if DEBUG:
                if not Metrics.objects.exists():
                    metric_cif = Metrics.objects.create(description='valor_cif', type='str', service='mock metrics srv')
                    metric_cif.tenants.set([tenant])
                    metric_nd = Metrics.objects.create(description='numero dias', type='str', service='mock metrics srv')
                    metric_nd.tenants.set([tenant])
                    metric_ts = Metrics.objects.create(description='taxa serviço', type='str', service='mock metrics srv')
                    metric_ts.tenants.set([tenant])
    
                if not Formula.objects.exists():
                    formula_fcl = Formula.objects.create(description='mock formula_fcl desc', expression='não sei mock fcl')
                    formula_fcl.tenants.set([tenant])
                    formula_lcl = Formula.objects.create(description='mock formula_lcl desc', expression='não sei mock lcl')
                    formula_lcl.tenants.set([tenant])
        