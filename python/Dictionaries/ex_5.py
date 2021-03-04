fhand = open('mbox.txt')

dic = dict()

for line in fhand:
    if not line.startswith('From') or len(line) < 0:
        continue
    elif line.startswith('From:'):
        continue
    else:
        line.rstrip()
        words = line.split()
        email = words[1]
        email_split = email.split('@')
        domain = email_split [1]
        dic[domain] = dic.get(domain,0) + 1

count = 0

for key, value in dic.items():
    if value > count:
        count = value
        most , highest = key, value
print(f'The most fequent sender is {most}, who sent {highest} amout of emails.')
print(dic)
