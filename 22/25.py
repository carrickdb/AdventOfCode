total = 0

with open("input") as f:
    for line in f:
        line = line.strip()
        curr = 0
        currTotal = 0
        for c in line[::-1]:
            if c == "-":
                currTotal += -1 * pow(5, curr)
            elif c == "=":
                currTotal += -2*pow(5,curr)
            else:
                currTotal += int(c)*pow(5,curr)
            curr += 1
        total += currTotal

print(total)

res = [0 for _ in range(20)]
curr = 0
while total // 5 < total:
    rem = total % 5
    if rem == 4:
        res[len(res)-curr-1] -= 1
        res[len(res)-curr-2] += 1
    elif rem == 3:
        res[len(res)-curr-1] -= 2
        res[len(res)-curr-2] += 1
    else:
        res[len(res)-curr-1] += rem

    total //= 5
    curr += 1

for i in range(len(res)):
    if res[i] == -1:
        res[i] = '-'
    elif res[i] == -2:
        res[i] = '='
    else:
        res[i] = str(res[i])

print(''.join(res))


"""
23:
125 25 5 1
       1 =
    1  -
    1  0 =

20:
         0
    1 -1

19:
       1 -
     1 =
     1 -1 -1

54
       1 -
     2

3125 625 125 25 5 1
                  0
              1 =
              0
      1   -1
      2
  1
13-1=0

-x^10 -2x^9+x^8


              0
         1 -2
       0
  1 -1
 2
1

guesses:
2-21=02=1-121-1-11-0

"""
