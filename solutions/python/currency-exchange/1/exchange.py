
def exchange_money(budget, exchange_rate):
    # returns converted currency
    # exchange_rate = amount of currency equal to foreign currency
    return float(budget / exchange_rate)

def get_change(budget, exchanging_value):
    # exchanging value = 'tax', kind of
    return budget - exchanging_value

def get_value_of_bills(denomination, number_of_bills):
    # denomination = value of bill
    return denomination * number_of_bills

def get_number_of_bills(amount, denomination):    
    return amount // denomination

def get_leftover_of_bills(amount, denomination):
    return amount % denomination

def exchangeable_value(budget, exchange_rate, spread, denomination):
    # spread = percentage taken as fee
    new_rate = exchange_rate + (exchange_rate * (spread / 100)) 
    total_new_currency = exchange_money(budget, new_rate)
    bill_value_new_currency = int(total_new_currency / denomination)
    maximun_value_new_currency = bill_value_new_currency * denomination
    return maximun_value_new_currency