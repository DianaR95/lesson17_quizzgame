# create a quizz game with admin and players.
# A user has to login. If player then he can play,
# if admin, can add quesitons
import json
import time

import admin_functions
import users
import game




if __name__ == '__main__':
    welcome_msg = "Welcome to Quizz Game"
    print(f"{len(welcome_msg) * '='}{welcome_msg}{len(welcome_msg) * '='}")

    current_player = users.login()

    while True:
        if list(current_player.keys())[0] == 'admin':
            admin_functions.run()
        else:
            print(f"Let's play {list(current_player.keys())[0]}")
            game.run_game(current_player)
            user_pick = input("DO you want to play again? Y/N: ")
            if user_pick.lower() == "n":
                break
        time.sleep(2)