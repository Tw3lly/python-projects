# Create model for question
# attributes text, answer
# Imports
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
# Creates empty list where we will store the dictionary items from data.py as an object in a list
question_bank = []

# Converting dict in data.py into objects and transferring them to a list
# Loops through dictionary
for question in question_data:
    # question_text will store the text value from dict
    question_text = question["text"]
    # question_answer will store the answer value from dict
    question_answer = question["answer"]
    # Creates an object from the class Question. Question has two attributes, q_text and q_answer.(question_model.py)
    # We pass in the question_text value and question_answer as the attribute data. This data changes for each time
    # we go through the loop.
    new_question = Question(question_text, question_answer)
    # Appends the newly formatted question object to the empty list created above
    question_bank.append(new_question)
    # We loop through the dictionary until the end.

# Creates a new object using QuizBrain class, QuizBrain init had one parameter so we pass on the newly modified
# question_bank as a list, and it will pull data from there
quiz = QuizBrain(question_bank)
# We tap in to the still_has_questions method, which checks if the list of questions has reached its end.
# as long as it returns True loop will continue, when it returns False the loop will end.
while quiz.still_has_questions():
    # We tap into the next_question method which will pick out the current question and print out an input statement
    quiz.next_question()

# Print statements to inform the user they have completed the Quiz
print("You have completed the quiz!")
# We tap into the quiz object to be able to pull out the score and the q_number and use it in a print statement
print(f"Your final score was: {quiz.score}/{quiz.q_number}")
