def add(a, b):
    print(f"ADDING {a}+{b}")
    return a + b

def subtract(a, b ):
    print (f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a , b ):
    print (f"MULTIPLYING {a} * {b}")
    return  a * b

def divide (a ,b ):
    print(f"DiVIDING {a} / {b}")
    return a / b


print("Let's do some math whit just functions!")

age = add(30, 5)
height = subtract (78, 4)
weight = multiply (90, 2)
iq = divide( 100, 2)

print(f" Age:{age},Height: {height}, Weight:{weight}, IQ:{iq}")


# A puzzle for the extract crediit, type it in anyway.
print("Here is a puzzle.")

what = add (age,multiply(weight,divide(iq,subtract(height,2))))


print("That becomes", what, "Can you do it by hand?")
