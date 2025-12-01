answer1=-1
answer2=-1

with open("day01/input.txt",'r') as input:
    lines=input.read().splitlines()
dial=50
pw=0
pw2=0
for line in lines:
    dir = -1 if line[0]=='L' else 1
    amount = int(line[1:])

    if dial==0 and dir==-1:
        pw2-=1

    dial += dir*amount

    pw2+=abs(dial // 100)
    if dial % 100 ==0 and dir==-1:
        pw2+=1
    


    dial %= 100
    print(dial,pw)
    if dial==0:
        pw+=1

answer1=pw
answer2=pw2


print(answer1,answer2)