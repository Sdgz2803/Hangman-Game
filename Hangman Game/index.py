from urllib.request import Request, urlopen
import random

def fetch_random_word(url):
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    web_byte = urlopen(req).read()
    webpage = web_byte.decode('utf-8')
    word_list = webpage.split("\n")
    return random.choice(word_list).strip()

def display_hangman(tries):
    HANGMAN_PICS = [
        '''
           +---+
               |
               |
               |
              ===
        ''', 
        '''
            +---+
            O   |
                |
                |
               ===
        ''', 
        '''
            +---+
            O   |
            |   |
                |
               ===
        ''',
        '''
            +---+
            O   |
           /|   |
                |
               ===
        ''', 
        '''
            +---+
            O   |
           /|\  |
                |
               ===
        ''', 
        '''
            +---+
            O   |
           /|\  |
           /    |
               ===
        ''', 
        '''
            +---+
            O   |
           /|\  |
           / \  |
               ===
        ''']
    return HANGMAN_PICS[min(tries, len(HANGMAN_PICS) - 1)]

def get_valid_input():
    while True:
        guess = input("Enter one letter: ").lower()
        if len(guess) == 1 and guess.isalpha():
            return guess
        print("Invalid input. Please enter a single letter.")

def play_hangman():
    url = "https://svnweb.freebsd.org/csrg/share/dict/words?revision=61569&view=co"
    random_word = fetch_random_word(url).lower()
    guessed_letters = set()
    correct_letters = set(random_word)
    tries = 0
    max_tries = len(display_hangman(0)) - 1
    word_display = ["_" if letter.isalpha() else letter for letter in random_word]

    print("THIS IS THE HANGMAN GAME")
    print(f"The word that you have to guess has {len(random_word)} letters")
    print("START GUESSING!!!!")

    while tries < max_tries:
        print(display_hangman(tries))
        print("Current word: " + " ".join(word_display))
        guess = get_valid_input()

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in correct_letters:
            print("Good guess!")
            for i, letter in enumerate(random_word):
                if letter == guess:
                    word_display[i] = guess
            if "_" not in word_display:
                print("Congratulations! You won!")
                print("The word was: " + random_word)
                break
        else:
            print("Wrong guess.")
            tries += 1

    if tries == max_tries:
        print(display_hangman(tries))
        print("Sorry, you lost! The word was: " + random_word)

if __name__ == "__main__":
    play_hangman()
