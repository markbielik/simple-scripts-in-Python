"""
ASSUMPTIONS OF THE PROGRAM:

Calculate and display the multiplication table for any integer

"""


def multiplication_table(number):
    """

    :param number: input string and convert to integer
    :return: multiplication action (string)
    """
    try:
        number = int(number)
        print(f"\nMultiplication table for number {number}")
        for x in range(1, 11):
            print(f"{x} * {number} = {x*number}")
    except ValueError as error:
        print("You entered a wrong value ", error)


print("""
    Welcome
    You are in the multiplication tables program
    You can enter any integer and get multiplication results from 1 to 10\n""")
user_number = input("Enter your number: ")
multiplication_table(user_number)
