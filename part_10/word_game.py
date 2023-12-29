# Write your solution here
import random

class WordGame():
    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds

    def round_winner(self, player1_word: str, player2_word: str):
        # determine a random winner
        return random.randint(1, 2)

    def play(self):
        print("Word game:")
        for i in range(1, self.rounds+1):
            print(f"round {i}")
            answer1 = input("player1: ")
            answer2 = input("player2: ")

            if self.round_winner(answer1, answer2) == 1:
                self.wins1 += 1
                print("player 1 won")
            elif self.round_winner(answer1, answer2) == 2:
                self.wins2 += 1
                print("player 2 won")
            else:
                pass # it's a tie

        print("game over, wins:")
        print(f"player 1: {self.wins1}")
        print(f"player 2: {self.wins2}")


class LongestWord(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        if len(player1_word) > len(player2_word):
            return 1
        elif len(player1_word) < len(player2_word):
            return 2
        else:
            return
        
class MostVowels(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        vowelList = ['a', 'e', 'i', 'o', 'u']
        p1Count = 0
        p2Count = 0
        for letter in player1_word:
            if letter.lower() in vowelList:
                p1Count += 1
        for letter in player2_word:
            if letter.lower() in vowelList:
                p2Count += 1
        if p1Count > p2Count:
            return 1
        elif p1Count < p2Count:
            return 2
        else:
            return     

class RockPaperScissors(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds) 

    def round_winner(self, player1_word: str, player2_word: str):
        validList = ['rock', 'paper', 'scissors']
        if (player1_word == "rock" and player2_word == "scissors") or (player1_word == "paper" and player2_word == "rock") or (player1_word == "scissors" and player2_word == "paper") or (player1_word in validList and player2_word not in validList):
            return 1
        elif (player1_word == "scissors" and player2_word == "rock") or (player1_word == "rock" and player2_word == "paper") or (player1_word == "paper" and player2_word == "scissors") or (player1_word not in validList and player2_word in validList):
            return 2
        else:
            return
if __name__ == "__main__":
    p = RockPaperScissors(4)
    p.play()