import unittest
from .Person import *

class PersonTestCase(unittest.TestCase):
    def test_person_name_correctly_initialized(self):
        person = Person("John")
        self.assertEqual(person.name, "John")

    def test_person_name_correctly_changed(self):
        # Arrange
        person = Person("John")
        # Act
        person.rename("Jan")
        # Assert
        self.assertEqual(person.name, "Jan")

    def test_persons_are_the_same_species(self):
        personAdam = Person("Adam")
        personEwa = Person("Ewa")
        self.assertEqual(personAdam.species, personEwa.species)


if __name__ == '__main__':
    unittest.main()
