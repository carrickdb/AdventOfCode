



# numNice = 0
#
# with open("input") as f:
#     for line in f:
#         pairs = {}
#         between = False
#         pairOfPairs = False
#         string = line.strip()
#         # string = "ieodomkazucvgmuy"
#         for i in range(len(string)-1):
#             if i > 0 and string[i-1] == string[i+1]:
#                 between = True
#             if string[i:i+2] in pairs:
#                 firstIndex = pairs[string[i:i+2]]
#                 if firstIndex != i-1:
#                     pairOfPairs = True
#             else:
#                 pairs[string[i:i+2]] = i
#         numNice += pairOfPairs and between
#
# print(numNice)



# numNice = 0
#
# with open("input") as f:
#     for line in f:
#         string = line.strip()
#         seenVowels = [0 for i in range(5)]
#         vowels = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}
#         double = False
#         forbiddenStrings = set(["ab", "cd", "pq", "xy"])
#         forbidden = False
#         for i in range(len(string)):
#             curr = string[i]
#             if curr in vowels:
#                 seenVowels[vowels[curr]] += 1
#             if i < len(string)-1:
#                 if string[i] == string[i+1]:
#                     double = True
#                 if string[i:i+2] in forbiddenStrings:
#                     forbidden = True
#                     break
#         nice = double and sum(seenVowels) >= 3 and not forbidden
#         print(nice)
#         numNice += nice
#
# print(numNice)
