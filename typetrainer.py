from random import randint
from colorama import Fore, Back, Style,init
import time
init(autoreset=True)

ord=["humor","magenta","vacation","wet","erratic","kindly","shape","accept","helpful","dark","demand","refund","iron","concentrate","dismiss","add","liver","arise","architect","identification","cash","pension","bowel","dismissal","drag","resignation","ghostwriter","suffering","instal","dialogue"]
text=["The ants enjoyed the barbecue more than the family.","I'd always thought lightning was something only I could see.","He didn't heed the warning and it had turned out surprisingly well.","I met an interesting turtle while the song on the radio blasted away.","He stepped gingerly onto the bridge knowing that enchantment awaited on the other side."]
options ={"w":"Words", "s":"Sentences","q":"quit"}
tryAgain={"t":"Try Again", "q":"Quit"}
highScore={}


def menu(title, prompt, options):
    print (title+"\n")
    for x in options:
        print(" "+x+") "+options[x])
    a = input(prompt)
    while not a in options:
        a = input(prompt)
    return a
    print("You selected option "+a+") "+options[a])

def comp(ord1):
    print("\n Write "+Fore.BLUE+ ord1+"\n")
    ord2=input("Write here: ")
    
    if ord1==ord2:
        return True
    else:
        return False

def results(start,length):
    
    stop = time.time()
    result = (stop-start)/60
    return("WPM: "+str(int(length/result)))
    
    
def startWordGame():
    start =time.time()
    i=0
    length=len(ord)
   
         
    for x in range(1,11):
        
        i=randint(0,length-x)
        while comp(ord[i]) ==False:
            print("\n"+Fore.RED+"Wrong!\n")
            
            
            
        del ord[i]
        if len(ord)==length-10:
            print (results(start,length))
            if menu("Do you want to try again?","\nOptions: ",tryAgain) =="t":
                startWordGame()
            

def startSentenceGame(sentence):
    
    start =time.time()
    i=0
    print("\n"+sentence+"\n")
    inputText=input("Write here: ")
    inputText = inputText.split(" ")
    
    wordSentence = sentence.split(" ")
    length=len(wordSentence)
    antalOrd=length
    
    for x in wordSentence:
        if not len(inputText) == length:
            print("The amount of words you wrote, does not match the amount of words in the sentence")
            
            return False
        
        if not x == inputText[i]:
            antalOrd -=1
            
        i+=1
        if i==length:
            print (results(start,length))
            
            if antalOrd==length:
                print("\n Congratulations you got everything correct!")
            else:
                print("\n You got "+str(antalOrd)+"/"+str(length)+" correct! Keep practicing!")
            
            if menu("Do you want to try again?","\nOptions: ",tryAgain)=="t":
                
                startSentenceGame(text[randint(0,len(text)-1)])
                

def startScreen():
    print("--------------------")
    print()
    print()
    print("    TypeTrainer")
    print()
    print()
    print("--------------------")
    print()
    input("Press enter to start the game\n")

    mode=menu("Select gamemode","\nMode: ",options)
    
    if mode =="s":
        startSentenceGame(text[randint(0,len(text)-1)])
    elif mode =="w":
        startWordGame()
        
def addHighScore(wpm):
    name= input("What your name?")
    
    highScore[name]= wpm
    
    
    
    
def showHighScore(score):
    i=1
    f=sorted(score.items())
    for a,b in f:
        print(str(i)+": "+str(a)+" WPM: "+str(b))
    
   
    
#addHighScore(50)
#showHighScore(highScore)
startScreen()



