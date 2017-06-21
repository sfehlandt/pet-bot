from django.db import models
from django.utils import timezone

# Create your models here.
NAME_VERBOSE      = 'nombre'
OWNER_VERBOSE     = 'dueño'
CREDITS_VERBOSE   = 'créditos'
STATUS_VERBOSE    = 'estado'
HAPPINESS_VERBOSE = 'felicidaad'
SPECIES_VERBOSE   = 'especie'

DESCRIPTION_VERBOSE = 'descripción'
DEADLINE_VERBOSE    = 'plazo'

class Greeting(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)

class Pet(models.Model):

    class Meta:
       verbose_name = 'Mascota'
       verbose_name_plural = 'Mascotas'

    name = models.CharField(max_length=30, verbose_name=NAME_VERBOSE)

    species = models.CharField(max_length=30, verbose_name=SPECIES_VERBOSE)

    owner = models.CharField(max_length=15, verbose_name=OWNER_VERBOSE)

    credits = models.IntegerField(default=0, verbose_name=CREDITS_VERBOSE)

    status = models.IntegerField(default=0, verbose_name=STATUS_VERBOSE)

    happiness = models.IntegerField(default=0, verbose_name=HAPPINESS_VERBOSE)

    def __str__(self):
        return self.name + ' ' + self.species + ' (' + self.owner + ')'

class Task(models.Model):

    class Meta:
       verbose_name = 'Tarea'
       verbose_name_plural = 'Tareas'

    name = models.CharField(max_length=30, verbose_name=NAME_VERBOSE)

    description = models.CharField(max_length=255, verbose_name=DESCRIPTION_VERBOSE)

    pet = models.ForeignKey(Pet, related_name='tasks', blank=True, null=True, verbose_name=Pet._meta.verbose_name)

    credits = models.IntegerField(default=0, verbose_name=CREDITS_VERBOSE)

    status = models.IntegerField(default=0, verbose_name=STATUS_VERBOSE)

    deadline = models.DateTimeField(verbose_name=DEADLINE_VERBOSE)


    def __str__(self):
        return self.name
