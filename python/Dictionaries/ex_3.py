fhand = open('mbox.txt')

dic = dict()

for line in fhand:
    if not line.startswith('From') or len(line) < 0:
        continue
    else:
        line.strip()
        words = line.split()
        email = words [1]
        dic[email] = dic.get(email, 0) + 1
for key in dic:
    print(f'{key} appears {dic[key]} times in the dictionary')