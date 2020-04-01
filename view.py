from flask import Flask,render_template,request


import time
import sys
import random

    app=Flask(__name__)


class Game:
    def player_win(self):
        print("Great you won this time!!!")

    def computer_win(self):
        print("computer won this time,better luck next time")

    def draw(self):
        print("Game is draw")

    def game_begin(self):
        choices=['rock','paper','scissors']
        attempts=3
        player_choice=input("Please enter your choice:")
        while True:
            if player_choice not in choices:
                print("Invalid choice,you have {} attempts left".format(attempts))
                attempts-=1

            else:
                computer=random.choice(choices)
                print("Computer : {} ".format(computer))

                if player_choice == computer:
                    self.draw()

                elif player_choice == 'rock' and computer == 'paper':
                    self.computer_win()

                elif player_choice == 'paper' and computer == 'rock':
                    self.player_win()
```````````````````````````````````````````
                elif player_choice == 'scissors' and computer == 'paper':
                    self.player_win()

                elif player_choice == 'rock' and computer == 'scissors':
                    self.player_win()

                elif player_choice == 'paper' and computer == 'scissors':
                    self.computer_win()

                elif player_choice == 'scissors' and computer == 'rock':
                    self.computer_win()

                else:
                    pass

                play_again=str(input("Do you want to play again? y/n:"))
                if play_again.lower == 'y':
                    self.game_begin()

                elif play_again.lower == 'n':
                    print("Good Bye!!")
                    time.sleep(2.5)
                    sys.exit(0)

                else:
                    print("Invalid option,good bye:")
                    time.sleep(2.5)
                    sys.exit(0)



@app.route('/')
def home():
    return render_template('index.html')


@app.route('/action',methods=['GET','POST'])
def action():
    return render_template('action.html')


@app.route('/score')
def score():
    return render_template('score.html')


if __name__ == '__main__':
    app.run(debug=True)


