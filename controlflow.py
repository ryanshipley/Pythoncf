# Task 1 Vowel or Consonant?
# Requirements: 
# 1. Promt the user to enter a letter in the alphabet(a-z or A-Z).
# 2. Determine whether the letter entered is a vowel.
# 3. Print out one fo two messages, is a vowel or isnt a vowel.
vowel = ['A', 'E', 'I', 'O', 'U'] #Created a table of all vowels.
#We create a variable input that will be an uppercase letter.
input = input('Enter a letter within A-Z: ').upper()

# If the input is in the vowel array, then we say its a vowel.
# If the input is 'Y' we have a special message for it.
# If the input is not in the array and its not 'Y' then it is a consonant.
if input in vowel :
    print(f'The chosen letter {input} is a vowel')

elif input == 'Y':
    print(f'The chosen letter {input} is special')

else: 
    print(f'the letter {input} is a consonant, not a vowel')