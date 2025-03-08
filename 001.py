'''A=int(input('enter a number'))
if A < 50 :
    print('failed')
elif A < 70 :
    print('قبول قابل')
elif A < 90 :
    print('خوب')
elif A > 90 :
    print('خوب خيلي')

B=input('enter something here') #simplest answer for num 2 question
if "a" or 'e' or 'i' or 'o' or 'u' in B : 
    print('there is a letter ')

B=input('enter something here') #a bit more complex answer to num 2 question
if 'a' in B :
    print('there is a "a"in this sentence ')
if 'e' in B :
    print('there is a "e"in this sentence ')
if 'i' in B :
    print('there is a "i"in this sentence ')
if 'o' in B :
    print('there is a "o"in this sentence ')
if 'u' in B :
    print('there is a "u"in this sentence ')

C=int(input('enter a number'))
if C % 2 == 0 :
    print('your number is even')
else :
    print('your number is odd')

a=int(input('enter your first number'))
b=int(input('enter your second number'))
c=int(input('enter your third number'))
if a**2 + b**2 == c**2:
    print('yep that the right numbers for the right tringle')
else:
    print('numebr are off for forming a right tringle')

A=(input('enter your password'))

if len(A) < 8 :
    print('enter more please')
if any(letter.isupper() for letter in A):
    print('one or more uppercase letter is in this password')
if any(letter.isdigit() for letter in A):
    print('at least is there one number in this password')
if any(letter in '@#$' for letter in A):
    print('there is @ or # or $ sign')
'''












