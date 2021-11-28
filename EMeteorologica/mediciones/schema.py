import graphene
from graphene_django import DjangoObjectType
from users.schema import UserType
from django.db.models import Q

from .models import Medicion

class MedicionType(DjangoObjectType):
    class Meta:
        model = Medicion


class Query(graphene.ObjectType):
    mediciones = graphene.List(MedicionType, search=graphene.String())

    def resolve_mediciones(self, info, search=None, **kwargs):
        if search:
            filter = (
                Q(Fecha__icontains=search)
            )        
            return Medicion.objects.filter(filter)

        return Medicion.objects.all()

class CreateMedicion(graphene.Mutation):
    id = graphene.Int()
    Temperatura = graphene.Float()
    Luz = graphene.Int()
    Humedad = graphene.Int()
    Fecha = graphene.Date()
    posted_by = graphene.Field(UserType)

    class Arguments:
        Temperatura = graphene.Float()
        Luz = graphene.Int()
        Humedad = graphene.Int()

    def mutate(self, info, Temperatura, Luz, Humedad):
        user = info.context.user or None

        medicion = Medicion(
            Temperatura=Temperatura,
            Luz=Luz,
            Humedad=Humedad,
            posted_by=user,
        )
        medicion.save()

        return CreateMedicion(id=medicion.id, 
            Temperatura=medicion.Temperatura, 
            Luz=medicion.Luz, 
            Humedad=medicion.Humedad, 
            Fecha=medicion.Fecha,
            posted_by=medicion.posted_by,
        )


class Mutation(graphene.ObjectType):
    create_medicion = CreateMedicion.Field()
