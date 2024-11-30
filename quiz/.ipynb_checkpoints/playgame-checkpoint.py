from .quizbuilder import QuestionBuilder
import random

class Game:
    def __init__(self, playlist):
        self.q_builder = QuestionBuilder(playlist)
        self.score = 0
        self.q_count = 0
        
    def getoptions(self):
        return ["artist", "label", "length", "age", "tempo"]
    
    def setseed(self, seed):
        random.seed(seed)
    
    def ask(self, q_type):
        try:
            question, options, solution = self.q_builder.makequestion(q_type)
        except ValueError as e:
            print(e)
            return
            
        while True:             
            print(f"\n{question}")
            for i, o in enumerate(options, start=1):
                print(f"{i}. {o}  ")
                
            try:
                user_number = int(input("\nChoose the correct number from the above: "))
                if user_number >= 1 and user_number <= len(options):
                    user_answer = options[user_number-1]
                    if self.q_builder.checker(user_answer, solution):
                        print("\nCongratulations! You got the correct answer!\n")
                        self.score += 1
                        break
                    else:
                        print(f"\nSorry, your answer is wrong. The correct answer is '{solution}'.\n")
                    self.q_count += 1
                    break
                else:
                    print("Invalid number. Please enter a number from the list!\n")
                    continue
            except ValueError:
                print("Invalid input. Please enter a number from the list!\n ")
                continue
            
    def getscore(self):
        print(f"Your current score is: {self.score}/{self.q_count}. Keep up the great work!")

    def play(self):
        print("----------------------")
        print("SPOT YOUR SPOTIFY: QUIZ")
        print("----------------------\n")
        username = input("Enter your name: ")
        print(f"Hello {username}! We're glad you're here today!\n")
        
        while True:
            print("Choose a question type from below. Type 'exit' to finish the quiz. Type 'score' to access your score board.")
            opt = self.getoptions()
            for i in opt:
                print(i)
            user_input = input("\nEnter your choice: ").strip().lower()
            if user_input == "exit":
                print(f"\nQUIZ ENDED. {username}'s score is {self.score}/{self.q_count}. Thank you {username}! Hope to see you again!\n")
                break
            if user_input == "score":
                print("")
                self.getscore()
                print("")
                continue
            if user_input not in self.getoptions():
                print("Invalid choice. Please choose from the options above!\n)")
                continue
            self.ask(user_input)