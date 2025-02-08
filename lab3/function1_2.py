#Read in a Fahrenheit temperature. Calculate and display the equivalent centigrade temperature. The following formula is used for the conversion: C = (5 / 9) * (F – 32)
def fahrenheitToCelsius(f):
    c = (5 / 9) * (f - 32)
    return c

f = float(input("Enter Fahrenheits: "))
print("It's", fahrenheitToCelsius(f), "celsius")