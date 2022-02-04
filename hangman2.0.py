import random

class HangmanGame:
    
    def __init__(self):
        self.wordlist = 'garrapolo, rice, williams, kittle '.split(', ') 
        self.randomword = None 
        self.hangman = None 
        self.turns  = 1 

    def start(self):
        self.randomword = random.choice(self.wordlist)
        self.hangman = len(self.randomword)*['_']

    def is_running(self):
        return True if '_' in self.hangman else False

    def show_all(self):
        if '_' in self.hangman:
            print('\nHangmanGame: {}\nturns: {}\n'.format(' '.join(self.hangman), self.turns))
        else:
            print('\nHangmanGame Completed!: {}\nturns: {}\n'.format(''.join(self.hangman), self.turns))
        print('---------------------------------------------------')

    def compare(self, guess):
        for i, char in enumerate(self.randomword):
            if guess == char:
                self.hangman[i] = char
        self.turns +=1

game = HangmanGame()
game.start()

while game.is_running():
    game.show_all()
    game.compare(input("Guess: "))
   
game.show_all()
    
