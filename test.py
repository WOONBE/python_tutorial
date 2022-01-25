print("재수")

print("잘자" in "잘자세요")

numbers = [1,2,6,8,5,3,2,1,9,7,2,3]
counter = {}

for number in numbers:
    if number in counter:
        counter[number] = counter[number] + 1
    else:
        counter[number] = 1
print(counter)