import json
import os
import random
import sys
import time

QUOTES_JSON_DIR = "workspace/DevSecOps/GuessGame/120Inspiring3WordQuotes.json"


class GuessGame():
    def __init__(self):
        self.quotes_list = []
        self.random_quote = []
        self.spaces_quote = []
        self.score = 0
        self.elapsed_time = 0

    def init_quotes_list(self):
        quotes_file = self.read_json()
        self.quotes_list = self.quotes_to_lists(quotes_file)

    def read_json(self):
        home = os.path.expanduser("~")
        path = os.path.join(home, QUOTES_JSON_DIR)
        with open(path) as f:
            return json.load(f)

    def quotes_to_lists(self, quotes_file):
        new_list = []
        for key, value in quotes_file.items():
            word_list = value.lower().split()
            new_list.append(word_list)
        return new_list

    def init_spaces_quote(self):
        for char in self.random_quote:
            if char != ' ':
                self.spaces_quote.append('_')
            else:
                self.spaces_quote.append(' ')
            

    def print_instructions(self, instructions, delay_sentence = 0, delay_char = 0):
        for sentence in instructions:
            time.sleep(delay_sentence)
            if delay_char:
                for char in sentence:
                    time.sleep(delay_char)
                    print(char, end = "")
                print("\n")
            else:
                print(sentence)

    def print_game_board(self):
        os.system('clear')
        instructions = [
            "Guess letters by pressing on the keyboard-\n",
            f"{''.join(self.spaces_quote)}\n",
            f"score: {self.score}    time: {self.elapsed_time}\n"
        ]
        self.print_instructions(instructions)

    def check_input_get_score(self, user_input):
        char_exists = False
        for n in range(len(self.random_quote)):
            if user_input == self.random_quote[n]:
                self.spaces_quote[n] = self.random_quote[n]
                char_exists = True
        if char_exists:
            self.score += 5
        else:
            self.score -= 1

    def spaces_quote_done(self):
        joined_quote = ''.join(self.spaces_quote)
        if '_' not in joined_quote:
            time.sleep(1)
            os.system('clear')
            instructions = [
                "Great! you got this one!",
                f"It only took you {self.elapsed_time} seconds..!"
            ]
            self.print_instructions(instructions, 0.5, 0.05)
            return True
        return False

    def game_over(self):
        if self.spaces_quote_done():
            if self.elapsed_time <= 30:
                self.score += 100
                instructions = ["Which means you earned a 100 extra points!"]
            else:
                instructions = ["You might improve next time..."]
            instructions.append([f"In total you earned {self.score} points- Well Done!"])
            self.print_instructions(instructions, 0.5, 0.05)
            return True
        return False
    
    def restart_or_exit(self):
        instruction = [
            "Would you like to play another round?",
            "Enter 'r' to replay or 'x' to Exit: "
        ]
        self.print_instructions(instruction, 0.5, 0.05)
        while (1):
            user_input = input()
            if user_input == "x":
                sys.exit()
            elif user_input == "r":
                return True
            else:
                print("Wrong input, try again...")

    def play_game(self):
        start_time = time.time()
        while(1):
            self.print_game_board()
            if self.game_over():
                if self.restart_or_exit():
                    return
            user_input = input()
            self.check_input_get_score(user_input)
            end_time = time.time()
            self.elapsed_time = end_time - start_time


    def start(self):
        while(1):
            os.system('clear')
            print("Welcome to the Quotes Guessing Game!\n")
            self.init_quotes_list()
            instructions1 = [
                f"You'll get a random quote from {(len(self.quotes_list))} possibilities",
                "You need to guess the letters of this quote",
                "Each correct answer will be credited with 5 points",
                "Wrong answer?- You lose 1 point",
                "Guess the whole quote in less than 30 seconds & get a 100 points!"
                ]
            self.print_instructions(instructions1, 1, 0.05)
            self.random_quote = list(
                ' '.join(random.choice(self.quotes_list))
            )
            self.init_spaces_quote()
            instructions2 = ["Ready?", "Steady?", "Go!!!"]
            self.print_instructions(instructions2, 1.5)
            time.sleep(1)
            self.play_game()
            self.__init__()


if __name__ == "__main__":
    game_instance = GuessGame()
    game_instance.start()
