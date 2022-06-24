# IMPORTING LIBRARIES
import html


class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        self.question = self.question_list[self.question_number]
        self.question.text = html.unescape(self.question.text)
        self.question_number += 1
        return f"Q.{self.question_number}: {self.question.text}"

    def still_has_questions(self):
        if self.question_number == len(self.question_list):
            return False
        return True

    def check_answer(self, user_answer):
        if user_answer.lower() == self.question.answer.lower():
            self.score += 1
            return True
        else:
            return False

    def print_result(self):
        print("You have completed the quiz.")
        print(f"Your final score was: {self.score}/{self.question_number}.")
