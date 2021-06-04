students={'name':'ziyaulhaq','age':20,'course':'bca','roll_no':174200191}
print(students)
print(students['name'])
print(students['age'])
print(students.get('marks','marks not present i9n dictionary'))
print(students.get('roll_nlo','roll_no is not present'))
students['marks']=80
print(students)
students.update({'name':'shivang','age':18})
print(students)
print(students.items())
print(students.keys())
print(students.values())
students['collage']='gla university'
print(students)
a=students.pop('age')
print(students)
print('pop=',a)
print(students.popitem())
students['age']=25
students['course']='mca'
print(students)
del students['age']
print(students)
print(students.setdefault('sex','xxx'))
print(students)
dictionary=students.copy()
print(dictionary)
print(students.fromkeys('name'))
students.clear()
print(students)
print(dictionary)
students['course']='bca'
print(students)
print(dictionary)



