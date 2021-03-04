#a_file = input('Enter a file: ')
fhand = open('mbox.txt')

dic = dict()

for line in fhand:
    if not line.startswith('From') or len(line) < 0:
        continue
    elif line.startswith('From:'):
        continue
    else: 
        line.rstrip()
        word_list = line.split()
        email = word_list[1]
        dic[email] = dic.get(email,0) + 1 

highest = 0

for pair in dic:
    if dic[pair] > highest:
        highest = [dic[pair]] 

print(highest)