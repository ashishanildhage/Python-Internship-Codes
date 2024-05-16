# name="ashish dhage"
# for output in name:#output is new variable created which gets one by one characer from name and then prints
#     print(output) # in for loop you only get one character at a time inside the output variable

# #write a program to check if string has only vowels
# string=input("Enter the string : ")
# vowels="aeiou"
# for output in string: #use "in" always because if u use =="aeiou", then it checks first char "a" if equal to "aeiou", hence it tells to check the char seperately in every char of other string rather than together
#     if output.lower() in vowels: #output every character gets converted to lower case so not a problem
#         print("",end="")
#     else:
#         print("not vowels")
#         break
# else: #remember to use else in while or even for loop if while loop exits correctly
#     print("yes they are all vowels")

# string=input("Enter the string : ")
# vowels="aeiou"
# res=""
# for output in string:
#     if output.lower() in vowels:
#         res+=output 
# print(res)

# #"   ab cd    " to "ab cd"
# str=input("Enter the string : ")
# for outstr in str:
#     if str!=" ":
#         pass
# s="hello"
# for i,j in enumerate(s):#takes one element as well as the index it holds position in and passes it ahead
#     print(i,j)

# #abcdef to AbCdEf
# s=input("Enter the string : ")
# res=""
# for i,c in enumerate(s):
#     if c==" ":
#         res+=" "+s[i+1].lower()
#     else:
#         if i%2==0:
#             c=c.upper()
#         res+=c
# print(res)

# s=input("Enter the string : ")
# res=""
# for i,c in enumerate(s):
#     if i%2==0 and c!=" ":
#         c=c.upper()
#     res+=c
# print(res)

# #write program to print pattern ---> very good correct code
# #    * 
# #   * *
# #  * * * 
# # * * * *
# i=1
# while i!=5:
#     print((5-i)*" ",i*"* ")
#     i+=1

# rows=4
# for row in range(rows+1):
#     for i in range(row):
#         print(" "*(rows-row)+"* "*row,end="  ")
#     print(" ")

#write a program to combine 2 strings - abc and cde into acbdce - wrong code
str1="abc"
str2="cde"
i=0
res=""
while i!=len(str1):
    for res in str1+str2:
        res+=(str1+str2)[i]+(str1+str2)[i+len(str1)-1]
        i+=1
print(res)

from itertools import zip_longest
s1="abc"
s2="cde"
res=""
for i,c in enumerate(s1):
    res+=s1[i]+s2[i]
print(res)

for i in range(len(s1)):
    res+=s1[i]+s2[i]
print(res)

for c1,c2 in zip_longest(s1,s2):#returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together, and then the second item in each passed iterator are paired together etc.
    res+=c1+c2
print(res)

