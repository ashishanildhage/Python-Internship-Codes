#Count the number of vowels
count=0
for i in input("Enter the string : "):
    if i!=" ":
        if i == "a" or i=="e" or i=="i" or i=="o" or i=="u":
            count+=1
print(count)
