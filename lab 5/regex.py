import re
## Python RegEx exercises

#1. Write a Python program that matches a string that has an `'a'` followed by zero or more `'b'`'s.
data = input()
target=re.findall("ab*", data)
if target != 0:
    print("True")
else:
    print("False")
print(target)

#2. Write a Python program that matches a string that has an `'a'` followed by two to three `'b'`.
#data = input()
target = re.findall("ab{2,3}", data)
if target != 0:
    print("True")
else:
    print("False")
    
#3. Write a Python program to find sequences of lowercase letters joined with a underscore.
#data = input()
target = re.findall("[a-z]+_+[a-z]+", data)
if target != 0:
    print("True")
else:
    print("False")
    
#4. Write a Python program to find the sequences of one upper case letter followed by lower case letters.
#data = input()
target = re.findall("[A-Z]+[a-z]+", data)
if target != 0:
    print("True")
else:
    print("False")

#5. Write a Python program that matches a string that has an `'a'` followed by anything, ending in `'b'`.
#data = input()
target=re.findall("a.*b", data)
if target != 0:
    print("True")
else:
    print("False")
    
#6. Write a Python program to replace all occurrences of space, comma, or dot with a colon.
#data = input()
target = re.sub(r'[ ,.]', ':', data)
print(target)

#7. Write a python program to convert snake case string to camel case string.
#data = input()
target = re.sub(r'_([a-z])', lambda m: m.group(1).upper(), data)

print(target)

#8. Write a Python program to split a string at uppercase letters.
#data = input()
target =  re.findall('[A-Z][^A-Z]*', data)

print(target)

#9. Write a Python program to insert spaces between words starting with capital letters.
#data = input()
target = re.sub(r'(?<!^)(?=[A-Z])', ' ', data)

print(target)

#10. Write a Python program to convert a given camel case string to snake case.
#data = input()
target = re.sub(r'(?<!^)(?=[A-Z])', '_', data).lower() 

print(target)