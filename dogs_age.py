"""
ASSUMPTIONS OF THE PROGRAM:

Calculated the age of the dog by human age

CONDITIONS TO BE FULFILLED:
1. for the first two years, each year of a dog's life is equal to 10.5 human years
2. over two years, each year of a dog's life is 4 human years,

"""


def dog_age(age: float):
    if age > 0:
        if age <= 2:
            return f"{name_dog} have {age * 10.5} human years"
        else:
            return f"{name_dog} have {(2*10.5)+((age-2)*4)} human years"
    else:
        return "Age age cannot be negative"


name_dog = input("Dog's name: ")
dogs_years = input(f"Years {name_dog}: ")
try:
    dogs_years = float(dogs_years)
    print(dog_age(dogs_years))
except TypeError and ValueError as error:
    print(f"Wrong type input value, {error}")

