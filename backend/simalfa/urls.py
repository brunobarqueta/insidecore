from django.urls import path
from simalfa.views import TenantCrudView, MetricsCrudView, FormulaCrudView

urlpatterns = [
    path('tenant/', TenantCrudView.TenantListCreateView.as_view(), name='tenant-list-create'),
    path('tenant/<int:pk>/', TenantCrudView.TenantGetAlterDeleteView.as_view(), name='tenant-get-alter-delete'),
    path('metrics/', MetricsCrudView.MetricsListCreateView.as_view(), name='metrics-list-create'),
    path('metrics/<int:pk>/', MetricsCrudView.MetricsGetAlterDeleteView.as_view(), name='mestrics-get-alter-delete'),
    path('formula/', FormulaCrudView.FormulaListCreateView.as_view(), name='metrics-list-create'),
    path('formula/<int:pk>/', FormulaCrudView.FormulaGetAlterDeleteView.as_view(), name='mestrics-get-alter-delete'),
]