#Format Speciifiers in Print Statement
age=input("Enter age\n")
name=input("Enter name\n")

#Dont use, ugly
msg="Your name is %s and your age is %s."%(name,age)
print(msg)

#was used before not now
msg1="Your name is {1} and your age is {0}.".format(age,name)
print(msg1)

#this works is python 3.6+ so use this only always
# here f after msg2= is necessary to tell it that
# it is format specifier and is a string.
msg2=f"Your name is {name} and your age is {age}."
print(msg2)

