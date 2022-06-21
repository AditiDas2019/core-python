# 1. Capitalize():
#     Capitalizer first letter of string
print("----------------1. Capitalize--------------------")
word = "hello world"
word.capitalize()   # senorio_1 = Variable not initialized, it'll be garbage collected.
print("without capitalize: " + word)
word_1= word.capitalize()   # senario_2 = Assigning to new variable.
print("with capitalize: " + word_1)
word= word.capitalize()   # senario_3 = Updating to the existing variable.
print("with capitalize: " + word_1)

# 2. Length of string:
print("----------------2. Length of string--------------------")
    # Math_function
length_of_string = "Python Programming avcjhvsj xkasga Python nbjhav Python"

print(len(length_of_string))

# 3. Count characters in string
print("----------------3. Count characters in string--------------------")
count_of_string = "bAsavaraju"

    # While loop

i = 0
while i < len(count_of_string):
    # sum = count_of_string.count(count_of_string[i])
    print(count_of_string[i]+":",count_of_string.count(count_of_string[i]))
    i += 1

    # For Loop
count = 0
for i in count_of_string:
    print(i+":", count_of_string.count(i))

# 4.String slicing
print("----------------4.String slicing--------------------")
String_slicing = "Checking for membership"
slice_1 = String_slicing[:]
print(slice_1)
slice_2 = String_slicing[0:]
print(slice_2)
slice_3 = String_slicing[::-1]
print(slice_3)
slice_4 = String_slicing[:12:-2]
print(slice_4)
slice_5 = String_slicing[2:20:4]
print(slice_5)

# 5. Length of longest string in python
print("----------------5. Length of longest string in python--------------------")
longest_length_of_word = "Length of longest string in python"
print(max(longest_length_of_word))
longest_length_of_word = list(longest_length_of_word.split())
print(longest_length_of_word)
print(max(longest_length_of_word))  # AASCI value

char = []
for i in longest_length_of_word:    # length wise longest count value
    char.append(len(i))
print(max(char))

# 6. First last chars swapping
print("----------------6. First last chars swapping--------------------")

swapping = "Python programming"
length = len(swapping)
print(swapping[length-1] + swapping[1:length-1] + swapping[0])
# Transelate method
maketrans = swapping.maketrans
x = swapping.translate(maketrans('Pg','gP'))
print(x)

# 7.Remove odd index values
print("----------------7.Remove odd index values--------------------")

remove_odd_values = "program to remove a newline in Python"
length = len(remove_odd_values)
even_values = ""
for i in range(length):
    if i%2 == 0:
        even_values = even_values + remove_odd_values[i]
print(even_values)
   # While Loop
even_val = ""
count = 0
while count < length:
    if count%2 == 0:
        even_val = even_val + remove_odd_values[count]
    count += 1
print(even_val)

#  8.Count words in a string
print("----------------8.Count words in a string--------------------")

count_word = "program to remove a newline in Python"
length = (count_word.split())
print("Normal  count words:",len(length))
    # While loop
count = 0
while count < len(length):
    count += 1
print("While Loop count words:",count)
    # For loop
count_1 = 0
for i in length:
    count_1 += 1
print("For loop count words:", count_1)

# 9.Upper lower case of a string
print("----------------9.Upper lower case of a string--------------------")

Upper_lower = "Upper lower case of a string"
print(Upper_lower.upper())
print(Upper_lower.lower())

# 10.Last part of string
print("----------------10.Last part of string--------------------")

Last_part = "count words"
print(Last_part[len(Last_part)-1])

