import hashlib

# id = 'abc'

i = 0
password = []
while len(password) < 8:
    hash = hashlib.md5((id+str(i)).encode()).hexdigest()
    if hash[:5] == "00000":
        password.append(hash[5])
        print(hash[5])
    i += 1
print(''.join(password))