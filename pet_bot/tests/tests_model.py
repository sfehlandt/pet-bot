from django.test import TestCase
from ..models import Pet, Task
from .data import *


# Create your tests here.

#-------------------------------------------------------
#-------------------------PET---------------------------
#-------------------------------------------------------

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
        self.assertEquals(self.old_count + 1, self.new_count, 'The number of Pets did not increase by 1 after creating the object')

    def test_model_delete_pet(self):
        # Arrange:
        self.pet = Pet.objects.create(**self.pet_data)
        self.old_count = Pet.objects.count()
        # Act:
        Pet.objects.filter(pk=self.pet.pk).delete()
        # Assert:
        self.new_count = Pet.objects.count()
        self.assertEquals(self.old_count - 1, self.new_count, 'The number of Pets did not decrease by 1 after creating the object')

    def test_model_pet_can_use_credits(self):
        # Arrange:
        self.pet = Pet.objects.create(**self.pet_data)
        self.pet.state = Pet.SICK
        self.pet.available_credits = 300
        self.pet.required_credits  = 200
        self.pet.save()
        # Act:
        self.pet.use_credits()
        # Assert:
        self.assertEquals(self.pet.state, Pet.OK, 'The Pet is not Ok')
        self.assertEquals(self.pet.required_credits, 0, 'The required credits of the Pet did not become 0')
        self.assertEquals(self.pet.available_credits, 100, 'The available credits of the Pet did not decrease after using them')

    def test_model_pet_cannot_use_credits(self):
        # Arrange:
        self.pet = Pet.objects.create(**self.pet_data)
        self.pet.state = Pet.SICK
        self.pet.available_credits = 100
        self.pet.required_credits  = 200
        self.pet.save()
        # Act:
        self.pet.use_credits()
        # Assert:
        self.assertNotEquals(self.pet.state, Pet.OK, 'The Pet is OK after invalid use of credits')
        self.assertNotEquals(self.pet.required_credits, 0, 'The required credits of the Pet became 0 after invalid use of credits')
        self.assertEquals(self.pet.available_credits, 100, 'The available credits of the Pet changed after invalid use of credits')

    def test_model_pet_random_bad_state(self):
        # Arrange:
        self.pet = Pet.objects.create(**self.pet_data)
        # Act:
        self.pet.random_bad_state(100)
        # Assert:
        self.assertNotEquals(self.pet.state, Pet.OK, 'The Pet is Ok after invoking a random bad state')
        self.assertEquals(self.pet.required_credits, 100, 'The required credits of the Pet did not become 100')


#-------------------------------------------------------
#-------------------------TASK--------------------------
#-------------------------------------------------------

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
        self.assertEquals(self.old_count + 1, self.new_count, 'The number of Tasks did not increase by 1 after creating the object')

    def test_model_create_task_with_associated_pet(self):
        # Arrange:
        self.old_count = Task.objects.count()
        self.task_data['pet'] = self.pet
        # Act:
        self.task = Task.objects.create(**self.task_data)
        # Assert:
        self.new_count = Task.objects.count()
        self.assertEquals(self.old_count + 1, self.new_count, 'The number of Tasks did not increase by 1 after creating the object')
        self.assertEquals(self.pet, Task.objects.get(pk=self.task.pk).pet, 'The Pet associated to the Task is not the same')

    def test_model_delete_task(self):
        # Arrange:
        self.task = Task.objects.create(**self.task_data)
        self.old_count = Task.objects.count()
        # Act:
        Task.objects.filter(pk=self.task.pk).delete()
        # Assert:
        self.new_count = Task.objects.count()
        self.assertEquals(self.old_count - 1, self.new_count, 'The number of Tasks did not decrease by 1 after creating the object')

    def test_model_associate_pet_to_task(self):
        # Arrange:
        self.task = Task.objects.create(**self.task_data)
        # Act:
        self.task.pet = self.pet
        self.task.save()
        # Assert:
        self.assertEquals(self.pet, Task.objects.get(pk=self.task.pk).pet, 'The Pet associated to the Task is not the same')

    def test_model_mark_as_done_task(self):
        # Arrange:
        self.task = Task.objects.create(**self.task_data)
        # Act:
        self.task.mark_as_done()
        # Assert:
        self.assertEquals(self.task.status, Task.DONE, 'Task status is not DONE')

    def test_model_mark_as_doing_task(self):
        # Arrange:
        self.task = Task.objects.create(**self.task_data)
        # Act:
        self.task.mark_as_doing()
        # Assert:
        self.assertEquals(self.task.status, Task.DOING, 'Task status is not DOING')

    def test_model_mark_as_doing_task(self):
        # Arrange:
        self.task = Task.objects.create(**self.task_data)
        # Act:
        self.task.mark_as_pending()
        # Assert:
        self.assertEquals(self.task.status, Task.PENDING, 'Task status is not PENDING')
