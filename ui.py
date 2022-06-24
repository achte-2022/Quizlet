# IMPORTING LIBRARIES
import tkinter
from quiz_brain import QuizBrain

# CONSTANTS
TRUE_IMAGE = "images/true.png"
FALSE_IMAGE = "images/false.png"
THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")
SCORE_FONT = ("Arial", 20)
CANVAS_WIDTH = 300
CANVAS_HEIGHT = 250


class QuizUI:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz_brain = quiz_brain
        self.score = 0
        self.window = tkinter.Tk()
        self.window.title("Quizzlet")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        # SCORE LABEL
        self.score_label = tkinter.Label(
            text=f"Score: {self.score}", font=SCORE_FONT, bg=THEME_COLOR, fg="white"
        )
        self.score_label.grid(row=0, column=1)

        # MAIN CANVAS
        self.canvas = tkinter.Canvas(
            width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white"
        )
        self.text = self.canvas.create_text(
            CANVAS_WIDTH / 2,
            CANVAS_HEIGHT / 2,
            text=f"Score:",
            font=FONT,
            fill=THEME_COLOR,
            width=CANVAS_WIDTH - 20,
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # TRUE BUTTON
        true_img = tkinter.PhotoImage(file=TRUE_IMAGE)
        self.true_button = tkinter.Button(
            image=true_img, highlightthickness=0, command=self.press_true
        )
        self.true_button.grid(row=2, column=0)

        # FALSE BUTTON
        false_img = tkinter.PhotoImage(file=FALSE_IMAGE)
        self.false_button = tkinter.Button(
            image=false_img, highlightthickness=0, command=self.press_false
        )
        self.false_button.grid(row=2, column=1)
        self.get_question()
        self.window.mainloop()

    def get_question(self):
        self.canvas.config(bg="white")
        if self.quiz_brain.still_has_questions():
            question_text = self.quiz_brain.next_question()
            self.canvas.itemconfig(self.text, text=question_text)
        else:
            self.canvas.itemconfig(
                self.text, text="You've reached the end of the quiz."
            )
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
            self.score_label.config(
                text=f"Score: {self.score}/{self.quiz_brain.question_number}"
            )
        return

    def press_true(self):
        answer = self.quiz_brain.check_answer("True")
        if answer:
            self.score += 1
        self.score_label.config(text=f"Score: {self.score}")
        self.give_feedback(answer)
        return

    def press_false(self):
        answer = self.quiz_brain.check_answer("False")
        if answer:
            self.score += 1
        self.score_label.config(text=f"Score: {self.score}")
        self.give_feedback(answer)
        return

    def give_feedback(self, answer):
        if answer:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_question)
        return
