from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []
for qs in question_data:
    qs_text = qs["text"]
    qs_answer = qs["answer"]
    new_qs = Question(qs_text, qs_answer)
    question_bank.append(new_qs)

quiz = QuizBrain(question_bank)

while quiz.has_questions():
    quiz.next_qs()

print("You have completed the quiz game.")
print(f"Your final score: {quiz.score}/{quiz.qs_number}")
