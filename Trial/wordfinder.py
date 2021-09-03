"""Word Finder: finds random words from a dictionary."""
import random 
words_file = open("words.txt", "r")

class WordFinder:
    def __init__ (self, word):
        self.word = random.choice(words_file.read())
        print(f"{len(self.word)} words read")
        
    
    def random(self):
        return random.choice(self.word)






