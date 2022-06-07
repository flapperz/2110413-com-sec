import hashlib

def CheckHash(plain, md5):
    if hashlib.sha1(plain.encode('UTF-8')).hexdigest() == md5:
        print(plain)
        return True
    if hashlib.md5(plain.encode('UTF-8')).hexdigest() == md5:
        print(plain)
        return True
    return False

def Rec(plain, md5, i):
    if i == len(plain):
        return CheckHash(plain, md5)

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

    for newChar in subList:
        subPlain = plain[0:i] + newChar + plain[i+1:]
        if Rec(subPlain, md5, i+1):
            return True
    return False

filename = '10k-most-common.txt'
md5 = 'd54cc1fe76f5186380a0939d2fc1723c44e8a5f7'

with open(filename) as file:
    for line in file:
        plain = line.strip()
        if Rec(plain, md5, 0):
            break
    else:
        print("not match")
    pass