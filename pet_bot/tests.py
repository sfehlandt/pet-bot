from django.test import TestCase
from .models import Pet, Task
from django.utils import timezone


# Create your tests here.

#-------------------------------------------------------
#-------------------------PET---------------------------
#-------------------------------------------------------
PET_DATA = {
    'name'     : 'Smelly',
    'species'  : 'Cat',
    'owner'    : 'Owned',
    'credits'  : 300,
    'status'   : 0,
    'happiness': 0,
}

class PetModelTestCase(TestCase):
    def setUp(self):
        self.pet_data = PET_DATA

    def test_model_create_pet(self):
        # Arrange:
        self.old_count = Pet.objects.count()
        # Act:
        self.pet = Pet.objects.create(**self.pet_data)
        # Assert:
        self.new_count = Pet.objects.count()
        self.assertEquals(self.old_count + 1, self.new_count)

    def test_model_delete_pet(self):
        # Arrange:
        self.pet = Pet.objects.create(**self.pet_data)
        self.old_count = Pet.objects.count()
        # Act:
        Pet.objects.filter(pk=self.pet.pk).delete()
        # Assert:
        self.new_count = Pet.objects.count()
        self.assertEquals(self.old_count - 1, self.new_count)


#-------------------------------------------------------
#-------------------------TASK---------------------------
#-------------------------------------------------------
TASK_DATA = {
    'name'        : 'Do this thing',
    'description' : 'In order to do this you should...',
    'credits'     : 300,
    'status'      : 0,
    'deadline'    : timezone.now(),
}

class TaskModelTestCase(TestCase):
    def setUp(self):
        self.pet = Pet.objects.create(**PET_DATA)
        self.task_data = TASK_DATA

    def test_model_create_task_without_associated_pet(self):
        # Arrange:
        self.old_count = Task.objects.count()
        # Act:
        self.task = Task.objects.create(**self.task_data)
        # Assert:
        self.new_count = Task.objects.count()
        self.assertEquals(self.old_count + 1, self.new_count)

    def test_model_create_task_with_associated_pet(self):
        # Arrange:
        self.old_count = Task.objects.count()
        self.task_data['pet'] = self.pet
        # Act:
        self.task = Task.objects.create(**self.task_data)
        # Assert:
        self.new_count = Task.objects.count()
        self.assertEquals(self.old_count + 1, self.new_count)
        self.assertEquals(self.pet, Task.objects.get(pk=self.task.pk).pet)

    def test_model_delete_task(self):
        # Arrange:
        self.task = Task.objects.create(**self.task_data)
        self.old_count = Task.objects.count()
        # Act:
        Task.objects.filter(pk=self.task.pk).delete()
        # Assert:
        self.new_count = Task.objects.count()
        self.assertEquals(self.old_count - 1, self.new_count)

    def test_model_associate_pet_to_task(self):
        # Arrange:
        self.task = Task.objects.create(**self.task_data)
        # Act:
        self.task.pet = self.pet
        self.task.save()
        # Assert:
        self.assertEquals(self.pet, Task.objects.get(pk=self.task.pk).pet)
