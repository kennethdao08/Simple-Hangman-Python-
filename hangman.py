from random import randint

WORDLIST = ["apple", "bottle", "catepillar","donkey", "explosion", 
            "friend", "gopher", "happy", "icicle", "japanese", 
            "killer", "laugh", "monster", "nose", "open", "poop",
            "quarter", "rainbow", "spicy", "television", "university",
            "version", "wallow", "xylophone", "yes", "zebra"]

LIMBS = 6

def rand_word(wordlist: list) -> str:
    index = randint(0, len(wordlist))
    return wordlist[index]

def create_guess(word: str) -> list:
    return [None for i in range(len(word))]

def grab_letter() -> str:
    run = True
    while(run):
        try:
            guess = input("Enter a letter to guess: ").strip()
            guess = int(guess)
            if type(guess) is int:
                raise ValueError

        except (ValueError):
            if type(guess) is int:
                print("Please enter a letter, try again.")
            elif len(guess) == 1:
                run = False
                break
            else:
                print("Please enter a letter, try again.")
            
    return guess.lower()

def fill_blanks(blank: list, word: str, guess: str) -> list:
    for i in range(len(word)):
        if guess == word[i]:
            blank[i] = guess
    return blank

def print_state(blanks: list) -> None:
    for char in blanks:
        if char == None:
            print("_", end= " ")
        else:
            print(char, end= " ")
    return None

def hangman(wordlist: list, limbs: int) -> None:
    word = rand_word(wordlist)
    guesses = create_guess(word)
    game_over = False
    limb_count = 0
    letter_count = 0
    while (not game_over):
        if letter_count == len(word):
            game_over = True
            break
        letter = grab_letter()
        if letter in word:
            print("Nice, you found a letter.")
            guesses = fill_blanks(guesses, word, letter)
            letter_count += 1
        else:
            print("Letter is not in the word!")
            limb_count += 1
            if limb_count == limbs:
                game_over = True
                print("You lost!")
                break
            
        
        print_state(guesses)
        print()
        print("You have {} limbs out of {} limbs.".format(limb_count, limbs))
        print()

        
    if limb_count < limbs:
        print("You won!")

    return None

'''
word = rand_word(WORDLIST)
guess = create_guess(word)

print(word)
print(guess)

print(grab_letter())
'''
hangman(WORDLIST, LIMBS)