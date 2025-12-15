import hashlib

id = 'abbhdwsy'
# id = 'abc'

i = 0
password = ["_" for i in range(8)]
found = 0
while found < 8:
    i += 1
    if i == 5357525:
        print(5357525)
    if i % 1000000==0:
        print(i)
    hash = hashlib.md5((id+str(i)).encode()).hexdigest()
    if hash[:5] == "00000":
        pos = int(hash[5], 16)
        if pos > 7:
            continue
        if password[pos] != "_":
            continue
        password[pos] = hash[6]
        print(password)
        found += 1
print(''.join(password))


# i = 0
# password = []
# while len(password) < 8:
#     hash = hashlib.md5((id+str(i)).encode()).hexdigest()
#     if hash[:5] == "00000":
#         password.append(hash[5])
#         print(hash[5])
#     i += 1
# print(''.join(password))