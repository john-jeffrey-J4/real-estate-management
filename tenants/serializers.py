from rest_framework import serializers
from .models import Tenant

# serializers.py

from rest_framework import serializers
from .models import TenantUnit, Tenant, Property


class TenantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenant
        fields = '__all__'


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'

class TenantPropertySerializer(serializers.ModelSerializer):
    tenant_id = TenantSerializer()
    property_id = PropertySerializer()

    class Meta:
        model = TenantUnit
        fields = '__all__'




class TenantUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = TenantUnit
        fields = '__all__'