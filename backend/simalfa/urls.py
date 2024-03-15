from django.urls import path
from simalfa.views import (TenantCrudView, 
                           MetricsCrudView,
                           FormulaCrudView,
                           ServiceItemCrudView,
                           ServiceItemMetricsCrudView)

urlpatterns = [
    #metrics
    path('metrics/', MetricsCrudView.MetricsGetCreateView.as_view(), name='metrics-get-create'),
    path('metrics/<int:pk>/', MetricsCrudView.MetricsGetAlterView.as_view(), name='mestrics-get-alter'),
    #formulas
    path('formula/', FormulaCrudView.FormulaGetCreateView.as_view(), name='metrics-get-create'),
    path('formula/<int:pk>/', FormulaCrudView.FormulaGetAlterView.as_view(), name='mestrics-get-alter'),
    #service-items
    path('service-item/', ServiceItemCrudView.ServiceItemGetCreateView.as_view(), name='service-item-get-create'),
    path('service-item/<int:pk>/', ServiceItemCrudView.ServiceItemGetAlterView.as_view(), name='service-item-get-alter'),
    #service-items-metrics
    path('service-item-metrics/', ServiceItemMetricsCrudView.ServiceItemMetricsGetPostView.as_view(), name='service-item-metrics-get-create'),
    path('service-item-metrics/<int:pk>/', ServiceItemMetricsCrudView.ServiceItemMetricsGetPutPatchView.as_view(), name='service-item-metrics-get-alter'),
    #tenants
    path('tenant/', TenantCrudView.TenantGetCreateView.as_view(), name='tenant-get-create'),
    path('tenant/<int:pk>/', TenantCrudView.TenantGetPutView.as_view(), name='tenant-get-put-patch'),
]