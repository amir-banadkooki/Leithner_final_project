import pickle
from datetime import datetime
from datetime import  timedelta
from tkinter import END  
listofcards = []

class card(object):
    def __init__(self, word, meaning , boxnumber , timeofreview):
        self.word = word
        self.meaning = meaning
        self.boxnumber = boxnumber
        self.timeofreview = timeofreview 

# Defining a function for making a list of flashcards
    def flashcard( flash , word, meaning , boxnumber , timeofreview):        
        flash.append([word, meaning , boxnumber, timeofreview])
        return flash

def new_word():
    global listofcards
    file = open('totoalcards', 'rb')
    listofcards = pickle.load(file)
    file.close()
    word = input('\n' +"Word you want to add to your Flashcards: ")
    meaning = input('\n' +"Meaning of the word in flashcard: ")
    boxnumber = 0
    timeofreview = datetime.strptime( str(datetime.now()),"%Y-%m-%d %H:%M:%S.%f")
    listofcards =  card.flashcard(listofcards, word, meaning , boxnumber , timeofreview)
    file = open('totoalcards', 'wb')
    pickle.dump(listofcards, file)
    file.close()
    file = open('totoalcards', 'rb')
    listofcards = pickle.load(file)
    file.close()
    start()
    
def practice():
    file = open('totoalcards', 'rb')
    listofcards = pickle.load(file)
    file.close()

    for ele in listofcards :
        if datetime.strptime( str(datetime.now()),"%Y-%m-%d %H:%M:%S.%f")  > ele[3] and ele[2] != 6 :
           print('\n' + ele[0])
           x = input("enter the meaning : ")
           if x == ele[1] :
                if int(ele[2]) == 0 :
                    ele[2] = 1
                    ele[3] = datetime.strptime( str(datetime.now()),"%Y-%m-%d %H:%M:%S.%f") + timedelta(seconds= 10)
                    print('\n' +"Correct!!"  +'\n' + "Now the Flashcard will be moved to next box (box number 1) ")
                elif int(ele[2]) == 1 :
                    ele[2] = 2
                    ele[3] = datetime.strptime( str(datetime.now()),"%Y-%m-%d %H:%M:%S.%f") + timedelta(seconds= 20)
                    print('\n' +"Correct!!"  +'\n' + "Now the Flashcard will be moved to next box (box number 2) ")
                elif int(ele[2]) == 2 :
                    ele[2] = 3
                    ele[3] = datetime.strptime( str(datetime.now()),"%Y-%m-%d %H:%M:%S.%f") + timedelta(seconds= 40)
                    print('\n' +"Correct!!"  +'\n' + "Now the Flashcard will be moved to next box (box number 3) ")
                elif int(ele[2]) == 3 :
                    ele[2] = 4
                    ele[3] = datetime.strptime( str(datetime.now()),"%Y-%m-%d %H:%M:%S.%f") + timedelta(seconds= 60)
                    print('\n' +"Correct!!"  +'\n' + "Now the Flashcard will be moved to next box (box number 4) ")
                elif int(ele[2]) == 4 :
                    ele[2] = 5
                    ele[3] = datetime.strptime( str(datetime.now()),"%Y-%m-%d %H:%M:%S.%f") + timedelta(seconds= 80)
                    print('\n' +"Correct!!"  +'\n' + "Now the Flashcard will be moved to next box (box number 5) ")
                elif int(ele[2]) == 5 :
                    ele[2] = 6
                    ele[3] = datetime.strptime( str(datetime.now()),"%Y-%m-%d %H:%M:%S.%f") + timedelta(seconds= 10)
                    print('\n' + "congratulations!!!!!" + '\n' + "you have memorised this Word!!!!' "+'\n')
           else:
             ele[2] = 0
             ele[3] = datetime.strptime( str(datetime.now()),"%Y-%m-%d %H:%M:%S.%f")
             print('\n' +"wrong!! Now the Flashcard will be moved to first box "  )
    else :
        print('\n' + "No more Words to review for now! come back later ;) " )      
  
    file = open('totoalcards', 'wb')
    pickle.dump(listofcards, file)
    file.close()
    file = open('totoalcards', 'rb')
    listofcards = pickle.load(file)
    file.close()
    start()
    
def start():
    z= input('\n' + "to add a new word type:' new ' to practice , type ' p '  and to quit type: 'q': " )
    if z == 'new' :
        new_word()
    elif z == 'p' :
        practice()
    elif z=='q' :
        print('\n' + "see you next time ;)" + '\n')
        END
    else:
        start()

start()
