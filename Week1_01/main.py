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


def recoverXor(ct1_hex, ct2_hex):
    ct1 = ct1_hex.decode('hex')
    ct2 = ct2_hex.decode('hex')
    if(len(ct1) > len(ct2)):
        return strxor(ct1[:len(ct2)], ct2)
    else:
        return strxor(ct1, ct2[:len(ct1)])


def decrypt():
    random_key = {}
    # recovered = []
    m_len = len(MSGS) - 1
    # for i in range(len(MSGS) - 2):
        # for j in range(m_len):
            # r = recoverXor(MSGS[i], MSGS[i + j + 1])



def main():
    readCiphertext('ciphertext')
    print(ciphertexts)

if __name__ == '__main__':
    main()
