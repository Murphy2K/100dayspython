#Step 1 
import random
word_list = ["ardvark", "baboon", "camel", "suhkruvatitupsukesekene", "elevandilondikondiluuydiuurija", "musirullikesekene", "minuarmaskiisukesekene"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

chosen_word = random.choice(word_list)
print(chosen_word)
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

guess = input("Arva täht: \n").lower()

# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
correct_guess = False  # Lisa see muutuja, et jälgida, kas kasutaja arvas õigesti.

for taht in chosen_word:
  if taht == guess:
    print("Õige")  # Prindi "Õige", kui täht on õige.
    correct_guess = True  # Märgi, et kasutaja arvas õigesti.
if not correct_guess:
  print("Vale")  # Prindi "Vale", kui kasutaja arvas valesti.

# Ülejäänud kood jääb samaks.

word_hidden = "_" * len(chosen_word)  # Muuda varjatud sõna moodustamise viis.

print(f"Word: {word_hidden}")
