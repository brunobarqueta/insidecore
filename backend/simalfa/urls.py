from django.urls import path
from simalfa.views import (TenantCrudView, 
                           MetricsCrudView,
                           FormulaCrudView,
                           ServiceItemCrudView,
                           #ServiceItemMetricsCrudView,
                           ServicesCrudView)

urlpatterns = [
    path('tenant/', TenantCrudView.TenantListCreateView.as_view(), name='tenant-list-create'),
    path('tenant/<int:pk>/', TenantCrudView.TenantGetAlterDeleteView.as_view(), name='tenant-get-alter-delete'),
    path('metrics/', MetricsCrudView.MetricsListCreateView.as_view(), name='metrics-list-create'),
    path('metrics/<int:pk>/', MetricsCrudView.MetricsGetAlterDeleteView.as_view(), name='mestrics-get-alter-delete'),
    path('formula/', FormulaCrudView.FormulaListCreateView.as_view(), name='metrics-list-create'),
    path('formula/<int:pk>/', FormulaCrudView.FormulaGetAlterDeleteView.as_view(), name='mestrics-get-alter-delete'),
    path('service-item/', ServiceItemCrudView.ServiceItemListCreateView.as_view(), name='service-item-list-create'),
    path('service-item/<int:pk>/', ServiceItemCrudView.ServiceItemGetAlterDeleteView.as_view(), name='service-item-get-alter-delete'),
    #path('service-item-metrics/', ServiceItemMetricsCrudView.ServiceItemMetricsListCreateView.as_view(), name='service-item-metrics-list-create'),
    #path('service-item-metrics/<int:pk>/', ServiceItemMetricsCrudView.ServiceItemMetricsGetAlterDeleteView.as_view(), name='service-item-metrics-get-alter-delete'),
    
    
    #Future base models
    path('groups/', ServicesCrudView.GetGroupsView.as_view(), name='groups-list'),
    path('groups/<int:code_group>/items', ServicesCrudView.GetItensForGroupsView.as_view(), name='groups-items-list'),
]