
input = "130,126,1,11,140,2,255,207,18,254,246,164,29,104,0,224"
numElements = 256

# input = "3,4,1,5"
# numElements = 5

input = list(map(int, input.split(",")))


l = [i for i in range(numElements)]

skip = 0
curr = 0
lenl = len(l)
for length in input:
    end = curr+length
    if end <= lenl:
        l = l[:curr] + l[curr:end][::-1] + l[end:]
    else:
        d = l+l
        d = d[:curr] + d[curr:end][::-1] + d[end:]
        l = d[lenl:end] + d[end-lenl:lenl]
    curr = (curr+length+skip) % lenl
    skip += 1
print(l[0]*l[1])


# l = [i for i in range(numElements)]

# skip = 0
# curr = 0
# lenl = len(l)
# for length in input:
#     end = curr+length
#     if end <= lenl:
#         l = l[:curr] + l[curr:end][::-1] + l[end:]
#     else:
#         d = l+l
#         d = d[:curr] + d[curr:end][::-1] + d[end:]
#         l = d[lenl:end] + d[end-lenl:lenl]
#     curr = (curr+length+skip) % lenl
#     skip += 1
# print(l[0]*l[1])