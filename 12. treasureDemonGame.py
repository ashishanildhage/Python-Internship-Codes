state1='''
       ---------
       | D | T |
       ---------
       |   | P |
       ---------
       '''
state2='''
       ---------
       | D | T |
       ---------
       | P |   |   
       ---------
       '''
state3='''
       ---------
       | D | T |
       ---------
       |   |   |
       ---------
       '''
state4='''
       ---------
       | D | P |
       ---------
       |   |   |
       ---------
       '''
move=input("Enter move U,R,L,D\n")
if move=='L':
    print(state2)
    move=input("enter the move")
    if move=='U':
        print(state3)
        print("you lose")
    else:
        print("Invalid")
elif move=='U':
    print(state4);print("you win")
else:
    print("Invalid")    
