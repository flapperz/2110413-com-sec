import hashlib
import time

def CheckHash(plain, md5):
    if hashlib.sha1(plain.encode('UTF-8')).hexdigest() == md5:
        print(plain)
        return True
    if hashlib.md5(plain.encode('UTF-8')).hexdigest() == md5:
        print(plain)
        return True
    return False

def Rec(plain, i):
    if i == len(plain):
        return [plain]

    char = plain[i].lower()
    subList = []
    if char.isalpha():
        subList += [char.upper(), char]
    else:
        subList += [char]

    if char == 'o':
        subList.append('0')
    elif char == '0':
        subList.append('o')
        subList.append('O')
    elif char == 'i':
        subList.append('1')
    elif char == 'l':
        subList.append('1')
    elif char == '1':
        subList.append('i')
        subList.append('I')
        subList.append('l')
        subList.append('L')

    res = []
    for newChar in subList:
        subPlain = plain[0:i] + newChar + plain[i+1:]
        res += Rec(subPlain, i+1)
            
    return res

filename = '10k-most-common.txt'

start = time.time()

rainbow = []
with open(filename) as file:
    for line in file:
        plain = line.strip()
        rainbow += Rec(plain, 0)

end = time.time()

print('time:', end-start)
print('size:', len(rainbow))