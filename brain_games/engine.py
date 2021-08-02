#!/usr/bin/env python
import prompt
count_games = 3


def run_engine(create_question_answer, INTRODUCTION_TO_GAME):
    break_count_game = 0
    print('Welcome to the Brain Games!')
    player_name = prompt.string('May I have your name? ')
    print(f'Hello, {player_name}!')
    print(INTRODUCTION_TO_GAME)
    while break_count_game != count_games:
        question, correct_answer = create_question_answer()
        print(f"Question: {question}")
        your_answer = prompt.string('Your answer: ')
        if str(correct_answer) == your_answer:
            break_count_game += 1
            if break_count_game == count_games:
                print(f'Congratulations, {player_name}!')
                return break_count_game
            else:
                print('Correct!')
        else:
            print(f"'{your_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'."
                  f"\n Let's try again, {player_name}!")
            break_count_game = count_games
