students={'name':'ziyaulhaq','age':20,'roll_no':174200191,'branch':'bca'}#1
print(students)
print('roll_no=',students['roll_no'])#2
print(students)
students['marks']=50#
print(students)
del students['age']
print(students)
name=students.pop('name')
print(name)

print(students.get('age','is not present in dictionary'))

print(students.popitem())
#students.clear()
students.update({'age':25})
print(students)

students.setdefault('sex',0)
print(students)
print(students.values())
print(students.keys())
print(students.items())
student1=students.copy()
print('student1=',student1)
r=student1
print(r)

      
                         
