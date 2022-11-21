import random
#from collections import Counter
 
someWords = '''apple banana mango strawberry
orange grape pineapple apricot lemon coconut watermelon
cherry papaya berry peach lychee muskmelon''' # string of all words
 
someWords = someWords.split(' ') # created list out of string

word = random.choice(someWords)  # choosing random word from someWords
print(word)

for i in word: # for every char in word we are printing _
    print('_', end = ' ')    
    
print() # for new line
counter= len(word)+2 # set counter of chances
list=[] # list for correct words
for x in range(counter): # chances by loop on counter
    print("guess your ", x+1,"letter") 
    y= input() # I am taking guessed input of character from player
    if y in word: # checking if guessed alphabet is in word
        list.append(y) # saving that alpabet in list
        a=0 # counter for all words are guessed or not
        for j in word: #loop on word, to print guessed word or _
            if j in list: 
                print(j, end=' ')
            else:
                a=1
                print('_',end=' ')
        if(a==0): 
            print()
            print("YOU WON")
            break
    print()
else: # if all chances taken and still loop is not broken then player lost
    print("YOU LOST")
























import random
#from collections import Counter
 
someWords = '''apple banana mango strawberry
orange grape pineapple apricot lemon coconut watermelon
cherry papaya berry peach lychee muskmelon''' # string of all words
 
someWords = someWords.split(' ') # created list out of string

word = random.choice(someWords)  # choosing random word from someWords
print(word)

for i in word: # for every char in word we are printing _
    print('_', end = ' ')    
    
print() # for new line
counter= len(word)+2 # set counter of chances
list=[] # list for correct words
x=0
while x<counter: # chances by loop on counter
    print("guess your ", x+1,"letter") 
    y= input() # I am taking guessed input of character from player
    if y.isalpha():
        x=x+1
        if y in word: # checking if guessed alphabet is in word
            list.append(y) # saving that alpabet in list
            a=0 # counter for all words are guessed or not
            for j in word: #loop on word, to print guessed word or _
                if j in list: 
                    print(j, end=' ')
                else:
                    a=1