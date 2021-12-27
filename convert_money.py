"""
ASSUMPTIONS OF THE PROGRAM:

Convert and display the entered value into US dollars or Polish zloty

CONDITIONS TO BE FULFILLED:
1. the default exchange rate can be changed

"""


def convert_to_USD():
    print("Default exchange rate is 4.12")
    exchange_rate = 4.12
    change = input("Do You wont change exchange rate? Yes/No\n")
    if change == "Yes" or change == "Y" or change == "yes" or change == "YES":
        new_rate = input("New rate: ")
        value = input("Amount to be replaced: ")
        print(f"Amount {value} to USD is {round(float(value) / float(new_rate), 2)}")
    else:
        value = input("Amount to be replaced: ")
        result = float(value) / exchange_rate
        print(f"Amount {value} to USD is {round(result, 2)}")


def convert_to_PLN():
    print("Default exchange rate is 4.12")
    exchange_rate = 4.12
    change = input("Do You wont change exchange rate? Yes/No\n")
    if change == "Yes" or change == "Y" or change == "yes" or change == "YES":
        new_rate = input("New rate: ")
        value = input("Amount to be replaced: ")
        print(f"Amount {value} to USD is {round(float(value) * float(new_rate), 2)}")
    else:
        value = input("Amount to be replaced: ")
        print(f"Amount {value} to USD is {round(float(value) * exchange_rate, 2)}")


print("""
    Welcome in Cantor. 
    Choose the option you want to perform (choose number 1 or 2)
    1. PLN to USD
    2. USD to PLN""")
choice = int(input("Your choice: "))
if choice == 1:
    convert_to_USD()
elif choice == 2:
    convert_to_PLN()
else:
    print("Wrong choice. Goodbye")
