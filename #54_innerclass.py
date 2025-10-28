'''class student:
    def __init__(self,name,rollno):
        self.name = name
        self.rollno= rollno
    def show(self):
        print(self.name,self.rollno)
s1=student("shiva",2)
s2=student("ntr",3)
#print(s1.name,s1.rollno)

s1.show() #it shows all data'''


class student: #outer class
    def __init__(self,name,rollno):
        self.name = name
        self.rollno= rollno
        self.lap =self.laptop() #object of laptop because inner class obj should be call in outer class
    def show(self):
        print(self.name,self.rollno)
        self.lap.show()
    
    class laptop: #inner class
        def __init__(self):
            self.brand='hp'
            self.cpu='i5'
            self.ram=8
        def show(self):
            print(self.brand,self.cpu,self.ram)


s1=student("shiva",2)
s2=student("ntr",3)
#print(s1.name,s1.rollno)

s1.show() #it shows all data
#lap1=s1.lap
#lap2=s2.lap
#print(id(lap1))
#print(id(lap2))
