# #abcdef to AbCdEf - wrong code if you include space in the string
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

# #correct program
# s=input("Enter the string : ")
# res=""
# for i,c in enumerate(s):
#     if i%2==0 and c!=" ":
#         c=c.upper()
#     res+=c
# print(res)

# #-----------------------
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

# #-------------------------
# #write a program to combine 2 strings - abc and cde into acbdce - wrong code
# str1="abc"
# str2="cde"
# i=0
# res=""
# while i!=len(str1):
#     for res in str1+str2:
#         res+=(str1+str2)[i]+(str1+str2)[i+len(str1)-1]
#         i+=1
# print(res)

# from itertools import zip_longest
# s1="abc"
# s2="cde"
# res=""
# for i,c in enumerate(s1):
#     res+=s1[i]+s2[i]
# print(res)

# for i in range(len(s1)):
#     res+=s1[i]+s2[i]
# print(res)

# for c1,c2 in zip_longest(s1,s2):#returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together, and then the second item in each passed iterator are paired together etc.
#     res+=c1+c2
# print(res)