import random

# Gets a random word from words.txt
def get_wordle_word():
  # Open the words.txt file to read as f
  with open('words.txt', encoding='utf-8') as f:
    file = f.readlines() # Array of all lines for f
  
    wordle_index = random.randint(0, len(file) - 1) # Generate random index for wordle word
    return file[wordle_index].strip() # Get the word and return it with newline ('\n') removed

print(get_wordle_word()) # Test


