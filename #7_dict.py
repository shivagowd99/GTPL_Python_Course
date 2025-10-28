#dict- unordered key value pairs,keys should be unique and its not allow duplicate keys

"""student= {"name":"shiva" ,"marks":470 , "perc":"98%", "college":"aditya engineering college"}
#b=student["name"]
b=student.get("perc")
print(b)"""

#combined two lists into dict datatype by using zip 
'''
keys=["name","perc","college"]
values=["shiva",80,"aditya"]
s=dict(zip(keys,values))
print(s)'''

'''program = {'js':'atom','cs':'vs','python':['pycharm','sublime'],'java':{'jse':'netbeans','jee':'eclipse'}}
run=program['java']['jse']
print(run)'''

#program to get keys in dict
shiva={"name":"ram","age":24,"college":"aditya"}
value=shiva.keys()
print(value)


#program to get values in dict
shiva={"name":"ram","age":24,"college":"aditya"}
value=shiva.values()
print(value)


#program to get items in dict
shiva={"name":"ram","age":24,"college":"aditya"}
value=shiva.items()
print(value)


#program to clear dict
shiva={"name":"ram","age":24,"college":"aditya"}
value=shiva.clear()
print(value)