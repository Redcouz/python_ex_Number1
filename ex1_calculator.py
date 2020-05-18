import re

print("Redcouz Calculator")

previous = 0
run = True

def performMath():
    global run
    global previous
    equation = ''
    if previous == 0: #<<< Make sure thats starts at the first equation >>>
        
        equation = input('Enter Equation (Type "Quit" if you want to finish):')
        
    else: #<<< Sum to the previous result >>>
        
        equation = input(str(previous))
        
    if equation == "Quit": #<<< Ends the script >>>
        
        run = False
        print("Thanks for using may calculator, See you soon")
        
    else: 
        
        equation = re.sub('[a-zA-Z,.:()" "]', '', equation) #<<< Delete everything that is not a number >>>
        if previous == 0:
            
            previous = eval(equation)

        else:
            
            previous = eval(str(previous) + equation)

        print("Its equal to", previous) #<<< Outcome >>>

while run:
    performMath()


