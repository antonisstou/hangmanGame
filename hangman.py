# Antonis Stournaras


def printhanger (tries,maxtries):
    if tries==5:
        print("+-----+")
        print("|")
        print("|")
        print("|")
    elif tries==4:
        print("+-----+")
        print("|     O")
        print("|")
        print("|")
    elif tries==3:
        print("+-----+")
        print("|     O")
        print("|   --+")
        print("|")
    elif tries==2:
        print("+-----+")
        print("|     O")
        print("|   --+--")
        print("|")
    elif tries==1:
        print("+-----+")
        print("|     O")
        print("|   --+--")
        print("|    /")
    elif tries==0:
        print("+-----+")
        print("|     O")
        print("|   --+--")
        print("|    / \ ")       

print("Welcome to KREMALA")
Game="New"
while Game=="New":
    player=input("Type g<Enter> or G<Enter> if word will be given by another player: ")
    f=open("words.txt")
    words=f.read()
    if (player=="g") or (player=="G"):
        word=input("Player don't look! 2nd player, type in word, must be in English and at least 3 letters long:").lower()
        while (len(word)<3) or (len(word)>20):
            word=input("Word is either too short or too long.Please enter another word:").lower()
        while (word not in words):
            word=input("This word can't be used")
        print(50*"\n")
    else:
        choice=(input('Type "R" or "r" if you want a word of random length,else give the length of the random word(min 3,max20):'))
        if (choice=="r")or(choice=="R"):
            import random
            lines =open("words.txt").read().splitlines()
            word=random.choice(lines)
        else:
            try:
                length=int(input("Give the length of the word between 3 and 20:"))
                while (length<3) or (length>20) :
                     length=int(input("Wrong number.Give the length of the word between 3 and 20:"))
            except  ValueError:
                 print("Not valid answer.")
            wordlength=0
            while (length!=wordlength):
                import random                                       
                lines=open("words.txt").read().splitlines()
                word=random.choice(lines)
                wordlength=len(word)
    word=word.upper()
    Solution=list(word)
    Answer=[]
    for i in range(0,len(Solution)):
        Answer.append("_")
    UsedLetters=[]
    tries=5
    maxtries=5
    printhanger(tries,maxtries) 
    print(''.join(Answer))
    print(tries,"tries left")
    print(UsedLetters)
    while tries!=0 and (Answer!=Solution):
        try:
            letter=input("Give a letter:").upper()
            while (len(letter)>1) or letter=="" or letter not in 'qwertyuioplkjhgfdsazxcvbnm'.upper() :
                letter=input("Not valid answer.Give a letter:").upper()
        except ValueError:
            print("Not valid answer")
       # letter=letter.upper()
        if letter in UsedLetters:
            print("You already used this letter")
            printhanger(tries,maxtries)
            print(''.join(Answer))
            print(tries,"tries left")
            print(UsedLetters)
        else:
            UsedLetters.append(letter)
            Found=False
            for i in range (0,len(Solution)):
                if Solution[i]==letter:
                    Answer[i]=Solution[i]
                    Found=True
            if Found==True:
                print("Guess letter:",letter)
                printhanger(tries,maxtries)
                print(''.join(Answer))
                print(tries,"tries left")
                print(UsedLetters)
            else:
                tries=tries-1
                print("Guess letter:",letter)
                printhanger(tries,maxtries)
                print(''.join(Answer))
                print(tries,"tries left")
                print(UsedLetters)
    if tries==0:
        print("Sorry! You lost ! The word was ",word)
    elif Answer==Solution:
        print("Congratulations!You found word",word)
    PlayAgain=input("Do you want to play again?")
    PlayAgain=PlayAgain.upper()      
    if PlayAgain!="YES":
        Game="Exit"
        print("The game will now exit.")