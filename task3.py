#Assigning elements to different lists

lst1 = [34,5,6,22]
lst1.append(12)
print(lst1)

lst2 = [3,4,7]
lst2.extend([23,56,8])
print(lst2)

lst1.insert(2,'rahul')
print(lst1,"\n")


#Accessing elements from a tuple

tup = (1,2,3,4,5)

print(tup[2])
print(tup[0:])
print(tup,"\n")


#Deleting different dictionary elements

dec = {'key':'value','name':'age','ram':'12','rohan':'23'}
print(dec)
del dec['ram']
print(dec)
dec.pop('rohan')
print(dec)
dec.clear()
print(dec)
