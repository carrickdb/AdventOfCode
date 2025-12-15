
"""
???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1
"""

memos = {}

def rec(r, nums):
    # ?###???????? 3,2,1
    tupnums = tuple(nums)
    if r in memos and tupnums in memos[r]:
        return memos[r][tupnums]
    if len(nums) == 0:
        if "#" in r:
            # print("returning 0 since # in r for", r, nums)
            return 0
        return 1
    if "?" not in r and "#" not in r:
        # print("returning 0 since ? not in r and # not in r for", r, nums)
        return 0
    currn = nums[0]
    res = 0
    for i in range(len(r)):
        if i+currn <= len(r):
            substr = r[i:i+currn]
            if "." not in substr:
                if i+currn < len(r) and r[i+currn] == "#":
                    continue
                res += rec(r[i+currn+1:], nums[1:])
    if r not in memos:
        memos[r] = {}
    memos[r][tupnums] = res
    return res

total = 0
with open("input2-12") as f:
    for l in f:
        row, nums = l.strip().split()
        nums = list(map(int, nums.split(",")))
        res = rec(row, nums)
        print(res)
        total += res
        # break

print(total)





# with open("input2-12") as f:
#     for l in f:
#         row, nums = l.strip().split()
#         nums = list(map(int, nums.split(",")))
#         lennums = len(nums)
#         lenrow = len(row)
#         dp = [[1]]
#         seen = False
#         for c in row[::-1]:
#             if c=='#':
#                 seen = True
#             if seen:
#                 dp[0].append(0)
#             else:
#                 dp[0].append(1)
#         for n in nums[::-1]:
#             cn = n
#             dp.append([0])
#             res = None
#             for i in range(len(row)):
#                 curr = len(row)-i-1
#                 currchar = row[curr]
#                 if currchar == "#":
#                     cn -= 1
#                     if cn == 0:
#                         res = dp[-1][-1]
#                     else:
#                         res = 0
#                 elif currchar == ".":
#                     if cn > 0:
#                         res = 0
#                     else:
#                         res = dp[-1][-1]
#                 else:
#                     res = dp[-1][-1]
#                     if cn > 0:
#                         res += dp[-2][len(row)-i]
#                 if res == None:
#                     print("something went wrong")
#                     exit()
#                 dp[-1].append(res)
#         break

# for i in dp:
#     print(i)
# print(dp[-1][-1])


# def getcombos(row, nums):
#     # print(row, nums)
#     if len(nums) == 0:
#         if all([x!="#" for x in row]):
#             return 1, [row]
#         return 0, []
#     if nums[0] > len(row):
#         return 0, []
#     currnum = nums[0]
#     count = 0
#     ways = []
#     for i in range(len(row)-currnum+1):
#         last = i+currnum
#         if "." in row[i:last]:
#             continue
#         if (i-1 < 0 or row[i-1] != "#") and (last >= len(row) or row[last] != "#"):
#             # if currnum == 2:
#             #     print("found", row[:last+1], "checking", row[last+1:])
#             currcount, newways = getcombos(row[last+1:], nums[1:])
#             count += currcount
#             for nw in newways:
#                 newstr = ''.join(["#" for _ in range(currnum)])
#                 if last < len(row):
#                     newstr += row[last]
#                 ways.append(f"{row[:i]}{newstr}{nw}")
#         if row[i] == "#":
#             break
    # return count, ways

# def getcombos(row, nums):
#     if len(nums) == 0:
#         if all([x!="#" for x in row]):
#             return 1
#         return 0
#     if nums[0] > len(row):
#         return 0
#     currnum = nums[0]
#     count = 0
#     for i in range(len(row)):
#         last = i+currnum
#         if last > len(row):
#             break
#         if "." in row[i:last]:
#             continue
#         if (i-1 < 0 or row[i-1] != "#") and (last >= len(row) or row[last] != "#"):
#             count += getcombos(row[last+1:], nums[1:])
#         if row[i] == "#":
#             break
#     return count

# expectedAnswers = [1,4,1,1,4,10,3,2,3,4]
# actualAnswers = []
# with open("input2") as f:
#     total = 0
#     for l in f:
#         row, nums = l.strip().split()
#         nums = list(map(int, nums.split(",")))
        
#         currtotal = getcombos(row, nums)
#         # currtotal, ways = getcombos(row, nums)
#         # for w in ways:
#         #     print(w)
#         print(currtotal, end=",")
#         actualAnswers.append(currtotal)
#         total += currtotal
#         # print()

# print(actualAnswers == expectedAnswers)
# print(actualAnswers)
# print(total)


# # too high:
# # 9789
# # 8295