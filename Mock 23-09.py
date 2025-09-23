def main():
    num = int(input("Enter a number: "))

    even_or_odd(num)
    positive_or_negative(num)
    square_number(num)
    cube_number(num)

def even_or_odd(num):
    if num % 2 ==0:
        print("Is an even number")
    else:
        print("Is a odd number")

def positive_or_negative(num):
    if num >= 0:
        print("Is a positive number")
    else:
        print("Is a negative number")

def square_number(num):
    print(num*num)

def cube_number(num):
    print(num*num*num)

main()

