class QuizBrain:
    def __init__(self, q_list):
        self.qs_number = 0
        self.score = 0
        self.qs_list = q_list

    def has_questions(self):
        if self.qs_number < len(self.qs_list):
            return True
        else:
            return False

    def next_qs(self):
        current_qs = self.qs_list[self.qs_number]
        self.qs_number += 1
        user_answer = input(f"Q.{self.qs_number}: {current_qs.text} (True/False): ").lower()
        self.check_answer(user_answer, current_qs.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer.lower():
            self.score += 1
            print("Your answer is right.")
        else:
            print("Your answer is wrong.")
        print(f"The correct answer: {correct_answer}")
        print(f"Your current score: {self.score}/{self.qs_number} \n")

