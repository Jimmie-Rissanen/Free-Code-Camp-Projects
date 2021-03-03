fhand = open('mbox.txt')

count = 0
emails = []
for line in fhand:
    if not line.startswith('From') or len(line) < 0:
        continue 
    else:
        count = count + 1
        li = line.split()
        lis = li [1]
        emails.append(lis)

print(emails, count)