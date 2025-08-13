from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []
for question in question_data:
    question_text= question["text"]
    question_answer = question["answer"]
    new_question=Question(question_text, question_answer)
    question_bank.append(new_question)
print(question_bank[0])  # This will print the list of Question objects created from question_data    
quiz=QuizBrain(question_bank)
quiz.next_question()  # This will call the next_question method from QuizBrain class
while quiz.still_has_question():
    quiz.next_question()  # This will continue to call next_question until there are no more question