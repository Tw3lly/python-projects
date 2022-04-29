# Quiz app with GUI. Pulls questions from https://opentdb.com/api.php.

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

# Creates empty list where we will store the dictionary items from data.py as an object in a list
question_bank = []

# Converting dict in data.py into objects and transferring them to a list
# Loops through dictionary
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]

    # Creates an object from the class Question. Question has two attributes, q_text and q_answer.(question_model.py)
    # We pass in the question_text value and question_answer as the attribute data. This data changes for each time
    # we go through the loop.
    new_question = Question(question_text, question_answer)

    # Appends the newly formatted question object to the empty list created above
    question_bank.append(new_question)


# Creates the quiz using our question list as a parameter
quiz = QuizBrain(question_bank)

# Calls for the quiz_UI using the QuizzInterface class where we pass in our quiz
quiz_ui = QuizInterface(quiz)
