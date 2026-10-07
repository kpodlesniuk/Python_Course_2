"""
Practice basic Python data structures.

List:
- Create a list named 'fruits' with 'apple', 'banana', 'cherry', and 'potato'.
- Add 'grape' to the list.
- Remove 'potato' from the list.
- Check if 'apple' is in the list and output the result.

Tuple:
- Create a tuple named 'colors' with three colors of your choice.
- Calculate its length and output the result.

Set:
- Create a set named 'numbers' with the numbers from 1 to 3.
- Add the number 4 to the set.

Dictionary:
- Create a dictionary named 'person' with 'name' and 'age' key-value pairs.
- Create a new key-value pair with a new 'name' and age.
"""

fruits = ['apple', 'banana', 'cherry', 'potato']
fruits.append('grape')
fruits.remove('potato')
if 'apple' in fruits:
    print("Apple is in the fruits list")
else:
    print("Apple is not in the fruits list")

colors = ('turquoise', 'cyan', 'navyblue', 'forestgreen')
length = len(colors)
print("Length if the colors tuple is:", length)

numbers = {1, 2, 3}
numbers.add(4)
print("Set numbers is now:", numbers)

person = {
    "Kate": 36,
    "Dmytro": 35,
    "Liutoslava": 30
}

person["Vohneslava"]=55
print("Dictionary person is now:", person)