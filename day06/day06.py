import math 
answer1=0
answer2=0

with open("day06/input.txt",'r') as input:
# with open("day06/test.txt",'r') as input:
    lines=input.read().splitlines()

N = len(lines[-1].split())
problem = [[] for _ in range(N)]

for line in lines:
    bits = line.split()
    if line.split()[0][0] not in '0123456789':
        ops = bits
        break
    if len(bits) != N:
        raise ValueError("Must have N bits")
    for i, a in enumerate(bits):
        problem[i].append(a)

for i in range(N):
    if ops[i]=='+':
        answer1+=sum([int(x) for x in problem[i]])
    elif ops[i]=='*':
        answer1+=math.prod([int(x) for x in problem[i]])


nums=[]
print('Ops', lines[-1])
skip = False
for i in range(len(lines[-1])-1,-1,-1):
    if skip:
        skip=False
        continue 
    num=''
    for j, line in enumerate(lines[:-1]):
        num+=line[i]
    if num.strip():
        nums.append(int(num))
    else:
        print('Huh?')
    if lines[-1][i]=='+':
        print(' + '.join([str(num) for num in nums]), " = ", sum(nums))
        answer2+=sum(nums)
        skip=True
        nums=[]
    elif lines[-1][i]=='*':
        print(' * '.join([str(num) for num in nums]), " = ",math.prod(nums))
        answer2+=math.prod(nums)
        skip=True
        nums=[]
    elif lines[-1][i]==' ':
        pass
    else:
        raise RuntimeError("Argh")
    
# Guess
# 12608160008122
# 12608160010122

print(answer1,answer2)
