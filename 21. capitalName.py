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
#title function - Correct one, super quick.
print(s.title())
#without using upper function but instead chr and ord number link conversions. minus 32 gives the capital value of any small letter
print(chr(ord(s[0])-32)+s[1:space_index]+" "+chr(ord(s[space_index+1])-32)+s[space_index+2:])

#but remember for slicing method i/p - ashish    dhage, o/p will be Ashish    dhage, hence challengingly wrong