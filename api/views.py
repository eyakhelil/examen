# views.py

from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Task, Entity, FieldDefinition, IntegrationLog
from .serializers import TaskSerializer, EntitySerializer, FieldDefinitionSerializer, IntegrationLogSerializer

# ViewSets pour CRUD
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class EntityViewSet(viewsets.ModelViewSet):
    queryset = Entity.objects.all()
    serializer_class = EntitySerializer

class FieldDefinitionViewSet(viewsets.ModelViewSet):
    queryset = FieldDefinition.objects.all()
    serializer_class = FieldDefinitionSerializer

class IntegrationLogViewSet(viewsets.ModelViewSet):
    queryset = IntegrationLog.objects.all()
    serializer_class = IntegrationLogSerializer

# ✅ Vues personnalisées
class EntityListView(generics.ListAPIView):
    queryset = Entity.objects.all()
    serializer_class = EntitySerializer

class FieldDefinitionListView(generics.ListAPIView):
    serializer_class = FieldDefinitionSerializer

    def get_queryset(self):
        entity_id = self.kwargs.get('entity_id')
        return FieldDefinition.objects.filter(entity_id=entity_id)

class SubmitDataView(APIView):
    def post(self, request):
        serializer = IntegrationLogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Data submitted successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
