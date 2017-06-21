from django.db import models

# Create your models here.
NAME_VERBOSE      = 'nombre'
OWNER_VERBOSE     = 'dueño'
CREDITS_VERBOSE   = 'créditos'
STATUS_VERBOSE    = 'estado'
HAPPINESS_VERBOSE = 'felicidaad'
SPECIES_VERBOSE   = 'especie'

class Greeting(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)

class Pet(models.Model):

    name = models.CharField(max_length=30, verbose_name=NAME_VERBOSE)

    species = models.CharField(max_length=30, verbose_name=SPECIES_VERBOSE)

    owner = models.CharField(max_length=15, verbose_name=OWNER_VERBOSE)

    credits = models.IntegerField(default=0, verbose_name=CREDITS_VERBOSE)

    status = models.IntegerField(default=0, verbose_name=STATUS_VERBOSE)

    happiness = models.IntegerField(default=0, verbose_name=HAPPINESS_VERBOSE)

    def __str__(self):
        return self.name + ' ' + self.species + ' (' + self.owner + ')'
