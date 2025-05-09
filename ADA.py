class Person:
    def __init__(self, name, date_of_birth, place_of_birth):
        self._name = name  
        self._date_of_birth = date_of_birth  
        self._place_of_birth = place_of_birth  

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def date_of_birth(self):
        return self._date_of_birth

    def talk(self):
        return f"Hi, my name is {self._name} and I was born in {self._place_of_birth}."

class AdaStaff(Person):
    def __init__(self, name, date_of_birth, place_of_birth, role, base):
        super().__init__(name, date_of_birth, place_of_birth)
        self._role = role
        self._base = base

    @property
    def base(self):
        return self._base

    @base.setter
    def base(self, base):
        self._base = base

    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, role):
        self._role = role

    def talk(self):
        return f"Hi, my name is {self._name}. I work in {self._base} and my role is {self._role}."

class AdaStudent(Person):
    def __init__(self, name, date_of_birth, place_of_birth, course, campus):
        super().__init__(name, date_of_birth, place_of_birth)
        self._course = course
        self._campus = campus

    @property
    def course(self):
        return self._course

    @course.setter
    def course(self, course):
        self._course = course

    @property
    def campus(self):
        return self._campus

    @campus.setter
    def campus(self, campus):
        self._campus = campus

    def talk(self):
        return f"Hi, I'm {self._name}, a student at {self._campus} campus studying {self._course}."


aqil = Person("Aqil Hussain", "01/01/2000", "Manchester")
steve = AdaStaff("Steve Rich", "01/01/1998", "Lincoln", "Lecturer", "Manchester")
sara = AdaStudent("Sara Ali", "05/05/2002", "Leeds", "Software Engineering", "Manchester")

# Demonstrating usage
print(steve.__dict__)
print(aqil.__dict__)
print(sara.__dict__)
print(steve.talk())
print(aqil.talk())
print(sara.talk())
steve.base = "London"
print(steve.talk())
print(steve.name)