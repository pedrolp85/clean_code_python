# https://www.codewars.com/kata/528d36d7cc451cd7e4000339

class Student:
    def __init__(self, name, fives, tens, twenties):
        self.name = name
        self.fives = fives
        self.tens = tens
        self.twenties = twenties

    def calculate_total_money(self) -> int:
        return (self.fives * 5 + self.tens * 10 + self.twenties * 20 )


def most_money(students):
    
    richer_student_name = None
    max_money = -1

    for student in students:
        print(f"el estudiante {student.name} tiene {student.calculate_total_money()}")
        if (student_money:=student.calculate_total_money()) > max_money:
            richer_student_name = student.name
            max_money = student_money
        elif student.calculate_total_money() == max_money:
            richer_student_name = 'all'

    return richer_student_name


phil = Student("Phil", 2, 2, 1)   # tiene 50
cam = Student("Cameron", 2, 2, 0) # tiene 30
geoff = Student("Geoff", 0, 3, 0) # tiene 30

print(most_money([cam, geoff, phil]))
print(most_money([cam, geoff]))
print(most_money([geoff]))