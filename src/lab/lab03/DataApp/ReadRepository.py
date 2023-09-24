import csv
from Person import Person

class ReadRepository:
    def __init__(self, path):
        if self.__class__.valid_path(path):
            self.path = path
        else:
            raise AttributeError

    @staticmethod
    def valid_path(path):
        result = True
        if path is None:
            result = False
        # try:
        #     open(path)
        # except FileNotFoundError:
        #     result = False
        return result

    def read_repository(self):
        result = []
        with open(self.path) as csvfile:
            readCSV = csv.reader(csvfile, delimiter=';')
            for row in readCSV:
                print(row[0], row[1], row[2], )
                person = Person(row[0], row[1], int(row[2]), row[3])
                result.append(person)
        return result

    def read_person_repository(self):
        result = []
        with open(self.path) as csvfile:
            readCSV = csv.reader(csvfile, delimiter=';')
            for row in readCSV:
                print(row[0], row[1], row[2], )
                person = {"name": row[0], "surname": row[1], "foot_size": row[2], "eyes_color": row[3]}
                result.append(person)
        return result
