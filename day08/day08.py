import math
from collections import defaultdict
from heapq import heapify, heappush, heappop

answer1=0
answer2=0

boxes={}
N=1000
with open("day08/input.txt",'r') as input:
# N=10
# with open("day08/test.txt",'r') as input:
    lines=input.read().splitlines()

i=0
for line in lines:
    x,y,z = [int(i) for i in line.split(',')]
    boxes[i] = (x,y,z)
    i+=1

nboxes = i

def getdist(a,b): 
    x1,y1,z1 = a
    x2,y2,z2 = b
    return (x2-x1)**2+(y2-y1)**2+(z2-z1)**2

dists = list()
heapify(dists)
done = set()
for i,box1 in boxes.items():
    for j,box2 in boxes.items():
        if i==j or (box2,box1) in done:
            continue
        heappush(dists,(getdist(box1,box2), i, j))
        done.add((box1,box2))

conns=0
deleted = dict()
circ = nboxes
while conns<N and dists:
    dist, box1, box2 = heappop(dists)
    while box2 in deleted:
        box2 = deleted[box2]        

    while box1 in deleted:
        box1 = deleted[box1]        

    if box1==box2:
        conns+=1
        continue
    

    sbox1 = boxes[box1]
    sbox2 = boxes[box2]
    if isinstance(sbox1, tuple):
        sbox1=set([sbox1])
    if isinstance(sbox2, tuple):
        sbox2=set([sbox2])
    boxes[circ] = sbox1.union(sbox2)
    conns+=1
    newbox=len(boxes)-1
    deleted[box1] = circ
    deleted[box2] = circ
    circ+=1

boxes_part1 = {k: v for k,v in boxes.items() if k not in deleted}

lc = [len(box) if isinstance(box, set) else 1 for i,box in boxes_part1.items() if i not in deleted]
lc.sort()
answer1 = math.prod(lc[-3:])


while dists:
    dist, box1, box2 = heappop(dists)
    obox1,obox2 = box1,box2 
    while box2 in deleted:
        box2 = deleted[box2]        

    while box1 in deleted:
        box1 = deleted[box1]        

    if box1==box2:
        conns+=1
        continue
    

    sbox1 = boxes[box1]
    sbox2 = boxes[box2]
    if isinstance(sbox1, tuple):
        sbox1=set([sbox1])
    if isinstance(sbox2, tuple):
        sbox2=set([sbox2])
    boxes[circ] = sbox1.union(sbox2)
    if len(boxes[circ])==1000:
        break
    conns+=1
    newbox=len(boxes)-1
    deleted[box1] = circ
    deleted[box2] = circ
    circ+=1

answer2 = boxes[obox1][0] * boxes[obox2][0]

print(answer1,answer2)
