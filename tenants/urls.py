from django.urls import include, path
from rest_framework import routers
from .views import TenantViewSet, TenantUnitViewSet, TenantPropertyListView

router = routers.DefaultRouter()
router.register(r'view', TenantViewSet, basename='tenantunit')

unit_router = routers.DefaultRouter()
unit_router.register(r'units', TenantUnitViewSet, basename='unit')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(unit_router.urls)),
    path('propertyunits/', TenantPropertyListView.as_view(), name='tenantproperty-list'),

]
