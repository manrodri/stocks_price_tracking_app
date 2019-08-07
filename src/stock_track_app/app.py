# todo ci setup: jenkins pipeline. Build, test, deploy.
# todo tests
# todo error handling
# todo oo desing
# todo gui
# todo use a db
# todo implement add_new_list and change track function to take multiple lists


import pandas_datareader as pdr
from time import sleep

symbols = "AMZN GOOG NFLX FB GLD SPY".split()
options = \
    "Track Default List, Show Default List, Add to Default, Edit Default List, Add new List, Quit"\
        .split(", ")


def show_default(lst=symbols):
    lst.sort()
    return symbols

def add_to_default(symbols):
    symbol = input("enter a symbol: ")
    while symbol != "":
        '''Error checking for symbol here'''
        symbols.append(symbol.upper())
        print("Added {} to Default list".format(symbols[-1]))
        symbol = input("enter symbol to add or hit enter to quit")

def edit_default():
    print("Select symbol to delete:")
    for i in range(len(symbols)):
        print("{} - {}".format(i, symbols[i]))
    removed = symbols.pop(int(input()))
    print("{} removed".format(removed))

def add_list(lists_dict):
    name = input("Enter new list name: ")
    new_list = list
    print("Enter symbol to add: ")
    symbol = input().upper()
    while symbols != "":
        new_list.append(symbol)
        print("Enter symbol to add or hit enter to finish")
        symbol = input().upper()
    return new_list

def get_prices(symbols):
    symbols.sort()
    return pdr.get_quote_yahoo(symbols)['price']


def main():
    lists = {}
    run_program = True;


    while run_program:
        print("Choose options:")
        for i in range(len(options)):
            print("{} - {}".format(i, options[i]))
        choice = int(input())
        if choice == 0:
            while True:
                print(get_prices(symbols))
                print('CNTL + C to quit')
                sleep(5)
        elif choice ==1:
            print(show_default(symbols))
        elif choice == 2:
            add_to_default(symbols)
        elif choice == 3:
            edit_default()
        elif choice == 4:
            pass
            #add_list()
        elif choice == 5:
            run_program = False

if __name__ == "__main__":
   main()




