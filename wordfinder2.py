"""Word Finder: finds random words from a dictionary."""
import random 

class WordFinder:
    def __init__ (self, word):
        words_file = open("words.txt", "r")
        self.word = self.parse(words_file)
        print(f"{len(self.word)} words read")

    def parse(self, words_file):
        return [w.strip() for w in words_file]

    def random(self):
        return random.choice(self.word)
        
class SpecialWordFinder:
    def parse(self, words_file):
        return [w.strip() for w in words_file
        if w.strip() and not w.startswith("#")]    






