from django.test import TestCase

from puppies.models import Puppy


class TestPuppy(TestCase):
    def setUp(self):
        Puppy.objects.create(name='Casper', age=3, breed='Bull Dog', color='Black')
        Puppy.objects.create(name='Muffin', age=1, breed='Gradane', color='Brown')

    def test_puppy_repr(self):
        casper_puppy = Puppy.objects.get(name='Casper')
        muffin_puppy = Puppy.objects.get(name='Muffin')

        assert repr(casper_puppy) == str(casper_puppy.name)
        assert repr(muffin_puppy) == str(muffin_puppy.name)
