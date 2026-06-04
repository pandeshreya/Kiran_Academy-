#HomeWork
#1)Find common subjects
student1 = ['Python','Java',"SQL","HTML"]
student2 = ["PHP","Python","React", "JAVA"]

common_sub = []

for sub1 in student1:
    for sub2 in student2:
        if sub1.lower() == sub2.lower():
            common_sub.append(sub1)
print(common_sub)     #['Python', 'Java']


#2)check if list can append set and tuple or not
students = ["Sai","Rahul","Rohit","Sita","Gita","Ravi","Kumar"]

s = {5,6,7,8}
students.append(s)    
t = (1,2,3,4,5)
students.append(t)
print(students)    #['Sai', 'Rahul', 'Rohit', 'Sita', 'Gita', 'Ravi', 'Kumar', {8, 5, 6, 7}, (1, 2, 3, 4, 5)]


#3)check if tuple can allows set and list or not
t = (1,2,3,[10,20],{4,5,6})
print (t)  #(1, 2, 3, [10, 20], {4, 5, 6})

v1,v2,v3,v4,v5 = t
print(v4)  #[10, 20]
print(v5)  #{4, 5, 6}

#4)explore all the methods of set
"""s = {1,2,3}
s.add(4) #adds single element
print(s) #{1, 2, 3, 4}"""

"""s = {1,2,3}
s.clear() #removes all elements
print(s) #set()"""

"""s = {1,2,3}
s1 = s.copy() #copy set 
print(s1)  #{1, 2, 3}"""

"""a = {1,2,3,4}
b = {3,4,5,6}
print(a.difference(b))  #{1, 2}"""

"""s = {1,2,3}
s.discard(3) #removes an element
print(s)    #{1, 2}"""

"""a = {1,2,3}
b = {2,3,4}
print(a.intersection(b))  #{2, 3}"""
