import logging
logging.basicConfig(level=logging.DEBUG, format='%(message)s')

def calculator():
    action_type = int(input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:"))
    num_one = float(input('Podaj składnik 1:'))
    num_two = float(input('Podaj składnik 2:'))
    if action_type == 1:
        variable_name = "Dodaję"
        variableone = logging.info('%s %s i %s', variable_name, num_one, num_two)
        result = num_one + num_two
    elif action_type == 2:
        variable_name = "Odejmuję"
        variableone = logging.info('%s %s i %s', variable_name, num_one, num_two)
        result = num_one - num_two
    elif action_type == 3:
        variable_name = "Mnożę"
        variableone = logging.info('%s %s i %s', variable_name, num_one, num_two)
        result = num_one * num_two
    else:
        variable_name = "Dzielę"
        variableone = logging.info('%s %s i %s', variable_name, num_one, num_two)
        result = num_one / num_two

    print("Wynik to %s" % result)
calculator()