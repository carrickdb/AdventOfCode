s,e = 146810, 612564
# s,e = 111122, 111122

ret = 0
for i in range(s, e+1):
    si = list(map(int, str(i)))
    ok = True
    double = False
    for j in range(len(si)-1):
        if si[j+1] < si[j]:
            ok = False
            break
        if si[j+1] == si[j] and (j-1 < 0 or si[j-1] != si[j]) and (j+2 >= len(si) or si[j+2] != si[j]):
            double = True
    ret += ok & double
print(ret)

# ret = 0
# for i in range(s, e+1):
#     si = list(map(int, str(i)))
#     ok = True
#     double = False
#     for j in range(len(si)-1):
#         if si[j+1] < si[j]:
#             ok = False
#             break
#         if si[j+1] == si[j]:
#             double = True
#     ret += ok & double
# print(ret)