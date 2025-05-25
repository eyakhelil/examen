# api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, EntityViewSet, FieldDefinitionViewSet, IntegrationLogViewSet, EntityListView, FieldDefinitionListView, SubmitDataView

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'entities', EntityViewSet)
router.register(r'fields', FieldDefinitionViewSet)
router.register(r'logs', IntegrationLogViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('entity-list/', EntityListView.as_view(), name='entity-list'),
    path('entity/<int:entity_id>/fields/', FieldDefinitionListView.as_view(), name='field-list'),
    path('submit-data/', SubmitDataView.as_view(), name='submit-data'),
]


