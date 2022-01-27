# 5-1
def print_n_times(value, n):
    for i in range(n):
        print(value)

print_n_times("안녕하세요", 5)

def print_n_times(*values, n=2):
    for i in range(n):
        for value in values:
            print(value)
        print()
    
print_n_times("안녕하세요", "즐거운", "파이썬 프로그래밍", n=3)



def return_test():
    return 100

value = return_test()
print(value) 

def mul(*values):
    output = 1
    for value in values:
        output *= value
    return output
print(mul(5, 7, 9, 10))


#5-2
def factorial(n):
    output = 1
    for i in range(1, n + 1):
        output *= i
    return output

print("5!:", factorial(5))

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print("5!:", factorial(5))

list = ["hong", 1, 2, 3, 4, 5, 6]
i = 1
for i in range(0,len(list),2):
    list[i] = 3

print(list)



