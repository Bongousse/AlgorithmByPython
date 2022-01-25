class LetterFilter:
    def __init__(self, s):
        self.s = s
        self.vowels = ["a", "e", "i", "o", "u"]

    # Enter your code here.
    # Complete the classes below.
    # Reading the inputs and writing the outputs are already done for you.
    #
    # class LetterFilter:
    #
    #   def __init__(self, s):
    #       self.s = s

    def filter_vowels(self):
        result = [c for c in self.s if c not in self.vowels]
        return "".join(result)

    # Enter your code here
    # Return a string

    def filter_consonants(self):
        result = [c for c in self.s if c in self.vowels]
        return "".join(result)

# Enter your code here
# Return a string

s = input()
f = LetterFilter(s)
print(f.filter_vowels())
print(f.filter_consonants())