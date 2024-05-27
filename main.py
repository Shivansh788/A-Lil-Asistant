Id = input("Enter ID : ")
PASS = input("Enter PASS : ")

if Id == "Shivansh" and PASS == "12345678":
    print("login")
else: 
    print("Wrong ID or PASS")
    exit()

# libraries import
from datetime import datetime
from AppOpener import open, close
import speech_recognition as sr
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

#little discription

Discription = '''This is mickey ai
well i am here for make your life easy
little discription about me as AI
AI refers to the development of computer systems that can perform tasks typically requiring human intelligence. 
These systems learn from data, recognize patterns, and make decisions based on algorithms. AI encompasses various subfields, 
including machine learning, natural language processing, computer vision, and robotics. 
It has applications in areas such as speech recognition, recommendation systems, autonomous vehicles, and medical diagnosis
'''


# help function (option 1 : full discription)

helping = ''' \nHere is how the ai works \n
    if you want some arithmetic work like add,sub... so on 
    just type add or sub and enter a value
    if you want to open a app
    just instruct "open app"
    Then app name
    you can also try to store result and plot graph

 '''

#Functions created
def sum(a,b):
    return a+b
def sub(a,b):
    return a-b
def multi(a,b):
    return a*b
def divide(a,b):
    try: 
        div = a/b
        return div
        raise ZeroDivisionError
    except ZeroDivisionError:
        print("you can not divide a number by zero")
def table(a,i):
    for i in range(10):
        print(a*i)

#Greatings
print("Welcome Back Sir \n How can i help you today")
print(datetime.now())


#driver code
while True:

    mode = int(input("Enter 1 for writing mode \nEnter 2 for speaking mode\n"))
    if mode == 1 :
        command1 = input("Enter a instruction you want me to execute : ")

    elif mode == 2 : #speech to text

        print("Speak funtion might not be that accurate")

        import speech_recognition as sr

        command1=""

        r = sr.Recognizer()

        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print("Recognizing...")
            command1 = r.recognize_google(audio, language='en-us')
            print(f'User said: {command1}')
        except Exception as e:
            print(e)
            print("Didn't understsand")
        pass

    else:
        print("please enter 1 or 2")
    
    command = command1

    if "help".lower() == command.lower():
        print(helping)

    elif "discription".lower() == command.lower():
        print(Discription)

    elif "open app".lower() == command.lower():
        app = input("Tell me app name : ")
        if "WhatsApp".lower() == app.lower():
            print("Opening Whatsapp")
            from AppOpener import open
            open("WhatsApp")

        elif "vs code".lower() == app.lower():
            print("Opening vs code")
            from AppOpener import open
            open("Visual Studio Code")

        elif "Telegram".lower() == app.lower():
            print("Opening Telegram")
            from AppOpener import open
            open("Telegram")

    elif "arithmetic".lower() == command.lower():
        x = int(input("Enter First number : "))
        y = int(input("Enter Second number : "))        
        operation = input("Tell me operation : ")
        if operation == "Add".lower() == operation.lower():
            print(sum(x,y))

        elif operation == "sub".lower() == command.lower():
            print(sub(x,y))

        elif operation == "Multiply".lower() == command.lower():
            print(multi(x,y))

        elif operation == "divide".lower() == command.lower():
            print(divide(x,y))

        elif operation == "table".lower() == command.lower():
            print(table(x))
        else :
            print("Error")

    elif "something crazy".lower() == command.lower():
        class QuantumCat:
            """
            A class that defies the laws of classical physics.
            It's not just a cat; it's a quantum cat!
            """

            def __init__(self, name="Schrödinger's Cat"):
                """
                Initializes our quantum cat with a mysterious name.
                """
                self.name = name
                self.alive = True

            def collapse(self):
                """
                Simulates the quantum collapse.
                """
                self.alive = not self.alive

            def observe(self):
                """
                Observes the quantum cat's state.
                """
                if self.alive:
                    return f"{self.name} is alive and dead simultaneously. 🐱🔮"
                else:
                    return f"{self.name} has collapsed into a definite state. 😿"

        # Let's create our quantum cat!
        quantum_kitty = QuantumCat()

        # Observe its mysterious existence
        print(quantum_kitty.observe())

        # Trigger the collapse
        quantum_kitty.collapse()

        # Observe again
        print(quantum_kitty.observe())

    elif "plot".lower() == command.lower():
        x = []
        y = []
        n = int(input("Enter the number of elements: "))
        print("Enter values of x")
        for i in range(n):
            ele = int(input())
            x.append(ele)
        print(x)
        print("Enter values of y")
        for i in range(n):
            ele = int(input())
            y.append(ele)
        print(y)
        
        sk = input("what you wanna plot : ")

        if sk == "line":
            # Function to plot
            plt.plot(x, y)

            # function to show the plot
            plt.show()
        elif sk == "bar":
            # Function to plot the bar
            plt.bar(x, y)
            
            # function to show the plot
            plt.show()
        elif sk == "hist":
            # Function to plot histogram
            plt.hist(y)

            # Function to show the plot
            plt.show()
        elif sk == "scatter" :
            # Function to plot scatter
            plt.scatter(x, y)

            # function to show the plot
            plt.show()

    elif "Matrix".lower() == command.lower():
        R1 = int(input("Enter the number of rows1 :"))
        C1 = int(input("Enter the number of columns1 :"))
        matrix1 = []
        print("Enter the entries rowwise:")
        for i in range(R1):
            a = []
            for j in range(C1):
                a.append(int(input()))
            matrix1.append(a)
        for i in range(R1):
            for j in range(C1):
                print(matrix1[i][j], end=" ")
            print()

        R2 = int(input("Enter the number of rows:"))
        C2 = int(input("Enter the number of columns:"))
        matrix2 = []
        print("Enter the entries rowwise:")
        for i in range(R1):
            b = []
            for j in range(C1):
                b.append(int(input()))
            matrix2.append(b)
        for i in range(R1):
            for j in range(C1):
                print(matrix2[i][j], end=" ")
            print()
        op_mat = input("Tell me operation for matrix : ")
        
        if op_mat == "Add".lower() == operation.lower():
            print(sum(matrix1,matrix2))

        elif op_mat == "sub".lower() == command.lower():
            print(sub(matrix1,matrix2))

        elif op_mat == "Multiply".lower() == command.lower():
            print(multi(matrix1,matrix2))

    elif "Store results".lower() == command.lower():
        #storing name and marks

        name_marks = {}
        num_stu = int(input("Enter the number of students you want to add: "))
        for i in range(num_stu):
            key = input("Enter Student name : ")
            value = input("Enter marks : ")
            name_marks[key] = value
        print("Your results are saved")

        #convert name_marks to excel sheet
        df = pd.DataFrame(name_marks)
        print(df)

        #to make excel file name results
        df.to_csv('results.csv')

    elif "show results".lower() == command.lower():
        #show excel
        #to read a excel file
        friends = pd.read_csv('results.csv')
        print(friends)

    elif "".lower() == command.lower():
        pass

    elif "Exit".lower() == command.lower():
        exit()

    else :
        print("Didn't support this command yet plz try again later")


