class StringReverser:
    def __init__(self):
        self.text = ""

    def get_input(self):
        self.text = input("Enter a sentence: ")

    def reverse_words(self):
        words = self.text.split()          # split string into words
        reversed_words = words[::-1]       # reverse the list of words
        return " ".join(reversed_words)    # join back into a string

# Create object
reverser = StringReverser()
reverser.get_input()
print("Reversed string (word by word):", reverser.reverse_words())