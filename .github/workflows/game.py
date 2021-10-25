from random import shuffle  
example = [1,2,3,4,5,6,7]
shuffle(example)
example

def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

result = shuffle_list(example)
result

mylist = ['O', '', '']

shuffle_list(mylist)

def player_guess():
    guess = ''
    while guess not in ['0','1','2']:
        guess = input("Pick a number:0,1,2")
        
    return int(guess)

player_guess()

myindex = player_guess()

myindex

def check_guess(mylist, guess):
    if mylist[guess] == 'O':
        print("correct")
    else:
        print("Wrong guess!")


#INTITAL LIST
mylist = [ '','O', '']
#SHUFFLE LIST
mixedup_list = shuffle_list(mylist)
#USER GUESS
guess = player_guess()
#CHECK GUESS
check_guess(mixedup_list,guess)
    