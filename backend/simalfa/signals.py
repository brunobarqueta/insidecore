from django.db.models.signals import post_migrate
from django.dispatch import receiver
from backend.settings import DEBUG
from simalfa.models.tenant import Tenant
from simalfa.models.metrics import Metrics
from simalfa.models.formula import Formula
from simalfa.enums import TypeMetric
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
                    m_cif = Metrics.objects.create(description='Valor Cif/NF', type=TypeMetric.CABECALHO.value, service='CIF',tenant=tenant)
                    m_nd = Metrics.objects.create(description='numero de dias', type=TypeMetric.CABECALHO.value, service='ND',tenant=tenant)
                    m_qtde = Metrics.objects.create(description='Quantidade', type=TypeMetric.SIMULACAO.value, service='QTDE',tenant=tenant)
                    m_mcub = Metrics.objects.create(description='Metros Cubicos', type=TypeMetric.SIMULACAO.value, service='M3',tenant=tenant)
                    m_ts = Metrics.objects.create(description='Taxa de serviço', type=TypeMetric.IMUTAVEL.value, service='TS',tenant=tenant)
                    m_ise = Metrics.objects.create(description='Valor isento de pagamento', type=TypeMetric.IMUTAVEL.value, service='ISE',tenant=tenant)
                    m_alq = Metrics.objects.create(description='Valor Aliquota', type=TypeMetric.IMUTAVEL.value, service='ALQ',tenant=tenant)
                    m_hora = Metrics.objects.create(description='Valor Hora', type=TypeMetric.SIMULACAO.value, service='HORA',tenant=tenant)
    
                if not Formula.objects.exists():
                    formula_qtde_ts = Formula.objects.create(description='MULTIPLICAR PELA QUANTIDADE', expression= 'QTDE * TS', tenant=tenant)
                    formula_qtde_ts.metrics.set([m_qtde, m_ts])
                    
                    formula_isento = Formula.objects.create(description='ZERAR NO DEMONSTRATIVO DE SIMULAÇÃO', expression='ISE * 0', tenant=tenant)
                    formula_isento.metrics.set([m_ise])
                    
                    formula_dia_nf_alq = Formula.objects.create(description='multiplicar o valor da cif/nf de exportação por dia e por aliquota.', expression='ND * CIF * ALQ', tenant=tenant)
                    formula_dia_nf_alq.metrics.set([m_nd, m_cif, m_alq])
                    
                    formula_cif_alq_dia = Formula.objects.create(description='multiplicar o valor CIF pela aliquota e por 10 dias', expression='(CIF * ALQ) * ND', tenant=tenant)
                    formula_cif_alq_dia.metrics.set([m_cif, m_alq, m_nd])
                    
                    formula_ts_hora = Formula.objects.create(description="Multiplicar a cada quantidade 'N'", expression='TS * HORA', tenant=tenant)
                    formula_ts_hora.metrics.set([m_ts, m_hora])
                    
                    
                    