import random as rand

lives = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
logo='''
888                                                           
888                                                           
888                                                           
88888b.  8888b. 88888b.  .d88b. 88888b.d88b.  8888b. 88888b.  
888 "88b    "88b888 "88bd88P"88b888 "888 "88b    "88b888 "88b 
888  888.d888888888  888888  888888  888  888.d888888888  888 
888  888888  888888  888Y88b 888888  888  888888  888888  888 
888  888"Y888888888  888 "Y88888888  888  888"Y888888888  888 
                             888                              
                        Y8b d88P                              
                         "Y88P"                               
'''
#Word bank of animals
words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()
word=rand.choice(words)
loop=True
while loop:
    display=[]
    print(word)
    lives_index=0
    word_list=[]
    for let in word:
        display.append("_")
        word_list.append(let)


    print(word_list)
    print(logo)
    while "_" in display:
        print(display)
        print(lives[lives_index])
        guessed_letter=input("Guess a letter\n").lower()
        if guessed_letter not in word:
            lives_index+=1
            if lives_index>=7:
                print("You ran out of lives.\nYou lose!!")
                break
            print(f"You guessed wrong\n"
                  f"{guessed_letter} is not in word\n"
                  f"You have {(len(lives)-1)-lives_index} lives left!")

        else:
            letter=guessed_letter
            let_ind=word_list.index(letter)
            display[let_ind]=letter
            print()
    if "_" not in display:
        print(f"You win!!\n"
              f"You had {lives_index} lives left")
    play_again=input("Play again?").lower()
    if play_again=="n" or play_again=="no":
        loop=False

