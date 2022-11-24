# ENcuentra por qué falla el siguiente código

class Student:

    def __init__(self, first_name, last_name, grades=[]):
        self.first_name = first_name
        self.last_name = last_name
        self.grades = grades
    
    def add_grade(self, grade):
        self.grades.append(grade)
    
    def get_average(self):
        return sum(self.grades) / len(self.grades)

someStudent = Student("PEdro", "Lopez")
someOtherStudent = Student("David", "Garcia")
someStudent.add_grade(98)
someOtherStudent.add_grade(77)
print(someStudent.grades)
print(someOtherStudent.grades)