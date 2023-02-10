from rest_framework import serializers

from .models import Item, Task, DemoModel
import django_filters

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class DemoModelSerializer(serializers.ModelSerializer):
    # year = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = DemoModel
        fields = '__all__'