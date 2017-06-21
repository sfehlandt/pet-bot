from django.test import TestCase
from .models import Pet

# Create your tests here.
class PetModelTestCase(TestCase):

    def setUp(self):
        self.pet_data = {
            'name'     : 'My Kitten',
            'owner'    : 'Owned',
            'credits'  : 300,
            'status'   : 0,
            'happiness': 0
        }

    def test_model_create_pet(self):
        self.old_count = Pet.objects.count()
        self.pet = Pet(**self.pet_data)
        self.pet.save()
        self.new_count = Pet.objects.count()
        self.assertEquals(self.old_count + 1, self.new_count)

    def test_model_delete_pet(self):
        self.pet = Pet(**self.pet_data)
        self.pet.save()
        self.old_count = Pet.objects.count()
        Pet.objects.filter(pk=self.pet.pk).delete()
        self.new_count = Pet.objects.count()
        self.assertEquals(self.old_count - 1, self.new_count)
