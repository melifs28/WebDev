from pydantic import BaseModel
#look into Pydantic, I belief it adds types to Python 
cur_id = 0

def increment():
    global cur_id #if you were to do just cur_id it would be passed by value, and it would then delete the instance of that variable, 
    cur_id += 1   #here you do that so that you call by reference to the actual id variable
    return cur_id

class Task(BaseModel): #this is the syntax for inheritance (?)
    id: int 
    description: str = ""
    isComplete: bool = False

    def __init__(self, **data): #constructor 
       super().__init__(id= increment(), **data)