import random
hangman =['''
+----+
  |  |
  O  |
 /|\ |
 / \ |
     |
=======    
''','''
+----+
  |  |
  O  |
 /|\ |
 /   |
     |
=======
''','''
+----+
  |  |
  O  |
 /|\ |
     |
     |
=======
''','''
+----+
  |  |
  O  |
 /|  |
     |
     |
=======
''','''
+----+
  |  |
  O  |
  |  |
     |
     |
=======
''','''
+----+
  |  |
  O  |
     |
     |
     |
=======
''','''
+----+
  |  |
     |
     |
     |
     |
=======
''']

with open("fruits.txt","r") as f:
    words=f.read().splitlines()
word=random.choice(words).lower()

print("\n---------------Hangman Game-Fruits Edition---------------\n\n")
print('''
Rules to guess the word:

1.Input single letter in one turn.
2.Don't use repeated letters.
3.Turns will be decremented after every guess.
''')
lives=6
guess=[]
done=False
print("Guess the word:")
while not done:
    for letter in word:
        if letter.lower() in guess:
            print(letter,end=" ")
        else:
            print("_",end=" ")
    print(" ")
    g=input(f"{hangman[lives]}\nEnter the guess:")
    guess.append(g.lower())
    if g.lower() not in word.lower():
        lives-=1
        if lives==0:
            print(hangman[0])
            break

    done=True
    for letter in word:
        if letter.lower() not in guess:
            done=False

if done:
    for letter in word:
        print(letter,end=" ")
    print(hangman[lives])
    print(f"You found the word! It is {word}.")
    
else:
    print(f"The word was {word}.\nBetter luck next time!")
