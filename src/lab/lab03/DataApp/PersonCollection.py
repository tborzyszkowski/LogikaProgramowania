from Person import Person
from datetime import date


class PersonCollection:
    def __init__(self, person_list=[]):
        self.person_list = person_list

    def add_person(self, person):
        self.person_list.append(person)

    def delete(self, person):
        if person in self.person_list:
            self.person_list.remove(person)

    def __str__(self):
        return "PersonCollection: " + str(self.person_list)


if __name__ == '__main__':
    person_collection = PersonCollection()
    fst = Person("Anna", "Kos", date.today(), 12, "pink")
    person_collection.add_person(fst)
    person_collection.add_person(Person())
    print(str(person_collection))

    person_collection.delete(fst)
    print(str(person_collection))
