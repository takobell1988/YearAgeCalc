
def get_user_input():

    num = int(input("Enter a number: "))
    if (num % 4) == 0:

        print(str(num) + ' is 4 multiple ')

    elif (num % 2) == 0:

        print(str(num) + ' is Even')

    else:

        print(str(num) + ' is Odd')


# get_user_input()


def devided_of_not():
    num = float(input("enter a number : "))
    num_to_devision = float(input("enter a number to devide by : "))
    modulo_value = num % num_to_devision
    print(str(modulo_value))
    if modulo_value == 0:
        print("deviding perfectly !")
    else:
        print("no deviding!")


devided_of_not()