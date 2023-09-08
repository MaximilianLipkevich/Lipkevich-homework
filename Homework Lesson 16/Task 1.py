class Person:
    def __init__(self, name, surname, age, is_present):
        self.name = name
        self.surname = surname
        self.age = age
        self.is_present = is_present

    def greetings(self):
        print(f'Hello, my name is {self.name}, I am {self.age} years old.')

class Student(Person):
    def __init__(self, name, surname, age, is_present, grade, performance):
        super().__init__(name, surname, age, is_present)
        self.grade = grade
        self.performance = performance

    def call_parents(self):
        if not self.is_present:
            self.is_present = True
            print("Student arrived at school and is now present")
        else:
            print("Student is already present")



class Teacher(Person):
    def __init__(self, name, surname, age, is_present, subject, salary):
        super().__init__(name, surname, age, is_present)
        self.subject = subject
        self.salary = salary

    def get_salary(self):
        if self.is_present:
            print(f'{self.name} {self.surname} got paid her salary of {self.salary} dollars')
        else:
            print(f'{self.name} {self.surname} is absent and thus is not getting her {self.salary} dollars salary')


student1 = Student('Max', 'Lipkevich', 22, False, 1, 'excellent')
teacher1 = Teacher('Amelia', 'Watson', 30, True, 'Literature', 3000)

teacher1.greetings()
teacher1.get_salary()
student1.call_parents()