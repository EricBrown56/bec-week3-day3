# Before using Regular Expressions, we need to import the re module

import re # re module is used for regular expressions

# Regex methods/functions:

# 1. findall() function: Returns a list containing all matches. Syntax: re.findall(pattern, string): pattern: the pattern to search for, string: the string to search in. Returns a list.

# Example:

# Find how many times I used the word "and" in the string
text = "Hi my name is Travis, and I like to go and do things and stuff."
ands = re.findall(r'and', text) # r is used to specify a raw string. Always start a regex pattern with r
print(ands) # Output: ['and', 'and', 'and']
print(len(ands)) # Output: 3

# Find all hashtags in the string
post = "I LOVE # learning #Python_is_lyfe and #Regex, this is so fun! #Coder"

hashtags = re.findall(r'#', post) 
print(hashtags) # Output: ['#', '#', '#', '#']
print(len(hashtags)) # Output: 4

tags = re.findall(r'#\w+', post) # \w+ is used to match any word character (alphanumeric character plus underscore)
print(tags) # Output: ['#Python_is_lyfe', '#Regex', '#Coder']

# Find all words that start with b and end with the letter e
sentence = "Abe asked to build a bridge be but he was told 'beware of the heehives'"

bes = re.findall(r'\bb\w+e\b', sentence) # \b is used to match a word boundary. \w+ is used to match any word character (alphanumeric character plus underscore)
print(bes) # Output: ['bridge', 'beware']

bes2 = re.findall(r'\bb\w*e\b', sentence) # * is used to match 0 or more occurrences of the preceding character
print(bes2) # Output: ['bridge', 'be', 'beware']

# Find all email addresses in the string
text = "you can contact me at t.p@gmail.co or travis-p2@codingtemple.com, traviscpeck@email.com"

# Whats in an email address?
# username can include letters a-z, numbers 0-9, underscores, periods, and hyphens
# domain can include letters a-z, numbers 0-9, and hyphens
# domain extension needs to be only two or three characters long and can include letters a-z

# When making regex patters, break it down into parts
# username: \w+[\w.-]*
# @
# domain: \w+[\w-]*
# .
# domain extension: [a-z]{2,3}

# emails = re.findall(r'[\w.-]+@[\w.-]+', text)
emails = re.findall(r'[\w.-]+@[\w-]+\.[a-z]{2,3}', text)
print(emails)

print('='*100)

# 2. search() function: Searches the string for a match and returns a match object if there is a match. Syntax: re.search(pattern, string): pattern: the pattern to search for, string: the string to search in. Returns a match object.(first match)

# email = input("Enter your email address: ")
# found = re.search(r'[\w.-]+@[\w-]+\.[a-z]{2,3}', email)
# # print(found)
# # print(found.group()) # Output: unpack the match object to get the string that matched the pattern

# if found:
#     print(f"{found.group()} is a valid email address")
# else:
#     print("Invalid email address")

# Validating phone numbers
# We want to accept a variety of phone number formats
# 555-555-5555
# 555.555.5555
# (555)555-5555
# 5555555555

number = "My phone number is: 770 987 9876 or 770-987-9876 or 770.987.9876 or (770) 987-9876" # only finds the first occurrence the other numbers will not be looked at
phone = re.search(r'\(?\d{3}(\s|-|\))?\d{3}(\s|-)?\d{4}', number) # \d is used to match any digit (0-9)
print(phone.group())

# re.match() function: Checks for a match only at the beginning of the string. Syntax: re.match(pattern, string): pattern: the pattern to search for, string: the string to search in. Returns a match object.

text = "Hello, world!"
obj = re.match(r'Hello', text)
print(obj.group())

# check if a website is secure
url = "https://www.google.com"
secure = re.match(r'https', url)
if secure:
    print(f"{url} is a secure website")
else:
    print(f"{url} is not a secure website")

# things not found will return None which will throw an error if you try to access the group method. Use try and except to handle this

# re.split() function: Returns a list where the string has been split at each match. Syntax: re.split(pattern, string): pattern: the pattern to split at, string: the string to split. Returns a list.

text = "Python,Regex;Splitting-Example. Fun, right?"
words = re.split(r"[,;.?-]", text) # when searching dashes, put it at the end of the list
print(words[:-1])

# re.sub() function: Replaces one or many matches with a string. Syntax: re.sub(pattern, repl, string): pattern: the pattern to search for, repl: the string to replace the match with, string: the string to search in. Returns a string.

number = "(770) 880-1180"

# replace anything that is not a digit with an empty string
new_number = re.sub(r'\D', '', number) # \D is used to match any non-digit character and replace it with an empty string
print(new_number)

# anonymous chat
chat = '''
@yvebee123 : "I think I love regex"
@travisp : "I love regex too!"
@yvebee123 : "Regex is so fun!"
@travisp : "I agree!"
'''
anan_chat = re.sub(r'@\w+', '@anonymous', chat)
print(anan_chat)

