class Question:
    def __init__(self,q_text,q_answer) -> None:
        self.text = q_text
        self.answer = q_answer
        
        
q_1 = Question('Is yam good','Yes')
q_1.answer()