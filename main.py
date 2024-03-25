# create a quizz game with admin and players.
# A user has to login. If player then he can play,
# if admin, can add quesitons
import json
import users




if __name__ == '__main__':
    welcome_msg = "Welcome to Quizz Game"
    print(f"{len(welcome_msg) * '='}{welcome_msg}{len(welcome_msg) * '='}")

    users.login()