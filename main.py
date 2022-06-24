# IMPORTING LIBRARIES
from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
from ui import QuizUI

question_bank = []

for i in question_data:
    q = Question(i["question"], i["correct_answer"])
    question_bank.append(q)

brain = QuizBrain(question_bank)

quizzlet = QuizUI(brain)
