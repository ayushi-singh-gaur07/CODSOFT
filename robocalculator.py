#robospeaker-calculator to calculate arithmetic operation:
import win32com.client as wincom
import time
speak=wincom.Dispatch("SAPI.Spvoice")
speak.Speak("welcome to robospeaker calculator created by ayushi")
print("welcome to robospeaker calculator created by ayushi!!")
def opr():
    speak.Speak("enter the first number::")
    x =int(input("enter the first  number::"))
    speak.Speak(x)                                                                                              
    speak.Speak("enter the second number::")
    y=int(input("enter the second number::"))
    speak.Speak(y)
    return x,y
    speak.Speak(x,y)
def calculator():
    print("\nCalculator\n")
    time.sleep(1)
    print("1 - Addition")
    time.sleep(1)
    print("2 - Subtraction")
    time.sleep(1)
    print("3 - Multiplication")
    time.sleep(1)
    print("4 - Division\n")
    time.sleep(1)
    a,b=opr()
    speak.Speak("enter your choice of operation:")
    time.sleep(0)
    op=int(input("enter your choice of operation: "))
    speak.Speak(op)
    if op in (1,2,3,4,5):
        if op==1:
            speak.Speak("Addition is: ")
            print("Addition is: ",(a+b))
            speak.Speak(a+b)
        elif op==2:
            speak.Speak("Subtraction is: ",(a-b))
            print("Subtraction is: ",(a-b))
            speak.Speak(a-b)
        elif op==3:
            speak.Speak("Multiplication is:")
            print("Multiplication is: ",(a*b))
            speak.Speak(a*b)
        elif op==4:
            speak.Speak("division is:")
            print("Division is: ",(a//b))
            speak.Speak(a//b)
        elif op==5:
            speak.Speak("invalid choice")
            print("Invalid Choice ")
        calculator()
    else:
        exit(0)
calculator()

