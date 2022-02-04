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




