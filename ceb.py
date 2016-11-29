import random
import string


def generate():                                                                 #genera 4 cifre, restituisce il vettore
    truth = []
    for i in range(0,4):
        truth.append(str(random.randint(0,9)))
    return truth

def check_score(stringa, inp):
    cows = 0
    bulls = 0
    for i in range(0, 4):
        if inp[i] in stringa:
            if inp[i] == stringa[i]:
                cows = cows + 1
            else:
                bulls = bulls + 1
    score = [cows, bulls]
    return score


if __name__ == "__main__" :
    vect = generate()
    string = string.join(vect, "")
    #print string
    print ("WELCOME TO COWS AND BULLS")
    inp = "0000"
    while (inp != "exit" and inp != string):
        inp = str(raw_input("try your luck > "))
        score = check_score(string,inp)
        print ("you have %d cows and %d bulls" % (score[0], score[1]))
