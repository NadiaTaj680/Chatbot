import random

def hangman():
    words = ['python','web','developer','computer']

    word=random.choice(words)
    word_length= len(word)
    guess_word= ["_"] * word_length
    guess_letters=[]
    lives= 4

    print("WELCOME TO THE GAME!")
    print("Enter any letter one at a time")
    print(f"You have {lives} chances to guess a word")
    print("".join(guess_word))

    while lives > 0:
        guess = input("Enter a letter.").lower()

        if len(guess)!=1 or not guess.isalpha():
            print("Not allowed,you can enter one letter at a time.")
            continue

        if guess in guess_letters:
            print("You already guessed,try another letter.")
            continue
        
        if len(guess_letters)==len(guess_word):
            break
        else:
            guess_letters.append(guess)


        if guess in word:
            print(f"Great! {guess} is in the word.")
            for index,letter in enumerate(word):
                if letter==guess:
                    guess_word[index]= guess
                    
        else:
            lives-=1
            print("Wrong Guess!!")
            print(f"You have {lives} chances to win.")

           # Display the current state

    if lives ==0 or len(guess_letters)==len(guess_word):
        print("WORD:","".join(word))
        print("Chances:",lives)
        print("Guess Letter :","".join(guess_letters))

        
    if "_" not in guess_word:
        print("CONGRATES YOU GUESS THE WORD", word)

    else:
        print("YOU LOSS! CHANCES ARE OVER.")

hangman()
        











