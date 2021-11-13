#PROGRAM SHOULD CORRECT GUESS THE NUMBER IN YOUR MIND

# #bruteforce prediction means 0,1,2,3,4,5,6,7,8,9,10,11....
# #divide and conquer binary search means < or > 50
# #these are searching and sorting algorithm - Minimum spanning tree, game theory, find the best path

# #Correct Program to guess the number in your mind.
# tries_left=7
# low=0
# high=100
# while tries_left:
#     tries_left-=1
#     guess=(high+low)//2 #if u dont want floating divided values then use // instead of / to get int answer
#     print(f"My guess is {guess}")
#     user_input=input("Enter <,> or = : ")
#     if user_input=='=':
#         print(f"The number is {guess}. I win!")
#         break
#     elif user_input=="<":
#         high=guess
#     elif user_input==">":
#         low=guess
# else: #in while else, else part if while exits abruptly by break then it will not execute else statement, otherwise in normal exit, it will enter else part
#     print("You Lost! Out of Guesses.")#this is called boundery value edge case testing, where even if 0 is guessed correct then it shows lost
# #You can also add else print lost inside the while loop but code wont look elegant, since 2 breaks in a loop.


#----------------------    
#if input is ashish dhage, then output should be Ashish Dhage - perfectly correct output good
user_input=input("Enter your name : ")
output=user_input[0].upper()
i=1
while len(user_input)!=i:
    if user_input[i]==" ":
        output+=user_input[i]+user_input[i+1].upper()
        i+=1#append twice here to skip the next character
    else:
        output+=user_input[i]
    i+=1
print(output)

#we can also find the space in the name and then slice the name to 2 strings and then upper the first variable
#get index of space
s="ashish   dhage"
space_index=0
while s[space_index]!=" ":
    space_index+=1
#slicing method using upper()
print(s[0].upper()+s[1:space_index]+" "+s[space_index+1].upper()+s[space_index+2:])
#title function 
print(s.title())
#without using upper function but instead chr and ord number link conversions. minus 32 gives the capital value of any small letter
print(chr(ord(s[0])-32)+s[1:space_index]+" "+chr(ord(s[space_index+1])-32)+s[space_index+2:])

#but remember for slicing method i/p - ashish    dhage, o/p will be Ashish    dhage, hence challengingly wrong




