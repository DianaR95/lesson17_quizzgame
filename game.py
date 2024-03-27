import copy
import datetime
import json
import random
import time
from quizz_logger import logger

POSSIBLE_ANSWERS = {0: 'a.', 1: 'b.', 2: 'c.', 3: 'd.'}


def change_highscore(player_id: str, score: int, path: str = "users.json"):
    try:
        with open(path, "r+") as f:
            players = json.loads(f.read())
            players[player_id]['high_score'] = score
            players[player_id]['date'] = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
            f.seek(0)
            f.write(json.dumps(players, indent=4))
    except Exception as e:
        print(f"Failed to save the highscore of {player_id} as {e}")
    else:
        print("Succesfully saved the new highscore")


def read_questions(questions_path: str = "questions.json"):
    try:
        with open(questions_path, "r") as f:
            questions = json.loads(f.read())
            questions = questions['questions']
        return questions
    except Exception as e:
        print(f"Fatal error on reading quizz questions: {e}")
        logger.error(f"Fatal error on reading quizz questions: {e}")
        exit(1)


def run_game(player: dict, questions_path: str = "questions.json") -> int:
    score = 0
    questions = read_questions(questions_path)

    copy_questions = copy.deepcopy(questions)

    while copy_questions:
        question_object = random.choice(copy_questions)

        # print(question_object)
        print(question_object['question'])
        for index, answer in enumerate(question_object['answers']):
            print(f"\t{POSSIBLE_ANSWERS[index]} {answer}")

        pick = input("Alege raspunsul corect: ")
        answers = {v: k for k, v in POSSIBLE_ANSWERS.items()}
        if answers[f"{pick}."] == question_object['correctIndex']:
            print("Corect answer")
            score += 1
        else:
            print("Wrong answer")
        copy_questions.remove(question_object)
        time.sleep(1)

    print(f"You have answered to {score} questions corectlly")

    if score > player[list(player.keys())[0]]['highscore']:
        change_highscore(player_id=list(player.keys())[0], score=score)

    return 1