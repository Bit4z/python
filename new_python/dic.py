student={'name':'ziya','age':20, 'roll_no':174200191,'course':'bca'}
#print(student)
print("Age=%d\nname=%s"%(student['age'],student['name']))
print("pop=",student.pop('roll_no'))
print(student)
print("pop_item=",student.popitem())
student['course']='mca'
student['roll_no']=174200191
student['mobile']=7060544392
print(student)
student1=student
print("student1=",student1)
print(student.get('age','not present age in dictionary'))
print(student.get('marks','not present marks in dictionary'))
list=[]
print(student.values())
student.update({'name':'shivang'})
print(student)
student['name']='ziyaulhaq khan'
print(student)
print(student1.items())
del student['age']

print(student)
student1['pin_Code']=202131
student3=student.copy()
print("student=",student)
print("student1=",student1)
print("student3=",student3)

student1.clear()
print("student clear=",student)
print(student.setdefault('favourate_color','green'))
print(student)

for i in student:
    #print("%s=%s"%(i,student[i]))
    print(i)

print(student3.keys())
print(student.items())
