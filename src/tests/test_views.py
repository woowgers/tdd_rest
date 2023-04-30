import pytest
from django.test import Client
from django.urls import reverse
from rest_framework import status

from puppies.models import Puppy
from puppies.serializers import PuppySerializer
from tests.conftest import PuppyData

client = Client()


@pytest.mark.django_db
def test_get_all_puppies(create_puppies: None):
    response = client.get(reverse('get_post_puppies'))
    puppies = Puppy.objects.all()
    serializer = PuppySerializer(puppies, many=True)
    assert response.data == serializer.data  # type: ignore
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_get_one_puppy(puppies_data: tuple[PuppyData, ...], create_puppies: None):
    puppy_name = puppies_data[0].name
    response = client.get(reverse('get_delete_update_puppy', kwargs={'pk': Puppy.objects.get(name=puppy_name).pk}))
    puppy = Puppy.objects.get(name=puppy_name)
    serializer = PuppySerializer(puppy)
    assert response.status_code == status.HTTP_200_OK
    assert response.data == serializer.data  # type: ignore
