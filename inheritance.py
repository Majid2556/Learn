class Human:

    def __init__(self,name,lname,age):
        self.name = name
        self.lname = lname
        self.age = age
        print(f"{self.name} Welcom")
    def sleep(self):
        return f"{self.name} sleeping....Zzzz"
    def __repr__(self):
        return f"{self.name} Hello"

class teacher(Human):

    def __init__(self,teacher_ID,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.teacher_ID = teacher_ID  

    def Score(self):
        return "Score!!"  
  


Ali = teacher(name = "Ali", lname = "Rezaei", age = 26,  teacher_ID = 1234)
print(Ali)