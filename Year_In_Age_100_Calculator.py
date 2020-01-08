import datetime
import time

def get_user_inputs():
    name = input("Whats your name? : ")
    age = input("Whats your age ? : ")
    return age, name


def calculate(age, name):
    years_to_age_100 = int(100) - int(age)
    current_year = datetime.datetime.now().year
    print(name + ", When you'l get 100 years old the year will be " + (str(int(current_year) + int(years_to_age_100)))
          + " ! ")

    num = input("pick a number for multiple prints : ")
    for n in range(0, int(num)):
        print(name + ", When you'l get 100 years old the year will be " + (str(int(current_year) + int(years_to_age_100)))
          + " ! ")


def play():
    age_and_name = get_user_inputs()
    calculate(age_and_name[0], age_and_name[1])
    time.sleep(4)

play()