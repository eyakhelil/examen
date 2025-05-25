from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Entity(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Représente un champ défini pour une entité (comme nom, email, etc.)
class FieldDefinition(models.Model):
    FIELD_TYPE_CHOICES = [
        ('text', 'Text'),
        ('number', 'Number'),
        ('boolean', 'Boolean'),
        ('date', 'Date'),
    ]

    entity = models.ForeignKey(Entity, on_delete=models.CASCADE, related_name='fields')
    name = models.CharField(max_length=100)
    field_type = models.CharField(max_length=50, choices=FIELD_TYPE_CHOICES)
    is_required = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} ({self.field_type})"


# Journal d'intégration pour suivre les synchronisations ou erreurs
class IntegrationLog(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    message = models.TextField()
    success = models.BooleanField(default=True)

    def __str__(self):
        return f"[{self.timestamp}] {'Success' if self.success else 'Error'}"