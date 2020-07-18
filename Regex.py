import re
phoneNumRegex = re.compile(r'\d\d\d\d-\d\d\d\d\d\d\d')
first_number = phoneNumRegex.search('My number is 0550-7041519, her number is 0550-7037656.')
numbers = re.findall(phoneNumRegex, 'My number is 0550-7041519, her number is 0550-7037656.')
print('First Phone Number found: ' + first_number.group())
print('All Numbers are: ' + ', '.join(numbers))

