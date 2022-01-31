class Student:
    def __str__(self):
        return "{} {}". format(self.이름, self.나이)
    def __init__(self, 이름, 나이):
        print("객체가 생성되었습니다")
        self.이름 = 이름
        self.나이 = 나이
    def __del__(self):
        print("객체가 소멸되었습니다.")
    def 출력(self):  
        print(self.이름, self.나이)
    
student = Student("윤인성", 3)
student.출력()
print(str(student))

import math
import math as 수학
from math import pi, sin
from math import *

