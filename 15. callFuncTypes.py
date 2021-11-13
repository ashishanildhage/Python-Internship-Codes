# you can pass a function as argument to another function
def work(f):
    f()
    
def foo():
    print("Foofoo")
    
f=foo #if the function has return then use f=foo() else if nothing is returned then use f=foo
f()
work(f)

#function inside function
def work(f):
    f()
    
def bar(): #writing a function/machine which builds another function/machine. machine manufacturing machine
    def foo():
        print("Foofoo bar")
    return foo
f=bar() 
f()