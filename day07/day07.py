from functools import lru_cache
answer1=0
answer2=0

with open("day07/input.txt",'r') as input:
# with open("day07/test.txt",'r') as input:
    lines=input.read().splitlines()


grid={}
maxr=0
for row,line in enumerate(lines):
    for col,ch in enumerate(line):
        if ch=='S':
            start = (row,col)
        if ch=='^':
            grid[(row,col)]='^'
            maxr=max(row,maxr)

def beamsplit(s):
    r,c = s
    if r > maxr:
        return 0
    
    while r<=maxr:
        r2=r+1
        if grid.get((r2,c))=='^':
            splits=[]
            if viewgrid.get((r2,c-1))!='|':
                viewgrid[(r2,c-1)]='|'
                splits.append((r2,c-1))
            if viewgrid.get((r2,c+1))!='|':
                viewgrid[(r2,c+1)]='|'
                splits.append((r2,c+1))

            return 1 + sum([beamsplit(sp) for sp in splits])
            
        if viewgrid.get((r2,c)):
            return 0
        viewgrid[(r2,c)] = '|'
        r=r2
    return 0

@lru_cache
def beamsplit2(s):
    r,c = s
    if r > maxr:
        return 0

    while r<=maxr:
        r2=r+1
        if grid.get((r2,c))=='^':
            return beamsplit2((r2,c-1)) + beamsplit2((r2,c+1))
            
        r=r2
    return 1


viewgrid=grid.copy()
answer1 = beamsplit(start)
answer2 = beamsplit2(start)
print(answer1,answer2)
