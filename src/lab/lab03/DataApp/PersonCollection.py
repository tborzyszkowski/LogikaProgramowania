from Person import Person
from datetime import date
from ReadRepository import ReadRepository


class PersonCollection:
    def __init__(self, person_list=[]):
        self.person_list = person_list

    def add_person(self, person):
        self.person_list.append(person)

    def delete(self, person):
        if person in self.person_list:
            self.person_list.remove(person)

    def add_data(self):
        read_repo = ReadRepository("persons.csv")
        persons_from_csv = read_repo.read_repository()
        for person in persons_from_csv:
            self.add_person(
                Person(person["name"],
                       person["surname"],
                       person["foot_size"],
                       person["eyes_color"])
            )
    def add_persons(self):
        read_repo = ReadRepository("persons.csv")
        persons_from_csv = read_repo.read_person_repository()
        for person in persons_from_csv:
            self.add_person(person)

    def __str__(self):
        return "PersonCollection: " + str(self.person_list)


if __name__ == '__main__':
    person_collection = PersonCollection()
    person_collection.add_persons()
    # fst = Person("Anna", "Kos", date.today(), 12, "pink")
    # person_collection.add_person(fst)
    # person_collection.add_person(Person())
    # print(str(person_collection))

    # person_collection.delete(fst)
    print(str(person_collection))
