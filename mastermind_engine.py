from random import randint

_random_number = []
_enter_number = "0"
_enter_inputs = 0
_count = {"cow": 0, "bull": 0}


def number_generator():
    """
    Компютер загадує число
    """
    global _random_number
    global _enter_inputs
    _enter_inputs = 0
    i = []
    while len(i) < 4:
        num = randint(1, 9)
        if num not in i:
            i.append(num)
    _random_number = i


def number_correct(number):
    """"
    Перевірка правильності вводу
    """
    if len(number) != 4:
        return False
    for i in number:
        if list(number).count(i) > 1:
            return False
        elif int(i) == 0:
            return False
    global _enter_number
    _enter_number = number
    return _enter_number



def report_count():
    """
    Кількість спроб відгадати число
    """
    global _enter_inputs
    _enter_inputs += 1
    if _count["bull"] == 4:
        return _enter_inputs


def bull_cow_count():
    """
    Кількість биків, кількість корів dict
    """
    global _count
    _count = {"cow": 0, "bull": 0}
    inc = 0
    for i in _enter_number:
        if int(i) in _random_number:
            _count["cow"] += 1
        if int(i) == _random_number[inc]:
            _count["bull"] += 1
        inc += 1
    return _count


if __name__ == "__main__":
    number_correct("1234")
    print(_enter_number)




