class 학생:
    def __init__(self, name, korean, math ,english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
    def 총점(self):
        return self.korean + self.math +\
            self.english + self.science

def 출력(self):
    print(self.name, self.총점())

