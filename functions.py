# COGS18 Final Project: ChatBot
## Alessandra Torres-Rojas
#My code ChatBot asks you a variety of questions to which you will type in the input specified in the docstrings (text in red) at the top of each function and press Enter. After you type in this input you will receive a different output for each question asked. This code is extremely simple and easy to use. I hope you find the process of using this code to be simple. Thank you to Professor Ellis and all the TA's for all their hardwork and for helping me on my final project as well as previous assignments. This has been a true learning experience.

'''Asks for your name, you will type in Aless as the name required, if you input anything else it will return Try Again'''
def question():
    stop = False
    print("\nFirst question:")
    while stop == False:
        inputStr = input("whats your name?")
        if(inputStr == "Aless"):
            print("Hi Aless!")
            stop = True
        else:
            print("\nTry again")
    print(inputStr)
    question()
    return True
    
'''Asks you how you're doing, you will type in Good as the input, if you input anything else it will return Try Again'''
def newquestion():
    stop = False
    print("\nSecond question:")
    while stop == False:
        inputStr = input("How are you doing today?")
        if(inputStr == "Good"):
            print("I'm glad to hear that!")
            stop = True
        else:
            print("\nTry again")
    print(inputStr)
    newquestion()
    
'''Asks if you have finished your final project yet, you will type in No as the input, if you input anything else it will return Try Again'''
def project():
    stop = False
    print("\nThird question:")
    while stop == False:
        inputStr = input("Have you finished your COGS 18 final project?")
        if(inputStr == "No"):
            print("Get to work on it!")
            stop = True
        else:
            print("\nTry again.")
    print(inputStr)
    project()
    
'''Asks if you've been practicing self care, you will type in No as the input, if you input anything else it will return Try Again'''
def selfcare():
    stop = False
    print("\nFourth question:")
    while stop == False:
        inputStr = input("Have you been practicing self-care?")
        if(inputStr == "No"):
            print("Oh no, remember to drink water, sleep, and eat!")
            stop = True
        else:
            print("\nTry again.")
    print(inputStr)
    selfcare()
    
'''Asks if you like this class, you will type in No as the input, if you input anything else it will return Try Again'''
def feedback():
    stop = False
    print("\nFifth question:")
    while stop == False:
        inputStr = input("Did you like this class?")
        if(inputStr == "No"):
            print("I'm sorry to hear that.")
            stop = True
        else:
            print("\nTry again")
    print(inputStr)
    feedback()
    
'''Asks how this class can improve, you will type in Provide more help! as the input, if you input anything else it will return Try Again'''
def improvement():
    stop = False
    print("\nSixth question:")
    while stop == False:
        inputStr = input("How can this class improve?")
        if(inputStr == "Provide more help!"):
            print("Thank you for your feedback.")
            stop = True
        else:
            print("\nTry again")
    print(inputStr)
    improvement()
    
'''Asks if you'll be taking another COGS class, you will type in No as the input, if you input anything else it will return Try Again'''
def again():
    stop = False
    print("\nSeventh question:")
    while stop == False:
        inputStr = input("Will you be taking another COGS class?")
        if(inputStr == "I don't think so."):
            print("Aw man! Have a great Winter break!")
            stop = True
        else:
            print("\nTry again")
    print(inputStr)
    again()