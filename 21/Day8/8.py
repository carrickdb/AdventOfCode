import itertools

segmentsToNumber = {
    ("a", 'b', 'c', 'e', 'f', 'g') : 0,
    ("c", "f") : 1,
    ("a", "c", "d", "e", "g") : 2,
    ('a', 'c', 'd', 'f', 'g') : 3,
    ('b', 'c', 'd', 'f') : 4,
    ('a', 'b', 'd', 'f', 'g') : 5,
    ('a', 'b', 'd', 'e', 'f', 'g') : 6,
    ("a", "c", "f") : 7,
    ('a', 'b', 'c', 'd', 'e', 'f', 'g') : 8,
    ('a', 'b', 'c', 'd', 'f', 'g') : 9,
}

def getOutputSum(outputs, assignments):
    numStr = ""
    for output in outputs:
        numStr += str(assignments[tuple(sorted(output))])
    return int(numStr)

def getMapping(patterns):
    segments = ["a", "b", "c", "d", "e", "f", "g"]
    for permutation in list(itertools.permutations(segments)):
        numbers = {1,2,3,4,5,6,7,8,9,0}
        works = True
        wordToNumber = {}
        for pattern in patterns:
            translation = []
            for char in pattern:
                translation.append(permutation[ord(char)-ord('a')])
            word = tuple(sorted(translation))
            if word not in segmentsToNumber or \
               segmentsToNumber[word] not in numbers:
                works = False
                break
            if not works:
                break
            numbers.discard(segmentsToNumber[word])
            wordToNumber[tuple(sorted(pattern))] = segmentsToNumber[word]
        if works:
            return wordToNumber


sumOutputs = 0
with open("input8") as f:
    for line in f:
        patternStr, outputStr = line.strip().split("|")
        patterns = patternStr.split()
        outputs = outputStr.split()
        sumOutputs += getOutputSum(outputs, getMapping(patterns))

print(sumOutputs)


#
# def getMapping(segments, patterns):
#     if count([len(segment) for segment in segments]) == 7:
#         return [list(segment)[0] for segment in segments]
#
# """
# get item with the most constraints (but not 1)
# or fuck it, just pick any of them
# for each char still left:
#     if that's the only char left for some other number, remove the char
#     otherwise, set the signal to that char
#
# """
#
# def getOutputVals(patterns, outputs):
#     segments = [{"a", "b", "c", "d", "e", "f", "g"} for i in range(7)]
#     for pattern in patterns:
#         known = {
#             2 : {"c", "f"},
#             3 : {"a", "c", "f"},
#             4 : {"b", "c", "d", "f"},
#         }
#         if len(pattern) in known:
#             for letter in pattern:
#                 segments[ord(letter)-ord('a')] = known[len(pattern)]
#     mapping = getMapping(segments, patterns)
#     total = 0
#     for output in outputs:
#         outputList = []
#         for char in output:
#             outputList.append(mapping[ord(char)-ord('a')])
#         total += int(signalsToNumber[tuple(sorted(outputList))])

# unique = 0
# with open("input8") as f:
#     for line in f:
#         _, outputs = line.strip().split("|")
#         outputLengths = map(len, outputs.split())
#         unique += sum([1 if length in [7, 2, 3, 4] else 0 for length in outputLengths])
#
# print(unique)
