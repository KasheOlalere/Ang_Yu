class User:
    def __init__(self,user_id,username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
        
    def follow(self,user):
        user.followers += 1
        self.following += 1

from data import question_data
class Question:
    def __init__(self,number):
        self.question = question_data[int(number)]['text']
        self.answer = question_data[int(number)]['answer']
        pass
    def ask(self):
        print(self.question)
        answer = input('Please input your answer: ')
        if answer.lower() == self.answer.lower():
            print('That\'s right, you are correct' )
            cont = input('Do you want to continue: ') 
            if cont.lower() == 'yes':
                start()
        else:
            try_ = input('Nope, that is wrong, would you like to, try again ?')
            if try_.lower() == 'yes':
                self.ask()
            else:
                print(f'The answer is {self.answer}')
        
def start():
    no = input('Pick a number: ')
    
    for i in range (11):
        print(f'Question {i}:')
        question = Question(i)
        question.ask()
        
start()