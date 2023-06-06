
#creating a set
set1=()
print("Initial blank set:")
print(set1)

#creating a set using string 
set1=set("tanmayee")
print("\nSet with the use of string:") 
print(set1)

#creating a set using constructor
String ='Moonisbeautiful'
set2 = set(String)
print("\nSet with the use of an object:")
print(set2)

#creating a set using list 
set3=set(["Moon", "is", "beautiful", "beautiful"])
print("\nSet using list:")
print(set3)

#creating a set using numbers
set4=set([1,2,2,3,4,4,5,6,6,7])
print("\nSet with using numbers:")
print(set4)

#creating a set using mixed values
set4=(set([1,2,'Sunset',4,5,'Sunrise']))
print("\nSet with use of mixed values:")
print(set4)

#
set5=set()
print("\nBlank set")
print(set5)

#adding an element anf tuple to the set
set5.add(10)
set5.add(20)
set5.add((30,40))
print("\nSet after addition of three elements:")
print(set5)

#adding element to the set using iterator
for i in range(10,20):
    set5.add(i)
print("\nSet after addtion of elents from 10-20:")
print(set5)

#using update function
set5=set([4, 5, (6, 7)])
set5.update([10,11])
print("\nUsing update function:")
print(set5)

#accesing elements using loops
print("\nElements of sets:")
for i in set5:
    print(i, end="")

#removing elements from the set
set5.remove(4)
set5.remove(5)
print("\nSet after removing elements:")
print(set5)

