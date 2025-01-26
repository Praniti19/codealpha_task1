import random
stages = ['''
      _______
     |/      |
     |      
     |      
     |       
     |  
     |
     |___
''', ''' 
     _______
     |/      |
     |      (_)
     |      
     |       
     |  
     |
     |___

''', '''
      _______
     |/      |
     |      (_)
     |      -|-
     |       
     |    
     |
     |___
     ''', '''
     _______
     |/      |
     |      (_)
     |      -|-
     |       |
     |     
     |
     |___''', '''
      _______
     |/      |
     |      (_)
     |      -|-
     |       |
     |     || ||
     |
     |___''']
word_list = ["cereal", "terrific", "versatile"]
word = random.choice(word_list)
print(word)
lives = 0
placeholder = ""
word_length = len(word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

game_over = False
correct_letters = []

while not game_over:
    guess = input("guess a letter:\n").lower()

    display = ""

    for letter in word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    if guess not in word:
        lives = lives + 1
        if lives == 4:
            game_over = True
            print("you Lose")

    if "_" not in display:
        game_over = True
        print("you win!")

    print(stages[lives])
