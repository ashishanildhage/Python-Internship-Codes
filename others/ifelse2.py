# #enter times the name and should display in 2 columns
# name=input("Enter name : ")
# times=int(input("Enter Times : "))
# columns=2
# i=1
# while i<=times:
#     j=0
#     while j<columns:
#         print(f"{i}. {name}  ",end="")
#         j+=1
#         i+=1
#         if i==times-1:
#             break
#     print("")

# #----------------------
# #Enter numbers and if non number then exit and add all given input numbers
# num=input("Enter number : ")
# i=0
# adder=0
# while num:
#     if '0'<=num[i]<='9':
#         adder = adder + num[i]
#     i+=1
# print(adder)

# #2nd try
# sum=0
# user_input=input("Enter a number or q to exit\n")
# while user_input!='q':
#     if '0'<=user_input<='9':#checks only if first character is digit or not,but we think it checks the whole thing
#         sum+=int(user_input)
#     user_input=input("Enter number again")
# print(f"sum={sum}")

# #correct prpgram 3rd try
# #try and except is used to first run the code and then if any error is shown then we shall handle it seperately later
# sum=0
# user_input=input("Enter a number or q to exit\n")
# while user_input!='q':
#     try:
#         num=eval(user_input) #eval - evaluates any valid python string to int or float or etc depending on input
#         sum+=num
#     except Exception as e:
#         print("Non-number given")
#     user_input=input("Enter input : ")
# print(f"sum={sum}")


