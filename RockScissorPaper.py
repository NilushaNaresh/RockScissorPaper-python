import time
import sys
import random


def player_win():
    print("Great you won this time!!!")


def computer_win():
    print("computer won this time,better luck next time")


def draw():
    print("Game is draw")


def game_begin():
    choices=['rock','paper','scissors']
    attempts=3
    while attempts<=3 and attempts >=0:
        player_choice=input("Please enter your choice:")
        if player_choice not in choices:
            print("Invalid choice,you have {} attempts left".format(attempts))
            attempts-=1

        else:
            computer=random.choice(choices)
            print("Computer : {} ".format(computer))

            if player_choice == computer:
                draw()

            elif player_choice == 'rock' and computer == 'paper':
                computer_win()

            elif player_choice == 'paper' and computer == 'rock':
                player_win()

            elif player_choice == 'scissors' and computer == 'paper':
                player_win()

            elif player_choice == 'rock' and computer == 'scissors':
                player_win()

            elif player_choice == 'paper' and computer == 'scissors':
                computer_win()

            elif player_choice == 'scissors' and computer == 'rock':
                computer_win()

            else:
                pass

            play_again=str(input("Do you want to play again? y/n:"))
            if play_again == 'y':
                game_begin()

            elif play_again == 'n':
                print("Good Bye!!")
                time.sleep(2.5)
                sys.exit(0)

            else:
                print("Invalid option,good bye:")
                time.sleep(2.5)
                sys.exit(0)


if __name__ == '__main__':
    game_begin()