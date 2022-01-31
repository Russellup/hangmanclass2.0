import random

class HangmanGame:
    
    def __init__(self):
        self.wl = 'garrapolo, rice, williams, kittle '.split(', ') # wordlist
        self.rw = None #randomword
        self.hm = None # hangman
        self.t  = 1 # turns

    def start(self):
        self.rw = random.choice(self.wl)
        self.hm = len(self.rw)*['_']

    def is_running(self):
        return True if '_' in self.hm else False
    