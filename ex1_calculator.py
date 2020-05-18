import re

print("Redcouz Calculator")

previous = 0
run = True

def performMath():
    global run
    global previous
    equation = ''
    if previous == 0: #<<<
        equation = input('Enter Equation (Type "Quit" if you want to finish):')
    else:
        equation = input(str(previous))
    if equation == "Quit":
        run = False
        print("Thanks for using may calculator, See you soon")
    else:
        equation = re.sub('[a-zA-Z,.:()" "]', '', equation)
        if previous == 0:
            previous = eval(equation)

        else:
            previous = eval(str(previous) + equation)

        print("Its equal to", previous)

while run:
    performMath()


