import graphene
from graphene_django.types import DjangoObjectType
from .models import Entity, FieldDefinition

# Type pour Entity
class EntityType(DjangoObjectType):
    class Meta:
        model = Entity

# Type pour FieldDefinition
class FieldDefinitionType(DjangoObjectType):
    class Meta:
        model = FieldDefinition

# Requête GraphQL
class Query(graphene.ObjectType):
    all_entities = graphene.List(EntityType)
    all_fields = graphene.List(FieldDefinitionType)

    def resolve_all_entities(self, info):
        return Entity.objects.all()

    def resolve_all_fields(self, info):
        return FieldDefinition.objects.all()

# Mutation pour créer une entité
class CreateEntity(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)

    entity = graphene.Field(EntityType)

    def mutate(self, info, name):
        entity = Entity.objects.create(name=name)
        return CreateEntity(entity=entity)

# Enregistrez la mutation
class Mutation(graphene.ObjectType):
    create_entity = CreateEntity.Field()

# Schéma complet
schema = graphene.Schema(query=Query, mutation=Mutation)
