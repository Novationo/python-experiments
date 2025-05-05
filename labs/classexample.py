class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def display(self):
        print("Name: ", self.name)
        print("Grade: ",self.grade)

student1 = Student(input("Name: ",), int(input("Grade: ")))
student1.display()