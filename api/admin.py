from django.contrib import admin
from .models import Task, Entity, FieldDefinition, IntegrationLog

admin.site.register(Task)
admin.site.register(Entity)
admin.site.register(FieldDefinition)
admin.site.register(IntegrationLog)