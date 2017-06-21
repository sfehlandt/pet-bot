from django.db import models

# Create your models here.
NAME_VERBOSE      = 'Nombre'
OWNER_VERBOSE     = 'Dueño'
CREDITS_VERBOSE   = 'Créditos'
STATUS_VERBOSE    = 'Estado'
HAPPINESS_VERBOSE = 'Felicidaad'

class Greeting(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)

class Pet(models.Model):

    name = models.CharField(max_length=30, verbose_name=NAME_VERBOSE)

    owner = models.CharField(max_length=15, verbose_name=OWNER_VERBOSE)

    credits = models.IntegerField(default=0, verbose_name=CREDITS_VERBOSE)

    status = models.IntegerField(default=0, verbose_name=STATUS_VERBOSE)

    happiness = models.IntegerField(default=0, verbose_name=HAPPINESS_VERBOSE)
