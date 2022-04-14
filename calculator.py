import logging
logging.basicConfig(level=logging.DEBUG, format='%(message)s')

def calculator():
    action_type = int(input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:"))
    num_one = float(input('Podaj składnik 1:'))
    num_two = float(input('Podaj składnik 2:'))
    variable_name = str()
    if action_type == 1:
        print(num_one + num_two)
        variable_name = "Dodaję"
    elif action_type == 2:
        print(num_one - num_two)
        variable_name = "Odejmuję"
    elif action_type == 3:
        print(num_one * num_two)
        variable_name = "Mnożę"
    else:
        print(num_one / num_two)
        variable_name = "Dzielę"

    variable_one = logging.info('%s %s i %s', variable_name, num_one, num_two)
    
result = calculator()

