from django.test import TestCase
from ..models import Pet, Task
from .data import *
from ..controller import *

class ControllerTestCase(TestCase):

    # Arrange:
    def setUp(self):
        self.pet_data = PET_DATA
        self.pet = Pet.objects.create(**self.pet_data)
        self.owner_id = self.pet.owner_id

        self.task_1 = Task.objects.create(**TASK_DATA_LAMBDA('1'))
        self.task_1.pet = self.pet
        self.task_1.save()
        self.task_2 = Task.objects.create(**TASK_DATA_LAMBDA('2'))
        self.task_2.pet = self.pet
        self.task_2.save()
        self.task_3 = Task.objects.create(**TASK_DATA_LAMBDA('3'))
        self.task_3.pet = self.pet
        self.task_3.save()
        self.task_4 = Task.objects.create(**TASK_DATA_LAMBDA('4'))
        self.task_5 = Task.objects.create(**TASK_DATA_LAMBDA('5'))
        self.required_credits = self.pet.required_credits
        self.available_credits = self.pet.available_credits

    def test_find_pet(self):
        # Act:
        pet_found = find_pet(self.owner_id)
        # Assert:
        self.assertEquals(pet_found, self.pet)

    def test_find_pet_reject_invalid(self):
        # Act / Assert:
        pet_found = None
        with self.assertRaises(ValueError):
            pet_found = find_pet(self.owner_id + '32')
        self.assertEquals(pet_found, None)

    def test_find_task(self):
        # Act:
        task_found = find_task(self.task_1.id)
        # Assert:
        self.assertEquals(task_found, self.task_1)

    def test_find_task_reject_invalid(self):
        # Act / Assert:
        task_found = None
        with self.assertRaises(ValueError):
            task_found = find_task(900)
        self.assertEquals(task_found, None)

    def test_my_tasks(self):
        tasks_list = [self.task_1, self.task_2, self.task_3]
        pet_tasks  = my_tasks(self.owner_id)
        self.assertEquals(tasks_list, pet_tasks)

    def test_start_task(self):
        # Act:
        pet_tasks_before = self.pet.tasks.all()
        task_count_before = len(pet_tasks_before)
        new_task = self.task_4
        # Assert:
        self.assertFalse(new_task in map(lambda x: x, pet_tasks_before))
        self.assertEquals(new_task.status, Task.PENDING)
        # Act:
        start_task(self.owner_id, new_task.pk)
        # Assert:
        pet_tasks_after = self.pet.tasks.all()
        task_count_after = len(pet_tasks_after)
        self.assertTrue(task_count_before + 1 == task_count_after)
        self.assertTrue(new_task in map(lambda x: x, pet_tasks_after))

    def test_finish_task(self):
        # Arrange:
        pet_credits_before = self.pet.available_credits
        task_to_finish = self.task_4
        start_task(self.owner_id, task_to_finish.id)
        # Act:
        finish_task(self.owner_id, task_to_finish.id)
        # Assert:
        self.pet = find_pet(self.owner_id)
        pet_credits_after = self.pet.available_credits
        self.assertFalse(task_to_finish.id in map(lambda x: x.id, self.pet.my_tasks()))
        self.assertEquals(pet_credits_before + task_to_finish.credits, pet_credits_after)

    def test_free_tasks(self):
        # Arrange:
        tasks_list = [self.task_4, self.task_5]
        # Act:
        free_tasks_hoped  = free_tasks()
        # Assert:
        self.assertEquals(tasks_list, free_tasks_hoped)

    def test_pet_status(self):
        # Assert:
        self.assertEquals(Pet.VERBOSE_STATE[self.pet.state], pet_status(self.owner_id))

    def tests_my_credits(self):
        # Assert:
        self.assertEquals(self.pet.available_credits, my_credits(self.owner_id))

    def tests_use_credits(self):
        # Arrange:
        available_credit_before = self.pet.available_credits
        required_credits_before = self.pet.required_credits
        self.assertTrue(self.pet.state != Pet.OK)
        # Act:
        use_credits(self.owner_id)
        # Assert:
        self.pet = find_pet(self.owner_id)
        self.assertTrue(self.pet.state == Pet.OK)
        self.assertEquals(
            self.pet.available_credits,
            available_credit_before - required_credits_before
        )
        self.assertEquals(self.pet.required_credits, 0)
