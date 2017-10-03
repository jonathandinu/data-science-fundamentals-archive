my_var = 4

# Initialize a new List. Can contain heterogeneous types
my_list = [1, "jonathan", [1,2,3], my_var]

# Indexing
my_list[1] #=> 'jonathan'

# Slicing (end point exclusive)
my_list[:2] #=> [1, 'jonathan']

# Negative Indexing (everything but last element)
my_list[:-1] #=> [1, 'jonathan', [1,2,3]]

# In-place Append
my_list.append(10)
print(my_list) #=> [1, 'jonathan', [1, 2, 3], 4, 10]

# Item Assignment
my_list[2] = "dinu"
print(my_list) #=> [1, 'jonathan', 'dinu', 4, 10]

# Concatenate two lists
my_list + [11, 12, 13] #=> [1, 'jonathan', 'dinu', 4, 10, 11, 12, 13]

# Concatenate and update
my_list += [11, 12, 13]
print(my_list) #=> [1, 'jonathan', 'dinu', 4, 10, 11, 12, 13]

num_list = [3, 2, 7, 1, 5]

# Sorting
sorted(num_list) #=> [1, 2, 3, 5, 7]

# In-place Sort
num_list.sort() #=> None
print(num_list) #=> [1, 2, 3, 5, 7]

# Tuples
tup = ("hello", 2, 3)

# Indexing like lists
tup[0] #=> 'hello'

# Tuples are Immutable however
tup[1] = 5 #=> TypeError: 'tuple' object does not support item assignment

# Dictionaries
employees = {'Jon': 42, 'Anne': 53213}

# Set new key
employees['Elisa'] = 7821

# Check Membership
'Jon' in employees #=> True

# Remove a key
del employees['Jon']

'Jon' in employees #=> False

employees.items() #=> dict_items([('Anne', 53213), ('Elisa', 7821)])

tup = ('Jonathan', 'Dinu')
employees[tup] = 21235

print(dictionary) #=> {'Anne': 53213, 'Elisa': 7821, ('Jonathan', 'Dinu'): 21235}

# Sets

words = set(['the', 'red', 'panda', 'jumped', 'over', 'the', 'red', 'barn'])

# No intrinsic order
print(words) #=> {'panda', 'over', 'red', 'the', 'barn', 'jumped'}

# Great for membership checks
'fox' in words #=> False

sentence = set(['the', 'red', 'fox', 'jumped', 'over', 'the', 'brown', 'fence'])

# Set logic: Difference
sentence - words #=> {'brown', 'fence', 'fox'}
words - sentence #=> {'barn', 'panda'}

# Set logic: Union
words | sentence #=> {'barn', 'brown', 'fence', 'fox', 'jumped', 'over', 'panda', 'red', 'the'}

# Set logic: Intersection
words & sentence #=> {'jumped', 'over', 'red', 'the'}

# Conditionals

if my_var == 42:
    print('The Universe makes sense')
elif 42 == 42:
    print("Numbers work")
else:
    print('Numbers are broken ¯\_(ツ)_/¯')
#=> 'Numbers work'

# Can use Ternary operator too!
'Numbers work' if 42 == 42 else 'Numbers are broken ¯\_(ツ)_/¯'
#=> 'Numbers work'

# Iteration
for item in my_list[4:]:
    print(item)

#=> 10
#=> 11
#=> 12
#=> 13

for idx in range(3):
    print(my_list[idx])

#=> 1
#=> 'jonathan'
#=> 'dinu'
