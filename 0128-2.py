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




#람다
power = lambda x: x * x
under_3 = lambda x: x<3


list_input_a = [1, 2, 3, 4, 5]

output_a = map(power, list_input_a)
print("map(power, list_input_a:)", output_a)
print(list(output_a))
print()

output_b = filter(under_3, list_input_a)
print(output_b)
print(list(output_b))
