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

highest_value = 0

for key, value in dic.items():
   if value > highest_value:
       highest_key, highest_value = key, value

print(highest_key, highest_value)
