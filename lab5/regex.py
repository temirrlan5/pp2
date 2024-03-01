#ex1
import re

a = input()
s = re.findall("ab*", a)
print(s)


#ex2
import re

def match_pattern(text):
    pattern = 'ab{2,3}' 
    if re.fullmatch(pattern, text):
        return True
    else:
        return False
    
#ex3
import re

a = input()
s = re.findall(r'[a-z]+_[a-z]+', a)
for x in s:
    print(x)
    
#ex4
import re

a = input()
s = re.findall(r'[A-Z][a-z]+', a)
for x in s:
    print(x)
    
#ex5
import re

def match_pattern(text):
    pattern = 'a.*b$'  # 'a' followed by anything, ending in 'b'
    if re.match(pattern, text):
        return True
    else:
        return False
    
#ex6
import re

a = input()
s = re.sub(r'[ ,.]', ':', a)
print(s)

#ex7
def sn_to_cam(sn_str):
    common_str=sn_str.split('_')
    cam_str=common_str[0]+''.join(word.capitalize() for word in common_str[1:])
    return cam_str
s=input()
print(sn_to_cam(s))

#ex8
a = input()
s = re.split(r'([A-Z])', a)
print(s)

#ex9
import re

def insert_spaces(text):
    modified_text = re.sub(r'(?<!^)(?=[A-Z])', ' ', text)
    return modified_text

a = input()
output_text = insert_spaces(a)
print(output_text)

#ex10
def camel_to_snake(camel_case):
    snake_case = ''
    for char in camel_case:
        if char.isupper():
            snake_case += '_' + char.lower()
        else:
            snake_case += char
    return snake_case.lstrip('_') 

camel = input()
snake =camel_to_snake(camel)
print(snake)
