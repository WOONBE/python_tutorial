#배운거 활용 정리

#2-4장
#input()
#string = input("인사말을 입력하세요>") 식으로 사용

#format
#string ="{}".format(10) {}갯수가 매개변수보다 많으면 오류발생
print(string)
{:f}:소수점 출력 / {:g}:의미없는 소수점 제거

#upper/lower
a = "exexex"
a.upper/lower() 형식으로 사용

#strip/isAA
공백제거/ 문자열의 구성 파악

#find/rfind
처음등장하는 위치를 왼쪽부터 찾기/ 오른쪽부터 찾기

#in
print("a" in "abcde") 식으로 사용해서 안에 있는지 찾기
값 in 리스트 형식으로 사용

#split
a = "10 20 30 40 50".split(" ")
print(a)
['10', '20', '30', '40', '50'] 처럼 나옴

#3장

#if 조건문
if True:
    print("sssss")
elif:
    print("xxxxx")
else: 
    print("rrrrr")

#4장

#리스트
list = [a, b, c, d, e]
#print(list[0]) 하면 0번째 위치의 요소가 나옴

#요소 추가하기
list.append(요소) 끝에 요소 추가
list.insert(위치,요소) 원하는 위치에 요소 추가
list.extend([4,5,6]) extend는 한번에 여러개 추가 원할때 사용

#요소 제거하기
del list[인덱스] 둘다 위치기반으로 제거
list.pop(인덱스)
list.remove(값) 얜 위치기반 아님, 가장 앞에 있는거 하나만 제거
list.clear() 모두 다 제거

#for 반복문
ex) for i in range(1,10,3)

#딕셔너리
list = [] / dict = {}으로 선언함 / 꺼내쓸땐 []사용해서 꺼내씀
dict = {
    "name" = "건조망고",
    "type" = "당절임"
}
#이런식으로 큰따옴표를 붙여서 정의해야 오류가 안뜸

#딕셔너리에 값 추가/제거
추가: 딕셔너리["새로운키"] = 새로운 값
제거: del dictionary["키"]

#내부에 키 확인은 in 사용 or get()사용
if key in dictionary:
    print(dictionary[key])

value = dictionary.get("존재하지 않는 키")
print(value)

for key in dictionary:
    코드

#4-3부터 시작

#범위
#a = range(1,10,3) 이면 1에서 9사이에 3의배수를 구해준다

#반대로 반복하기
1. for i in range(4, -1)식으로 -를 넣어준다
2. for i in reversed(range(5)) reversed를 넣어준다

#while 반복문
#덧셈이면 0을 곱셈이면 1을 먼저 선언해주고 ex)number = 0 or 1
while number<10:
    print("sssssss")
    number += 1 이런식으로 무한 반복이 되게 설정

#break / continue

#5장 함수
def 함수 이름():
    문장 식으로 사용

#가변 매개변수
def 함수이름(매개변수, 매개변수, ..., *가변 매개변수):
    문장
#가변 매개변수 뒤에는 일반 매개변수 불가/ 가변 매개변수는 하나만 사용가능

#기본 매개변수
(value, '매개변수 = 값'(기본매개변수))
맨앞은 가변 매개변수이고 뒤에 값이 기본매개변수임
보통 가변 기본 순으로 사용함

#키워드 매개변수(좀 햇갈림)

#return
def return_test():
    return 100 
value = return_test()
print(value) (100을 안적으면 None으로 출력됨)

#기본적인 함수 활용
def 함수(매개변수):
    변수 = 초기값(덧셈이면 0/ 곱셈이면 1)
    여러가지 처리
    여러가지 처리
    여러가지 처리
    return 변수

def sum_all(start=0, end=100, step=1):
    output = 0
    for i in range(start, end+1, step):
        output += 1
    return output

print(sum_all(0, 100, 2))

#튜플
tuple_test = (데이터, 데이터, 데이터 , .....)식으로 사용
-하나만 넣어서 정의하려면 tuple = (273,)처럼 ',' 넣어서 정의해야함
-괄호 없이도 사용 가능함

a, b = 10, 20
a, b = b, a
#print(a, b) 하면 20, 10이 나옴

#람다부터 시작
map(함수, 리스트) 새로윤 리스트 구성
filter(함수, 리스트) 리턴값이 True로 나오게 새로운 리스트를 구성해줌


