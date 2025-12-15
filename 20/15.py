

start = [1,20,11,6,12,0]
said = {}
i = 1
for num in start:
    said[num] = i
    i += 1

prev = start[-1]
while True:
    curr = None
    if prev in said:
        curr = i-1-said[prev]
    else:
        curr = 0
    said[prev] = i-1
    if i == 30000000:
        print(curr)
        break
    # print(i, curr)
    # if i == 20:
    #     break
    prev = curr
    i += 1
