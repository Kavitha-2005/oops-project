                # PYTHON PROJECT - 2

         # Question and project discribtion

             ''' 1. Calculator
              2. To-Do List App
              3. Number Guessing Game
              4. Quiz App
               ( Using Oops )'''




# 1. CALCULATOR (OOPS VERSION

class calculator:
    def add(self,a,b):
        print(a+b)
    def sub(self,a,b):
        print(a-b)
    def multiply(self,a,b):
        print(a*b)
    def divide(self,a,b):
        print(a%b)
cal=calculator()
cal.add(5,6)
cal.sub(3,8)
cal.multiply(12,9)
cal.divide(2,10)

# 2.TO-DO LIST APP

class todo_list:
    def __init__(self):
        self.tasks=[]
    def add_task(self,task):
        self.tasks.append(task)
        print(task)
    def remove_task(self,task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(task)
        else:
            print("task not found")
    def show_tasks(self):
        if not self.tasks:
            print("no task in the list.")
        else:
            print("your tasks:")
            for i,task in enumerate(self.tasks,1):
                print(i,task)
todo=todo_list()
todo.add_task("studying")
todo.add_task("complete project")
todo.add_task("complete breakfast")
todo.add_task("vessels washing")
todo.add_task("cloth washing")
todo.show_tasks()
todo.remove_task("studying")
todo.remove_task("breakfast")
todo.show_tasks()


# 3.NUMBER GUESSING GAME

import random
class number_guessing_game:
    def __init__(self):
        self.secret_number=random.randint(1,50)
    def guess(self,number):
        if number==self.secret_number:
            return("*correct!*you guessed it!")
        elif number<self.secret_number:
            return("too low!")
        else:
            return("too high!")
game=number_guessing_game()
while True:
    user_guess=int(input("ENTER YOUR GUESSING NUMBER (1-50):"))
    result=game.guess(user_guess)
    print(result)
    if result.startswith("correct"):
        break

# 4. QUIZ APP

class question:
    def __init__(self,text,answer):
        self.text=text
        self.answer=answer
class quiz:
    def __init__(self,question):
        self.questions=questions
        self.score=0
    def start(self):
        for i in self.questions:
            user_answer=input(i.text+"(true/false)")
            if user_answer.lower()==i.answer.lower():
                print("correct answer")
                self.score+=1
            else:
                print("wrong answer")
        print(self.score,len(self.questions))
questions=[question("Python is an interpreted language.","true"),
           question("The earth is a flat.","false"),
           question("Oops means object oriented programming.","true")]
quiz=quiz(question)
quiz.start()
                
    
        






































        
        
        





        
    
