# Stanley Mohr
# 6/2/20
# Game for rock paper scissors

import random

computer_moves_list = ['rock', 'paper', 'scissors']
user_move_dict = {0: 'rock', 1: 'paper', 2: 'scissors'}

print("Lets play!")


def game():
    computer_selected_move = random.choice(computer_moves_list)
    # debug print
    # print("DEBUG:" + str(computer_selected_move))
    print("\nWhisper to me what move you want to make.")
    print("1) Rock")
    print("2) Paper")
    print("3) Scissors")
    my_input = input()
    user_selected_move = (int(my_input) - 1)

    # debug
    # print(user_selected_move)

    if user_selected_move in user_move_dict.keys():
        print(str.upper(user_move_dict[user_selected_move]) + "--" + str.upper(computer_selected_move))
        if user_move_dict[user_selected_move] == computer_selected_move:
            print("A draw!")
            replay()
        # user selects rock
        elif user_selected_move == 0 and computer_selected_move == computer_moves_list[1]:
            # user rock and computer paper
            print("Paper covers rock! You lose!")
            replay()
        elif user_selected_move == 0 and computer_selected_move == computer_moves_list[2]:
            # user rock and computer scissors
            print("Rock beats scissors! You win!")
            replay()
        elif user_selected_move == 1 and computer_selected_move == computer_moves_list[0]:
            # user paper and computer rock
            print("Paper covers rock! You win!")
            replay()
        elif user_selected_move == 1 and computer_selected_move == computer_moves_list[2]:
            # user paper and computer scissors
            print("Scissors cut paper! You lose!")
            replay()
        elif user_selected_move == 2 and computer_selected_move == computer_moves_list[0]:
            # user scissors and computer rock
            print("Rock beats scissors! You lose!")
            replay()
        elif user_selected_move == 2 and computer_selected_move == computer_moves_list[1]:
            # user scissors and computer paper
            print("Scissors cut paper! You win!")
            replay()
    else:
        print("That's not a choice! I tried hard to set this game up, just 1-3 got it? (y/n)")
        force_replay()


def replay():
    print("Play again!? (y/n)")
    user_again = input()
    if user_again == "y":
        print("We can get that stupid computer!")
        game()
    elif user_again == "n":
        print("You are just gonna walk away?")
        return
    else:
        replay()


def force_replay():
    answer = input()
    if answer == 'y':
        game()
    elif answer == 'n':
        return
    else:
        print("Try again please!")
        force_replay()


game()
