jumin = "990120-1234567"

print("tjdquf : " + jumin[7])
print("연 :" + jumin[0:2])
print("월:" + jumin[2:4])
print("일:" + jumin[4:6])
print("생년월일: "+ jumin[:6])
print("뒤에서부터:" + jumin[-7:])


print("나는 %d살입니다" %20)
(print("나는 %s을 좋아해요." % "파이/선"))

print("나는{}살입니다".format(20))

print("나는 {0}색과 {1}색을 좋아해요.".format("파란", "빨강"))
print("나는 {age}살이며, {color}색을 좋아해요".format(age = 20, color="빨강"))

age = 20
color = "빨강"



#url = "http://naver.com"
url = "http://google.com"
my_str = url.replace("http://","")
print(my_str)
my_str = my_str[:my_str.index(".")]
print(my_str)
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print(password)

#리스트 []
subway1=10
subway2=20
subway3=30

subway = [10,20,30]
print(subway)
subway = ["유재석","조세호"]
print(subway.index("조세호"))
subway.append("하하")
print(subway)
subway.insert(1,"정형동")
print(subway)
print(subway.pop())


cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3])
print("hi")

from random import*
users = range(1,21)
print(type(users))
users = list(users)
print(type(users))

print(users)
shuffle(users)
print(users)

winners = sample(users,4)
print(winners)

print("당첨자발표")
print("치킨:{0}".format(winners[0]))
print("커피: {0}".format(winners[1:]))



