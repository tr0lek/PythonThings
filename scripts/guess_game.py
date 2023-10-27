import random
import time
def luckset():
     global lucky
     lucky = random.randint(1,lvl) 
     guessing()


def levels():
    global lvl
    print("Type 1 for easy mode")
    print("Type 2 for medium mode")
    print("Type 3 for hard mode")
    print("Press Enter to continue")
    mode = input()
    try:
        test = (int(mode)) + 1
    except:
        print("Choose a correct mode!")
        levels()
    mode = int(mode)
    if mode == 1:
     lvl = 10 
     luckset()
    elif mode == 2:
         lvl = 100
         luckset()  
    elif mode == 3:
        lvl = 1000
        luckset()
    else:
         print("Choose a correct mode!")
         levels()  
    

def guessing():
    print("Guess a number from 1 to " + str(lvl))
    guess = input()
    try:
        test2 = (int(guess)) + 1
    except:
        print("Enter a nubmer!")
        guessing()
    guess = int(guess)
    if guess == lucky:
        win()
    else:
        if guess > lucky:
            print("Less")
            guessing()
        else:
            if guess < lucky:
                    print("More")
                    guessing()

def win():
     print("Congrats! You won.")
     time.sleep(3)

print("Hello, in this game you have to guess the correct number")
levels() 
