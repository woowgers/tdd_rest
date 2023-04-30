from dataclasses import dataclass

import pytest

from puppies.models import Puppy


@dataclass
class PuppyData:
    name: str
    age: int
    breed: str
    color: str


@pytest.fixture
def puppies_data() -> tuple[PuppyData, ...]:
    return (
        PuppyData(name='Casper', age=3, breed='Samoyed', color='White'),
        PuppyData(name='Zoydberg', age=4, breed='Bull Terier', color='Black'),
        PuppyData(name='Shupel', age=1, breed='Sheepdot', color='Brown'),
        PuppyData(name='Momba', age=2, breed='Saluki', color='Grey'),
    )


@pytest.fixture
@pytest.mark.django_db
def create_puppies(puppies_data: tuple[PuppyData, ...]) -> None:
    for puppy in puppies_data:
        Puppy.objects.create(name=puppy.name, age=puppy.age, breed=puppy.breed, color=puppy.color)
