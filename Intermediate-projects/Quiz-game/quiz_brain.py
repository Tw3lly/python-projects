# 2 attributes, question_number, question_list which is being initialized when new quiz brain is created
# Pass over question bank into question list, initialize into an input
# Usually you assign attributes in the __init__
class QuizBrain:
    def __init__(self, q_list):
        # q_number, so we can keep track of which question we are at with a count
        self.q_number = 0
        # Score attribute to keep track of the users score
        self.score = 0
        # we've defined the question_list as an attribute of an object within the QuizBrain class because,
        # quiz program focuses on being able to access the questions and their answers.
        # We want this as an attribute so any method that the QuizBrain needs to execute can access it
        # and modify it easily.
        self.question_list = q_list

    def still_has_questions(self):
        # if the q_number is less or equal to the end of the list, while loop in main.py will continue asking questions
        if self.q_number <= len(self.question_list)-1:
            return True
        # Else we will return False, which will end the loop.
        else:
            return False
        # !LESSONS LEARNED!
        # To make above method one line of code:
        # return self.q_number < len(self.question_list)

    def next_question(self):
        # Current question is equal to the qlist[index_number]
        current_question = self.question_list[self.q_number]
        # After we got a hold of the item in the index, which starts with 0, we want the question number that's being
        # printed to start with 1 instead of 0, therefore we go one number up.
        self.q_number += 1
        # Input is = guess, Where we have the q-number and the text inserted
        # Remember: Question had two attributes, .text and .answer
        user_answer = input(f'Q.{self.q_number}: {current_question.text} (True/False): ')
        # We call out the method check:answer at the end of each question to check answer
        # It will use the user_answer as input and compare it to current_question.answer
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        # If user answer is equal to correct answer
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            # 1 Point to the user score will be added
            self.score += 1
        else:
            print("You got it wrong")
        # print out the correct answer regardless of user was right/wrong
        print(f"The correct answer was: {correct_answer}.")
        # Prints out your current score/vs/the current question number
        print(f"Your score is {self.score}/{self.q_number} \n")


