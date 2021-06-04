students={'name':'ziyaulhaq','age':20,'roll_no':174200191,'branch':'bca'}#1
print(students)
print('roll_no=',students['roll_no'])#2
print(students)
students['marks']=50#3
print(students)
del students['age']#4
print(students)
name=students.pop('name')#5
print(name)

print(students.get('age','is not present in dictionary'))#6

print(students.popitem())#7
#students.clear()
students.update({'age':25})#8
print(students)

students.setdefault('sex',0)#9
print(students)
print(students.values())#10
print(students.keys())#11
print(students.items())#12
student1=students.copy()#13
print('student1=',student1)
r=student1#14
print(r)

      
                         
