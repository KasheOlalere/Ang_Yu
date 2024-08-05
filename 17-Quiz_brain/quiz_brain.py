# ask question
# check if answer is correct
# check if at end

from data import question_data

class QuizBrain:
    def __init__(self,q_list) -> None:
        self.question_number = 0
        self.correct = 0
        self.question_list = q_list
    def ask(self):
        while self.question_number < len(self.question_list):
            answer = input(f'Q.{self.question_number+1} {self.question_list[self.question_number].text} ? (True/False)\n')
            if answer.capitalize() == self.question_list[self.question_number].answer:
                print('That is correct')
                self.correct += 1
            elif answer.capitalize() == 'Quit' or answer.capitalize() == 'Exit':
                print('You have chosen to end the program')
                break
            else:
                print('That is wrong')
            print(f'{self.correct}/{self.question_number+1}')
            self.question_number += 1
        print(f'That\'s all folks, you scored {round(self.correct/(self.question_number+1)*100,2)}%')