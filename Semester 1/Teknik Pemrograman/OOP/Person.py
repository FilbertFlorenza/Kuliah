class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return 'name: ' + self.name + '\nage: ' + str(self.age)
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, a):
        self._age = a

    def speak(self, word):
        print(self.name + ' says: ' + word)

class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    @property
    def grade(self):
        return self._grade
    
    @grade.setter
    def grade(self, g):
        if not isinstance(g, int):
            raise ValueError("Only integers are allowed.")
        self._grade = g

class TIStudent(Student):
    def __init__(self, name, age, grade, lesson = ''):
        super().__init__(name, age, grade)
        self.lesson = lesson

    @property
    def lesson(self):
        return self._lesson

    def lesson(self, l):
        self._lesson = l 
      
    
p1 = Person('Filbert', 40)
p1.speak('hello world')
s1 = Student('Filbert 2', 40, 100)
print(p1.name)