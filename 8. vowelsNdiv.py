# #character is vowel or not(wrong -> in expression, true is not equal to true only for "a" because python evaluates last computed expression, hence only a os vowel not others like e i o u)
# char = "u"
# print("Not Vowel" if char!=("a" or "e" or "i" or "o" or "u") else "Vowel")

# #Vowel or not
# char=(input("Enter Character"))
# alpha="a"<=char<="z" or "A"<=char<="Z"
# vowels="aeiouAEIOU,.$#!"
# if alpha: # dont write char==alpha or char in alpha becuse alpha already has char variable and has checked if true or not before itself
#     print(f"'{char}' is a Vowel" if char in vowels  else "Not Vowel") if char else print("empty")
#     print("vowel" if char=="a" or char=="e" or char=="i" or char=="o" or char=="u" else "Not Vowel")
# else:
#     print("Not an Alphabet")

# #------------------------------    
# #number is divisible by 3 and/or 7 (correct but if dont use elif and use only if then write num%3!=0 and num%7==0 instead of only num%7==0 in elif)
# num=int(input("Enter Number\n"))
# print("divisble by 3 & 7" if num%3==0 and num%7==0 else ( "divisble by 3" if num%3==0 and num%7!=0 else ("divisible by 7" if num%7==0 and num%3!=0 else "not divisible by 3 or 7")))

# #------------------------------
# #write a program to check if string has only vowels
# string=input("Enter the string : ")
# vowels="aeiou"
# for output in string: #use "in" always because if u use =="aeiou", then it checks first char "a" if equal to "aeiou", hence in tells to check the char seperately in every char of other string rather than together
#     if output.lower() in vowels: #output every character gets converted to lower case so not a problem
#         print("",end="")
#     else:
#         print("not vowels")
#         break
# else: #remember to USE ELSE IN WHILE OR EVEN FOR LOOP if loop exits correctly
#     print("yes they are all vowels")
# #Additional program to display only vowels from the input
# res=""
# for output in string:
#     if output.lower() in vowels:
#         res+=output 
# print(res)