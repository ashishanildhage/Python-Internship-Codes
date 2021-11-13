#Function Argument in Function Case :
def work(p): p()
def name(): print("Ashish")

p=name; work(name) #>>>Ashish
p=name; work(name()) #>>>Ashish {\n} Error:'Nonetype' object not callable
p=name(); work(name) #>>>Ashish {\n} Ashish 
p=name(); work(name()) #>>>Ashish {\n} Ashish {\n} Error:'Nonetype' object not callable 
p=name; print(work(name)) #>>>Ashish {\n} None
p=name; print(work(name())) #>>>Ashish {\n} Error:'Nonetype' object not callable
p=name(); print(work(name))#>>>Ashish {\n} Ashish {\n} None 
p=name(); print(work(name())) #>>>Ashish {\n} Ashish {\n} Error:'Nonetype' object not callable

p=name; work(p) #>>>Ashish
p=name; work(p()) #>>>Ashish {\n} Error:'Nonetype' object not callable
p=name(); work(p) #>>>Ashish {\n} Error:'Nonetype' object not callable 
p=name(); work(p()) #>>>Ashish {\n} Error:'Nonetype' object not callable 
p=name; print(work(p)) #>>>Ashish {\n} None
p=name; print(work(p())) #>>>Ashish {\n} Error:'Nonetype' object not callable
p=name(); print(work(p))#>>>Ashish {\n} Error:'Nonetype' object not callable 
p=name(); print(work(p())) #>>>Ashish {\n} Error:'Nonetype' object not callable 

#---------------------------------------
#Function Argument in Function Case :
def work(p): p
def name(): print("Ashish")

p=name; work(name) #>>>
p=name; work(name()) #>>>Ashish 
p=name(); work(name) #>>>Ashish 
p=name(); work(name()) #>>>Ashish {\n} Ashish 
p=name; print(work(name)) #>>>None
p=name; print(work(name())) #>>>Ashish {\n} None
p=name(); print(work(name))#>>>Ashish {\n} None 
p=name(); print(work(name())) #>>>Ashish {\n} Ashish {\n} None

p=name; work(p) #>>>
p=name; work(p()) #>>>Ashish 
p=name(); work(p) #>>>Ashish  
p=name(); work(p()) #>>>Ashish {\n} Error:'Nonetype' object not callable 
p=name; print(work(p)) #>>>None
p=name; print(work(p())) #>>>Ashish {\n} None
p=name(); print(work(p)) #>>>Ashish {\n} None 
p=name(); print(work(p())) #>>>Ashish {\n} Error:'Nonetype' object not callable

#-----------------------------------
#Return Function Argument in Function Case :
def work(p): p()
def name(): return "Ashish"

p=name; work(name) #>>>
p=name; work(name()) #>>>Error:'Nonetype' object not callable
p=name(); work(name) #>>>
p=name(); work(name()) #>>>Error:'str' object not callable 
p=name; print(work(name)) #>>>None
p=name; print(work(name())) #>>>Error:'str' object not callable
p=name(); print(work(name))#>>>None 
p=name(); print(work(name())) #>>>Error:'str' object not callable

p=name; work(p) #>>>
p=name; work(p()) #>>>Error:'str' object not callable
p=name(); work(p) #>>>Error:'str' object not callable 
p=name(); work(p()) #>>>Error:'str' object not callable 
p=name; print(work(p)) #>>>None
p=name; print(work(p())) #>>>Error:'str' object not callable
p=name(); print(work(p))#>>>Error:'str' object not callable 
p=name(); print(work(p())) #>>>Error:'str' object not callable 

#---------------------------------------
#Return Function Argument in Function Case :
def work(p): p
def name(): return "Ashish"

p=name; work(name) #>>>
p=name; work(name()) #>>> 
p=name(); work(name) #>>> 
p=name(); work(name()) #>>>
p=name; print(work(name)) #>>>None
p=name; print(work(name())) #>>>None
p=name(); print(work(name)) #>>>None 
p=name(); print(work(name())) #>>>None

p=name; work(p) #>>>
p=name; work(p()) #>>>Ashish 
p=name(); work(p) #>>>Ashish  
p=name(); work(p()) #>>>Error:'str' object not callable 
p=name; print(work(p)) #>>>None
p=name; print(work(p())) #>>>None
p=name(); print(work(p)) #>>>None 
p=name(); print(work(p())) #>>>Error:'str' object not callable
