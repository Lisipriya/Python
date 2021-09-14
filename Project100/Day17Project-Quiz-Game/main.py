from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


question_bank = []

for items in question_data:
    question = items["question"]
    answer = items["correct_answer"]
    questions = Question(question, answer)
    question_bank.append(questions)


quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_questions():
    final_score = quiz_brain.next_question()

print("You have Completed the Quiz Competition")
print(f"You Final Score is: {final_score}")
