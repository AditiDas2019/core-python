
# 11.Convert a given string to all uppercase
print("----------------11.Convert a given string to all uppercase--------------------")

word = "dsvsm k.sacdscs cs cks kb c"
print(word.upper())

# 12.program to remove a newline in Python
print("----------------12.program to remove a newline in Python--------------------")

remove_new_line = "Hello\nWorld!"
print(remove_new_line.replace('\n',' '))

text = "A regular \n expression is a sequence \n of characters\n that specifies a search\n pattern."
print(text)
print(text.replace('\n', ''))

my_list = ["Python\n", "is\n", "Fun\n"]
new_list = []
print("Original List: ", my_list)
for i in my_list:
    new_list.append(i.replace("\n", ""))

# 13.program to check whether a string starts with specified characters
print("----------------13.program to check whether a string starts with specified characters--------------------")

url = "https://onthegomodel.com"
is_secure_url = url.startswith("https://")
print(is_secure_url)
URL_1 = "https;//onthegomodel.com"
is_secure_url_1 = URL_1.startswith("https://")
print(is_secure_url_1)

# 14.to set the indentation of the first line
print("----------------14.to set the indentation of the first line--------------------")

indentation = "Pyt\thon Pro\tgramming"
print(indentation)

# 15.to print the following floating numbers upto 2 decimal places
print("----------------15.print the floating numbers--------------------")
number = "13.676271253651"
number = float(number)
print(round(number,2))

# 16.print the following floating numbers upto 2 decimal places with a sign
print("----------------16.print the floating numbers--------------------")

number_1 = "13.676271253651"
number_1 = float(number_1)
print(str(round(number_1,2))+"$")

# 17.to display a number with a comma separator
print("----------------17.to display a number with a comma separator--------------------")

num = "1 2 3 4 5 6 7 8 9"
num_1 = num.replace(' ',',')
print(num_1)

# 18.to format a number with a percentage
print("----------------18.to format a number with a percentage--------------------")
number = 0.45

print('{:.2%}'.format(number))

# print(str(round((number * 100),2)) + '0%')

# name = "RAGHAVENDRA REDDY"
# Unique charecters only show this code
# count_words = 0
# sum = ''
# for i in name:
#     count_words = name.count(i)
#
#     if name.count(i) <2:
#               sum += i
# print(sum)

# 19. to count occurrences of a substring in a string
print("---------------to count occurrences of a substring in a string-----------------")
# define string
string = "Python is awesome, isn't it?"
substring = "is"

count = string.count(substring)

# print count
print("The count is:", count)

# 20. count repeated characters in a string
print("---------------20. count repeated characters in a string-----------------")

name = "RAGHAVENDRA REDDY"


for i in name:
    count_words = name.count(i)
    # if name.count(i) >1:      we are using this condition in string duplicate charectors find out only
    #     sum += i
    print(i +":",name.count(i))
name_word = "RAGHAVENDRA REDDY"
dict = {}
for j in name_word:
    keys = dict.keys()
    if j in keys:
        dict[j] += 1

    else:
        dict[j] = 1
print(dict)

