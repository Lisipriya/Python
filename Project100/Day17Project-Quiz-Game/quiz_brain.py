class QuizBrain:
    def __init__(self, ques_list):
        self.question_number = 0
        self.question_list = ques_list
        self.score = 0

    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    def next_question(self):
        new_question = self.question_list[self.question_number]
        self.question_number += 1
        user_input = input(f"Q{self.question_number}: {new_question.question} (True/False)?: ").lower()
        correct_answer = new_question.answer
        final = self.check_answer(user_input, correct_answer)
        return final

    def check_answer(self, user_input, correct_answer):
        if user_input == correct_answer.lower():
            self.score += 1
            print("You got it!..")
        else:
            print("That's wrong answer")

        print(f"The Correct answer was: {correct_answer}")
        print(f"Your Current Score is: {self.score}/{self.question_number}")
        return f"{self.score}/{self.question_number}"
