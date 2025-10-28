#polymorphism = It is nothing but same action can do in different ways
class pycharm:
   def execute(self): #same method
       print("compiling")
       print("Running")
class MyEditor:
    def execute(self): #same method
        print("spell check")
        print("convention check")
        print("compiling")
        print("running")

class laptop:
    def code(self,ide):
        ide.execute()

#ide =pycharm()
ide=MyEditor()
lap1= laptop()
lap1.code(ide)