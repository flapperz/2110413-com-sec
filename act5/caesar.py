import enchant
import string
d = enchant.Dict("en_US")

cipher = input().tolower()

maxvalid = 0
ans = ''
for i in range(26):

    plain = ''
    for a in cipher:
        if a in string.ascii_lowercase: 
            plain += chr((ord(a)+i-97)%26 + 97)
        else:
            plain += a
    valid = sum([d.check(word) for word in plain.split().strip('.')])
    if valid > maxvalid:
        ans = plain
        maxvalid = valid
print(ans)