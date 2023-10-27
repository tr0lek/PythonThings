import random
import time
def luckset():
     global lucky
     lucky = random.randint(1,lvl) 
     guessing()


def levels():
    global lvl
    print("Wpisz 1 dla poziomu łatwego")
    print("Wpisz 2 dla poziomu średniego")
    print("Wpisz 3 dla poziomu trudnego")
    print("Naciśnij enter aby potwierdzić")
    mode = input()
    try:
        test = (int(mode)) + 1
    except:
        print("Wybierz poprawny tryb!")
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
         print("Wybierz poprawny tryb!")
         levels()  
    

def guessing():
    print("Podaj numer od 0 do " + str(lvl))
    guess = input()
    try:
        test2 = (int(guess)) + 1
    except:
        print("Podaj liczbe!")
        guessing()
    guess = int(guess)
    if guess == lucky:
        win()
    else:
        if guess > lucky:
            print("Niżej")
            guessing()
        else:
            if guess < lucky:
                    print("Wyżej")
                    guessing()

def win():
     print("Brawo, zgadłeś numer!")
     time.sleep(3)

print("Witaj, w tej grze musisz odgadnąć losowy numer w wybranym przedziale")
levels() 