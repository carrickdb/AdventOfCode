
def countQuestions(questions, groupSize):
    return [n==groupSize for n in questions].count(1)

total = 0
with open("input6") as f:
    groupSize = 0
    questions = [0 for i in range(26)]
    for line in f:
        if line == "\n":
            # print(countQuestions(questions, groupSize))
            total += countQuestions(questions, groupSize)
            questions = [0 for i in range(26)]
            groupSize = 0
            continue
        groupSize += 1
        answers = set()
        for char in line.strip():
            answers.add(char)
        for a in answers:
            questions[ord(a)-ord('a')] += 1

# print(countQuestions(questions, groupSize))
total += countQuestions(questions, groupSize)

print(total)


# count = 0
# with open("input6") as f:
#     questions = set()
#     for line in f:
#         if line == "\n":
#             count += len(questions)
#             questions = set()
#             continue
#         for char in line.strip():
#             questions.add(char)
#
# count += len(questions)
#
# print(count)
