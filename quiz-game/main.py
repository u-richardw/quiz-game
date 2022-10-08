from data import question_data
from question_model import question
from quiz_brain import QuizBrain
question_bank = []
for questions in question_data:
    question_text = questions["question"]
    question_answer = questions["correct_answer"]
    new_question = question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz")
print(f"YOur final score was: {quiz.score}/{quiz.question_number}")
