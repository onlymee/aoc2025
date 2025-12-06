answer1=0
answer2=0

with open("day05/input.txt",'r') as input:
# with open("day05/test.txt",'r') as input:
    lines=input.read().splitlines()


done = False
ranges = []
ingred = set()

for line in lines:
    if line=='':
        done = True
        continue
    if not done:
        a,b = line.split('-')
        ranges.append((int(a),int(b)))
    else:
        ingred.add(int(line))


fresh=set()
for i in ingred:
    for a,b in ranges:
        if a <= i <= b:
            fresh.add(i)
            break

answer1 = len(fresh)

trimmed=set()
for a,b in ranges:
    for c,d in trimmed:
        if a<c and b>d:
            trimmed.remove((c,d))
            break
        if c<=a<=d:
            a=d+1
        if c<= b <=d:
            b=c-1
        if b<a:
            break
    if b>=a:
        trimmed.add((a,b))
    
for a,b in trimmed:
    answer2+=b-a+1

print(answer1,answer2)
