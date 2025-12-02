answer1=0
answer2=-1

with open("day02/input.txt",'r') as input:
    lines=input.read().splitlines()
# lines=["11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"]
rstrs = lines[0].split(',')
ranges=[]
for r in rstrs:
    se=r.split('-')
    ranges.append((int(se[0]),int(se[1])))
print(ranges)
invalid=set()
for rng in ranges:
    st,end = rng
    ns = len(invalid)
    for i in range(st,end+1):
        num=str(i)
        valid=True
        valid2=True
        
        ls=len(num)
        if num[:ls//2]==num[ls//2:]:
            answer1+=i
        for lls in range(ls-1,0,-1):
            if ls%lls==0:
                if num==num[:lls] * (ls//lls):
                    answer2+=i


print(answer1,answer2)
