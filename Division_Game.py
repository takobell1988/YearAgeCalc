
def get_user_input():

    num = int(input("Enter a number: "))
    if (num % 4) == 0:

        print(str(num) + ' is 4 multiple ')

    elif (num % 2) == 0:

        print(str(num) + ' is Even')

    else:

        print(str(num) + ' is Odd')


# get_user_input()


def divided_of_not():
    num = float(input("enter a number : "))
    num_to_division = float(input("enter a number to divide by : "))
    modulo_value = num % num_to_division
    print(str(modulo_value))
    if modulo_value == 0:
        print("divisible perfectly !")
    else:
        print("no divisible!")


divided_of_not()