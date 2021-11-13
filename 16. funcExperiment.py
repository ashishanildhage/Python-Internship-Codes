#Print Case Functions :
def name():
    print("Ashish")
    
name # >>>
name() # >>>Ashish
print(name) # >>><function name ___ >
print(name()) # >>>Ashish {\n} None
p=name # >>> 
p=name() # >>>Ashish
p()=name # >>>Error:Cannot assign to function call
p()=name() # >>>Error:Cannot assign to function call

p=name; p # >>>
p=name; p() # >>>Ashish
p=name(); p # >>>Ashish 
p=name(); p() # >>>Ashish {\n} Error:'Nonetype' object is not callable

p=name; print(p) # >>><function name ___>
p=name; print(p()) # >>>Ashish {\n} None
p=name; print(name) # >>><function name ___>
p=name; print(name()) # >>>Ashish {\n} None
p=name(); print(p) # >>>Ashish {\n} None
p=name(); print(p()) # >>>Ashish {\n} Error:'Nonetype' object not callable
p=name(); print(name) # >>>Ashish {\n} <function name ___>
p=name(); print(name()) # >>>Ashish {\n} Ashish {\n} None

#--------------------------------
#Return Case Functions:
def name():
    return "Ashish"

name # >>>
name() # >>>
print(name) # >>><function name ___>
print(name()) # >>>Ashish
p=name # >>>
p=name() # >>>
p()=name # >>>Error:Cannot assign to function call
p()=name() # >>>Error:Cannot assign to function call

p=name; p # >>>
p=name; p() # >>>
p=name(); p # >>>
p=name(); p() # >>>Error:'str' object is not callable

p=name; print(p) # >>><function name ___>
p=name; print(p()) # >>>Ashish
p=name; print(name) # >>><function name ___>
p=name; print(name()) # >>>Ashish 
p=name(); print(p) # >>>Ashish 
p=name(); print(p()) # >>>Error:'str' object not callable
p=name(); print(name) # >>><function name ___>
p=name(); print(name()) # >>>Ashish
