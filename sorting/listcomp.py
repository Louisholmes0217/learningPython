# list comprehension

# long way to create this list
squares = []
for i in range(1,11):
    squares.append(i*i)
print(squares)

# list comprehension way of doing the same thing
squares = [i * i for i in range(1,11)]
print(squares)

students = [100,90,80,70,60,50,40,30,0]

#passed_students = list(filter(lambda x:x>=60, students))
#print(passed_students)
# can be written as:
# passed_students = [i for i in students if i >= 60]
passed_students = [i if i >= 60 else "FAILED" for i in students]
print(passed_students)