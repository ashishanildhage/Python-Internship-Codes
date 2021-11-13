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
# # for i,c in enumerate(s1):
# #     res+=s1[i]+s2[i]
# # print(res)

# for c1,c2 in zip_longest(s1,s2):#returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together, and then the second item in each passed iterator are paired together etc.
#     res+=c1+c2
# print(res)