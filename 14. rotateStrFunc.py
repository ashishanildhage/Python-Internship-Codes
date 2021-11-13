# #write a program to rotate the string -  Wrong code : Left and right shift operators are bitwise not character wise
# s=input("Enter the string : ")
# choice = input("Enter L or R to rotate : ")
# def rotate(string,choice):
#     if choice == "L":
#         string<<1
#         return string
#     elif choice == "R":
#         string>>1
#         return string
# out = rotate(s,choice)
# print(out)

#this is how u write a code which is testable - neat and clean
def rotateLeftOnce(s):
    return s[-1]+s[:-1]
#always have 1 line gap between 2 functions - design standard rules for coding
def rotateRightOnce(s):
    return s[1:]+s[0]

def rotate(s,direction,times):
    for i in range(0,times):
        if direction.upper() == "L":
            s=rotateLeftOnce(s)
        elif direction.upper() == "R":
            s=rotateRightOnce(s)
    return s #dont forget to add return s in function code. 

s=input("Enter the string : ")
choice = input("Enter L or R to rotate : ")
times = int(input("Enter the number of times : "))
print(rotate(s,choice,times))

'''programmer and software developer are different roles. programmer - how ever u do, work must be done with. developer - code must be neat and clean and should be fast and testable
requirements specifications - functional and non functional requirements
non- func req - speed performance code size improving
functions in python are first class objects - one can assign a function to a variable
'''