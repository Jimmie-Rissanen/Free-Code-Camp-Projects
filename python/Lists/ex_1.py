def chop(t):
    t.pop(-1)
    t.pop(0)

def middle(t):
    return t[1:-2]

li = [1,2,3,4,5,6,7,8]

print(li)

chop(li)

print(li)

rest = middle(li)

print(rest)
