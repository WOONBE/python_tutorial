numbers = [1,2,3,4,5,6,7,1,1,1,2]
counter = {}

for number in numbers:
    if number in counter:
        counter[number] = counter[number] + 1
    else:
        counter[number] = 1

print(counter)