# This syntax made me think. Why is the output of this code the number of lines in the file?
# Turns out that python just reads one line at a time, and since this code does not do anything except counting, this is the output.
#mbox = open ('mbox.txt')
#count = 0
#for line in mbox:
#    count = count + 1
#print(count)
# Make a new file by giving the varible "fil" the value open and name a file that do not exist. 
# Add 'w' to make a opened file writeable
#fil = open('mbox.txt', 'w')

# I started this task thinking I need a for looop. After reading about .read I realized I can store the whole file in a variable if it fits in workingmemory.
text = open('mbox_short.txt')
read = text.read()
#for line in text:
    
upper = read.upper()

print(upper)

