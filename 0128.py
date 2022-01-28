#튜플
a, b = 10,20
a, b = b, a
print(a)


def test():
    return (10, 20)

a,b = test

print(a)
print(b)

#람다
def call_10_times(func):
    for i in range(10):
         func()

def print_hello():
    print("안녕하세요")

call_10_times(print_hello)
pass

def power(item):
    return item * item
def under_3(item):
    return item < 3

list_input_a = [1, 2, 3, 4, 5]

output_a = map(power, list_input_a)
print("map(power, list_input_a:)", output_a)
print(list(output_a))
print()

output_b = filter(under_3, list_input_a)
print(output_b)
print(list(output_b))
