from mastermind_engine import report_count, number_correct


while True:
    number = input("Введіть чотирьохзначне число")
    if number_correct(number):
        if report_count():
            print("Ура, ви вгадали це число за {} спроб".format(report_count()))
            break
        else:
            print("")
    else:
        print("Ви ввели не коректне число")


