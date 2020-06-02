# Stanley Mohr
# 6/2/20
# Game for rock paper scissors

import random

computer_moves_list = ['rock', 'paper', 'scissors']
computer_selected_move = random.choice(computer_moves_list)
user_move_dict = {1: 'rock', 2: 'paper', 3: 'scissors'}

# debug print
print(computer_selected_move)

print("Lets play!")
print("Whisper to me what move you want to make.")
print("1) Rock")
print("2) Paper")
print("3) Scissors")
user_selected_move = (int(input()) - 1)


if 0 <= user_selected_move < 3:
    var = computer_moves_list[user_selected_move] in user_move_dict.values()
    print(var)
else:
    print('That is not a choice!')
    
