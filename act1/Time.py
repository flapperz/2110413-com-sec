import hashlib
import time
filename = '10k-most-common.txt'

start = time.time()

rainbow = []
i = 0
with open(filename) as file:
    for line in file:
        i += 1
        hashlib.sha1(line.encode('UTF-8')).hexdigest()

end = time.time()
print((end-start)/i)
