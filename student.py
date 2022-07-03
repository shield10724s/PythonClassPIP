class Student(object):
    def __init__(self, name, age, gender, level, grades=None):
        self.name = name
        self.age = age
        self.gender = gender
        self.level = level
        self.grades = {}

    def setGrade(self, course, grade):
        self.grades[course] = grade

    def getGrade(self, course):
        return self.grades[course]

    def getGPA(self):
        return sum(self.grades.values())/len(self.grades)

shriyans = Student('shriyans', 14, 'male', 9, {'math':9})
print(shriyans.getGPA())

ghost = Student('ghost', 13, 'female', 8, {'math':7})
print(ghost.setGrade('school', 7))
print(ghost.getGrade('school'))
print(ghost.getGPA())