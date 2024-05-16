# #enter number if it has 0 then give outputs as 9 - Correct but in big projects u dont use python console to output the variable without storing it
# str=input("Enter input : ")
# i=0
# try:
#     while str:
#         print("9",end="") if str[i]=="0" else print(f"{str[i]}",end="")
#         i+=1
# except Exception as e:
#     print("")

# str1=input("Enter input : ")
# i=0
# str2=""
# try:
#     while i<len(str1):
#         str2 += "9" if str1[i]=="0" else str1[i]
#         i+=1
# except Exception as e:
#     print("")
# print(str2)

# str2=str2.replace("9","0") #str2.replace("9","0") is wrong, cant change contents of string, need to create a new string always
# print(str2)


# num=input("Enter input : ")
# i=0
# res=""
# while i<len(num):# < because last character index is -1 hence < not <=
#     c=num[i]
#     if c=="0":
#         c="9" 
#     res+=c
#     i+=1
# print(res)

