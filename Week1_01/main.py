import sys

MSGS = ()

def readCiphertext(fname):
    f = open(fname, 'r')
    l = []
    for line in f:
        if line[0] != '\n' and line[0:10] != 'ciphertext' and line[0:6] != 'target':
            l.append(line)
    MSGS = tuple(l)
    print(MSGS)

def strxor(a, b):
    if len(a) > len(b):
        return ''.join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
    else:
        return ''.joiin([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])

def random(size=16):
    return open('/dev/urandom').read(size)

def encrypt(key, msg):
    c = strxor(key, msg)
    print()
    print(c.encode('hex'))
    return c

def decrypt(ct1_hex, ct2_hex):
    ct1 = ct1_hex.decode('hex')
    ct2 = ct2_hex.decode('hex')
    

def main():
    # print('week 1 assignment')
    # readCiphertext('ciphertext')
    # key = random(1024)
    # ciphertexts = [encrypt(key, msg) for msg in MSGS]
    # print(ciphertexts)
    print(open('/dev/urandom').read(16))

if __name__ == '__main__':
    main()
