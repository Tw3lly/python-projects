from tkinter import *
from quiz_brain import QuizBrain

# Constants
THEME_COLOR = "#375362"
GREEN = "#80FF80"
RED = "#FF3232"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        # Window
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        # Canvas
        self.canvas = Canvas(width=300, height=250, highlightthickness=0, bg="white")
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        self.text = self.canvas.create_text(150, 125, width=280,
                                            text="Title", fill=THEME_COLOR,
                                            font=("Ariel", 20, "italic"))

        # Labels
        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(column=1, row=0)

        # Buttons
        true_button_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_button_image, highlightthickness=0, borderwidth=0,
                                  command=self.true_check_answer)
        self.true_button.grid(column=0, row=2)

        false_button_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_button_image, highlightthickness=0, borderwidth=0,
                                   command=self.false_check_answer)
        self.false_button.grid(column=1, row=2)

        # Calls function to get next question
        self.get_next_question()

        # Mainloop
        self.window.mainloop()

    def get_next_question(self):
        """Sets bg to white and calls for the next question from quiz_brain"""
        self.canvas.config(bg="white")
        # Only pulls next questions if there still are questions left in the list.
        if self.quiz.still_has_questions():
            # Update score label
            self.score_label.config(text=f"Score: {self.quiz.score}")
            # Updates question text in our canvas using from the return from function.
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.text, text=q_text)
        else:
            # If no questions remain, end quiz and disable buttons.
            self.canvas.itemconfig(self.text, text=f"You have reached the end of the Quiz.\n"
                                                   f"Your final score is {self.quiz.score}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_check_answer(self):
        """Runs when user presses True button"""
        self.give_feedback(self.quiz.check_answer("True"))

    def false_check_answer(self):
        """Runs when user presses the False button"""
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        """Lights background to red or green depending on if the user was right or wrong"""
        if is_right:
            self.canvas.config(bg=GREEN)
        else:
            self.canvas.config(bg=RED)

        self.window.after(1000, func=self.get_next_question)


