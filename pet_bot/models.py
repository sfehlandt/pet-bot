from django.db import models
from django.utils import timezone
from enum import Enum
import random

# Create your models here.
NAME_VERBOSE      = 'nombre'
OWNER_VERBOSE     = 'dueño'
CREDITS_VERBOSE   = 'créditos'
STATUS_VERBOSE    = 'estado'
SPECIES_VERBOSE   = 'especie'
AVAILABLE_VERBOSE = 'disponibles'
REQUIRED_VERBOSE  = 'necesitados'

DESCRIPTION_VERBOSE = 'descripción'
DEADLINE_VERBOSE    = 'plazo'

class Greeting(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)

class Pet(models.Model):

    class Meta:
       verbose_name = 'Mascota'
       verbose_name_plural = 'Mascotas'

    OK      = 0
    BORED   = 1
    HUNGRY  = 2
    COLD    = 3
    DIRTY   = 4
    SICK    = 5
    INJURED = 6
    SAD     = 7

    STATE_CHOICES = (
        (OK      , 'Ok' ),
        (BORED   , 'Aburrido' ),
        (HUNGRY  , 'Hambriento' ),
        (COLD    , 'Con frío' ),
        (DIRTY   , 'Sucio' ),
        (SICK    , 'Enfermo' ),
        (INJURED , 'Herido' ),
        (SAD     , 'Triste' ),
    )

    name = models.CharField(max_length=30, verbose_name=NAME_VERBOSE)

    species = models.CharField(max_length=30, verbose_name=SPECIES_VERBOSE)

    owner_name = models.CharField(max_length=15, verbose_name=OWNER_VERBOSE)

    owner_id = models.BigIntegerField(verbose_name=OWNER_VERBOSE + '_id')

    available_credits = models.IntegerField(default=0, verbose_name=CREDITS_VERBOSE +' '+ AVAILABLE_VERBOSE)

    state = models.IntegerField(default=0, choices=STATE_CHOICES, verbose_name=STATUS_VERBOSE)

    required_credits = models.IntegerField(default=0, verbose_name=CREDITS_VERBOSE +' '+ REQUIRED_VERBOSE)

    def __str__(self):
        return self.name + ' ' + self.species + ' (' + self.owner_name + ')'

    def use_credits(self):
        if self.state == Pet.OK or self.required_credits > self.available_credits:
            return False
        else:
            self.state = Pet.OK
            self.available_credits = self.available_credits - self.required_credits
            self.required_credits = 0
            self.save()
            return True

    def random_bad_state(self, credits):
        states = [x[0] for x in Pet.STATE_CHOICES]
        states = states[1:]
        self.state = random.choice(states)
        self.required_credits = credits
        self.save()

class Task(models.Model):

    class Meta:
       verbose_name = 'Tarea'
       verbose_name_plural = 'Tareas'

    DONE     = 0
    PENDING  = 1
    DOING    = 2

    STATUS_CHOICES = (
        (DONE,    'Terminada'),
        (PENDING, 'Pendiente'),
        (DOING,   'En progreso'),
    )

    name = models.CharField(max_length=30, verbose_name=NAME_VERBOSE)

    description = models.CharField(max_length=255, verbose_name=DESCRIPTION_VERBOSE)

    pet = models.ForeignKey(Pet, related_name='tasks', blank=True, null=True, verbose_name=Pet._meta.verbose_name)

    credits = models.IntegerField(default=0, verbose_name=CREDITS_VERBOSE)

    status = models.IntegerField(default=PENDING, choices=STATUS_CHOICES, verbose_name=STATUS_VERBOSE)

    deadline = models.DateTimeField(verbose_name=DEADLINE_VERBOSE)

    def __str__(self):
        return self.name

    def mark_as_doing(self):
        self.status = Task.DOING
        self.save()

    def mark_as_done(self):
        self.status = Task.DONE
        self.save()

    def mark_as_pending(self):
        self.status = Task.PENDING
        self.save()
