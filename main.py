import os
from mastermind_engine import report_count, \
    number_correct, bull_cow_count, number_generator
from termcolor import cprint, colored

while True:
    response = input(colored("Бажаєте ще зіграти? ", color='yellow'))
    if response == "q" or response == "й":
        break
    os.system('CLS')
    number_generator()
    while True:
        number = input(colored("Введіть чотирьохзначне число: ", color='blue'))
        if response == "q" or response == "q":
            os.system('EXIT')
        if number_correct(number):
            bull = bull_cow_count()["bull"]
            cow = bull_cow_count()["cow"]
            report = report_count()
            if report:
                print("Ура, ви вгадали це число за {} спроб".format(report))
                break
            else:
                print("Биків: ", bull)
                print("Корів: ", cow)
        else:
            print("Ви ввели не коректне число")
