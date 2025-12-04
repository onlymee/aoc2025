answer1=0
answer2=0

with open("day04/input.txt",'r') as input:
# with open("day04/test.txt",'r') as input:
    lines=input.read().splitlines()


grid=set()

for r,line in enumerate(lines):
    for c, ch in enumerate(line):
        if ch=='@':
            grid.add((r,c))
sgrid=len(grid)

for (r,c) in grid:
    pnts = [(r+1,c),(r-1,c),(r+1,c-1),(r-1,c-1),(r,c-1),(r+1,c+1),(r-1,c+1),(r,c+1)]
    n= sum([p in grid for p in pnts])
    if n<4:
        answer1+=1

while True:
    remove=set()
    for (r,c) in grid:
        pnts = [(r+1,c),(r-1,c),(r+1,c-1),(r-1,c-1),(r,c-1),(r+1,c+1),(r-1,c+1),(r,c+1)]
        n= sum([p in grid for p in pnts])
        if n<4:
            remove.add((r,c))
    if not remove:
        break
    grid.difference_update(remove)
    answer2+=len(remove)

print(answer1,answer2)
