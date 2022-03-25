"""
ASSUMPTIONS OF THE PROGRAM:

The program checks the correctness of the PESEL number entered by the user and displays appropriate messages

"""


class PESEL:
    def __init__(self, nr_pesel):
        self.nr_pesel = nr_pesel

    def check(self):
        if len(self.nr_pesel) == 11 and self.nr_pesel.isdigit():
            return int(self.nr_pesel)

    def validate(self):
        scales = "1379137913"
        sum_number = 0
        for i in range(10):
            number = int(scales[i]) * int(self.nr_pesel[i])
            sum_number += number
        ver = 10 - (sum_number % 10)
        if ver == int(self.nr_pesel[10]):
            return "PESEL is correct"
        else:
            return "Error PESEL"


a = PESEL(input("Enter the PESEL number to be checked: "))
try:
    a.check()
    print(a.validate())
except ValueError and IndexError as error:
    print(f"Error 2, {error}")
