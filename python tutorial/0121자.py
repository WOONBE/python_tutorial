numbers = [1,2,3,4,5,6,7,1,2,3,4,5,6,2,3,4,6,7,8,9]
counter = {}
for number in numbers:
    if number in counter:
        counter[number] +=1
    else:
        counter[number] = 1

print(counter)

year = int(input("연도를 입력하세요>"))
if((year%4 == 0 and year%100 !=0) or year % 400 ==0 ):
    print(year, "윤년입니다")
else :
    print(year, "윤년이 아닙니다")

x = float(input("점수를 입력하세요 : "))
grade = ' '
if(x >= 4.5):
    grade = 'A+'
elif(x >= 4.0):
    grade = 'A'
elif(x >= 3.5):
    grade = 'B+'
elif(x >= 3.0):
    grade = 'B'
elif(x >= 2.5):
    grade = 'C+'
elif(x >= 2.0):
    grade = 'C'
else:
    grade = 'D'
print(grade)

