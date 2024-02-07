

from rest_framework import viewsets, generics
from .models import Tenant, TenantUnit
from .serializers import TenantSerializer, TenantUnitSerializer, TenantPropertySerializer


class TenantViewSet(viewsets.ModelViewSet):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer


class TenantUnitViewSet(viewsets.ModelViewSet):
    queryset = TenantUnit.objects.all()
    serializer_class = TenantUnitSerializer


class TenantPropertyListView(generics.ListAPIView):
    serializer_class = TenantPropertySerializer

    def get_queryset(self):
        queryset = TenantUnit.objects.all()
        property_id = self.request.query_params.get('property_id', None)
        if property_id:
            queryset = queryset.filter(property_id=property_id)
        return queryset
