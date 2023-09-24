from datetime import date
from datetime import timedelta

class Person:
    colors = ['red', 'yellow', 'blue', '#776655']
    min_year = 18
    max_years = 99

    def __init__(self,
                 name="Jan",
                 surname="Kowalski",
                 #date_of_birth=date.today(),
                 foot_size=33,
                 eyes_color="red"):
        self.name = name
        self.surname = surname
        #self.date_of_birth = date_of_birth
        self.foot_size = foot_size
        self.eyes_color = eyes_color

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) > 1:
            self.__name = name

    # @property
    # def date_of_birth(self):
    #     return self.__date_of_birth
    #
    # @date_of_birth.setter
    # def date_of_birth(self, date_of_birth):
    #     if self.__class__.min_year <= self.__class__.how_many_years(date_of_birth) <= self.__class__.max_years:
    #         self.__date_of_birth = date_of_birth

    @property
    def foot_size(self):
        return self.__foot_size

    @foot_size.setter
    def foot_size(self, foot_size):
        if 24 <= foot_size <= 42: #(24<= foot_size) and (foot_size <= 42)
            self.__foot_size = foot_size

    @property
    def eyes_color(self):
        return self.__eyes_color

    @eyes_color.setter
    def eyes_color(self, eyes_color):
        if eyes_color in self.__class__.colors:
            self.__eyes_color = eyes_color

    def age(self):
        return self.__class__.how_many_years(self.date_of_birth())

    @staticmethod
    def how_many_years(date_of_birth):
        today = date.today()
        one_or_zero = \
            ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))
        year_delta = today.year - date_of_birth.year
        return year_delta - one_or_zero


    def __str__(self):
        return "{ first_name: " + self.name + \
            ", second_name: " + self.surname + \
            ", foot: " + str(self.foot_size) + \
            ", eyes: " + self.eyes_color + " }"

    def __repr__(self):
        return str(self)


if __name__ == '__main__':
    person = Person()
    print(person)
    # person.eyes_color = "blue"
    # person.date_of_birth = date.today() - 19 * timedelta(days=365)
