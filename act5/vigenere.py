import string
key = input.strip().lower()
plain = input.strip().lower()

cipher = ''
for (i,a) in enumerate(plain):
    if a in string.ascii_lowercase:
        currentkey = key[i%len(key)]
        offset = currentkey - 97
        cipher += chr(((ord(a) + offset)- 97)%26 + 97)
    else:
        cipher += a

print(cipher)
    