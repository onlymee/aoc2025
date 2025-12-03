answer1=0
answer2=-1

with open("day03/input.txt",'r') as input:
    lines=input.read().splitlines()
# lines=[
# "987654321111111",
# "811111111111119",
# "234234234234278",
# "818181911112111"]
for line in lines:
    bank = [int(c) for c in line]
    print(bank)
    cell1=max(bank[:-1])
    p1=bank.index(cell1)
    cell2=max(bank[p1+1:])
    print(f"{cell1}{cell2}")
    jolt = int(f"{cell1}{cell2}")
    answer1+=jolt


print(answer1,answer2)
