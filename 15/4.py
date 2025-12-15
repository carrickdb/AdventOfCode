import hashlib

# secretKey = "ckczppom"
secretKey = "ckczppom"
i = 0
while True:
    curr = hashlib.md5(bytearray(secretKey + str(i), 'utf-8')).hexdigest()
    if curr[:6] == "000000":
        print(i)
        print(curr)
        break
    i += 1
