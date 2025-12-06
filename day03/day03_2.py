from functools import lru_cache

answer1=0
answer2=0
def l2b(l):
    return ''.join([str(i) for i in l])

with open("day03/input.txt",'r') as input:
    lines=input.read().splitlines()
# lines=[
# "987654321111111",
# "811111111111119",
# "234234234234278",
# "818181911112111"]

@lru_cache
def findmax(bank,size) -> str:
    ll=len(bank)
    cell = max(list(bank[:ll-size+1]))
    if size==1:
        return cell
    cellp = [ i for i,c in enumerate(bank[:ll-size+1]) if c==cell]
    choices = [int(cell + findmax(bank[pos+1:],size-1)) for pos in cellp]
    
    return str(max(choices))

for line in lines:
    answer1 += int(findmax(line,2))
    answer2 += int(findmax(line,12))

print(answer1,answer2)
