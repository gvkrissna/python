# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 16:14:53 2020

@author: gvkri
"""

# Print Word start with 's' or 'S'
st='Sam print only the word the start with s in this sentence'
for word in st.split():
    if (word[0]=='s' or word[0]=='S'):  
        print(word)
for word in st.split():
    if (word[0].lower()=='s'):  
        print(word)       
# Print Even numbers between 1 & 10
for num in range(1,11,2):
    print(num)
#List of Number between 1 & 151 divisible by 3
print([x for x in range(1,51) if x%3 == 0])

#Print the word that has even number in the letters
st="print the every work in this sentence that has even number of letters"
for word in st.split():
    if(len(word)%2==0):
        print(word + 'is even!')
#Print integers from 1 to 100. But multiples of 3 with Fizz and Multiples of 5 with "Buzz". Multipels of 3 & 5 with FizzBuzz
for num in range(1,100):
    if(num%3==0 and num%5==0):
        print('FizzBuzz')
    elif(num%3==0):
        print('Fizz')
    elif(num%5==0):
        print('Buzz')
    else:
        print(num)
#First Letters of every word in the string
st="create a list of the first letters of every word in this string"
print([word[0] for word in st.split()])
        