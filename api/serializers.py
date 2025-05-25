# api/serializers.py
from rest_framework import serializers
from .models import Task
from .models import Entity, FieldDefinition, IntegrationLog

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class EntitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entity
        fields = '__all__'

class FieldDefinitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FieldDefinition
        fields = '__all__'

    def validate_name(self, value):
        if ' ' in value:
            raise serializers.ValidationError("Le nom du champ ne doit pas contenir d'espaces.")
        return value

    def validate(self, data):
        # Empêche les doublons de noms de champ dans une même entité
        entity = data.get('entity')
        name = data.get('name')

        if entity and FieldDefinition.objects.filter(entity=entity, name=name).exists():
            raise serializers.ValidationError("Ce nom de champ existe déjà pour cette entité.")
        return data

class IntegrationLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = IntegrationLog
        fields = '__all__'