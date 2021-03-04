fhand = open('mbox.txt')

dic = dict()

for line in fhand:
    if not line.startswith('From'):
        continue
    elif line.startswith('From:'):
        continue
    else:
        line.rstrip()
        words = line.split()
        email = words [1]
        name, domain = email.split('@')
        dic[name] = dic.get(name ,0 ) + 1

lst = list()

for key, val in dic.items():
    lst.append((val, key))

lst.sort(reverse=True)
for key, val in lst:
    print(key, val)

    