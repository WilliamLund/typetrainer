from random import randint
from colorama import Fore, Back, Style,init
import time
init(autoreset=True)

ord=["humor","magenta","vacation","wet","erratic","kindly","shape","accept","helpful","dark","demand","refund","iron","concentrate","dismiss","add","liver","arise","architect","identification","cash","pension","bowel","dismissal","drag","resignation","ghostwriter","suffering","instal","dialogue"]

text=["The ants enjoyed the barbecue more than the family.","I'd always thought lightning was something only I could see.","He didn't heed the warning and it had turned out surprisingly well.","I met an interesting turtle while the song on the radio blasted away.","He stepped gingerly onto the bridge knowing that enchantment awaited on the other side."]

left=['q','w','e','a','s','d','z','x','c','r','f','v','t','g']

right=['y','u','i','o','p','h','j','k','l','b','n','m']

lrb={"l":"Left","r":"Right","b":"Both"}

options ={"w":"Words", "s":"Sentences","l":"Letters","h":"Show Highscores","q":"quit"}

tryAgain={"t":"Try Again","h":"Add High Score", "q":"Quit"}

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
    return("WPM: "+str(int((length/result)+0.5)))

def optionsScreen():
    mode=menu("Select gamemode","\nMode: ",options)
    
    if mode =="s":
        startSentenceGame(text[randint(0,len(text)-1)])
    elif mode =="w":
        startWordGame()
    elif mode=="l":
        startLettersGame()
    elif mode=="h":
        showHighScore(highScore)

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
            wpm=(results(start,10))
            print (wpm)
            choice=menu("Do you want to try again?","\nOptions: ",tryAgain)
            if choice =="t":
                startWordGame()
            elif choice =="h":
                addHighScore(wpm)
                showHighScore(highScore)
                
            

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
            wpm=results(start,length)
            print (wpm)
            
            if antalOrd==length:
                print("\n Congratulations you got everything correct!")
            else:
                print("\n You got "+str(antalOrd)+"/"+str(length)+" correct! Keep practicing!")
            choice =menu("Do you want to try again?","\nOptions: ",tryAgain)
            if choice =="t":
                startSentenceGame(text[randint(0,len(text)-1)])
            elif choice=="h" and antalOrd==length:
                addHighScore(wpm)
                showHighScore(highScore)
            elif choice=="h":
                print("You can only add your score if you got all words correct")
                optionsScreen()
            
                
def startLettersGame():
    mode=menu("Select Keyboardside","\nSide: ",lrb)
    
    if mode=="l":
        leftGame()
    elif mode=="r":
        rightGame()
    elif mode=="b":
        bothGame()
    
def leftGame():
    
    for i in range(0,10):
        let=""
        for x in range(0,3):
            let += left[randint(0,13)]
        print(let)
        userLet = input("Write Here: ")
        if not userLet == let:
            print("Game Over!")
            optionsScreen()
            return ""
    print("Congratulations you Won!")
    
    optionsScreen()
    
def rightGame():
    for i in range(0,10):
        let=""
        for x in range(0,3):
            let += right[randint(0,12)]
        print(let)
        userLet = input("Write Here: ")
        if not userLet == let:
            print("Game Over!")
            optionsScreen()
            return ""
    print("Congratulations you Won!")
    
    optionsScreen()
    
    
def bothGame():
    for i in range(0,10):
        let=""
        
        for x in range(0,3):
            if randint(0,1) ==0:
                let += left[randint(0,13)]
            else:
                let += right[randint(0,12)]
            
            
           
        print(let)
        userLet = input("Write Here: ")
        
        if not userLet == let:
            print("Game Over!")
            optionsScreen()
            return ""
    print("Congratulations you Won!")
    
    optionsScreen()
    
def startScreen():
    print("--------------------")
    print()
    print()
    print(Fore.BLUE+"    TypeTrainer")
    print()
    print()
    print("--------------------")
    print()
    input("Press enter to start the game\n")

    optionsScreen()
    

        
       
def addHighScore(wpm):
    name= input("What your name? ")
    
    highScore[name]= wpm
    
       
def showHighScore(score):
    i=1
    f=sorted(score.items(),reverse=True,key=lambda x:x[1])
    
    print("\n"+"\u0332".join("HIGHSCORE ")+"\n")
    
    for a,b in f:
        print(str(i)+": "+str(a)+" "+str(b))
        i+=1
    print()
    
    optionsScreen()
    
       

#startScreen()
addHighScore(24)
addHighScore(38)
showHighScore(highScore)

