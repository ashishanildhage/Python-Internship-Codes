import os
os.getcwd()#get current working directory
# to create file in directory
f=open("data.txt","w") #write type 
print("Ashish Dhage",file=f,flush=True) #prints to a stream - file like object in sys.stdout not on screen
f.close() #Always close file since the file stays in RAM when u write and doesnt return back to harddisk.
#or instead of closing use flush. But flush is slow because saving/printing on harddisk is much slower than on RAM. Eg: Autosavefile every 5 mins
#if file is reopened & printed & closed then it gets overwritten

