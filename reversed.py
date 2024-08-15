def reverse_number(number):
    reversed_number = (str(number)[::-1])
    return reversed_number



number = eval(input("Enter a number: "))
print(reverse_number(number))