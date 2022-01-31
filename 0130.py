#exception
try:
    number = int(input("정수입력>"))
    print("원의 반지름:", number)
except Exception as exception:
    print(type(exception))
    print(exception)

#raise 예외객체
raise Exception("안녕하세요")
