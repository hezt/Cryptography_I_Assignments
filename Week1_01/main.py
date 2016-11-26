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
        return ''.join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])


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
    recovered = [["" for i in range(len(MSGS))] for i in range(len(MSGS))]
    m_len = len(MSGS) - 1
    for i in range(len(MSGS) - 1):
        for j in range(m_len):
            r = recoverXor(MSGS[i], MSGS[i + j + 1])
            recovered[i][j] = r
            recovered[j][i] = r    
        m_len -= 1
    for i in range(len(recovered)):
        byte_loc = 0
        while 1:
            alphabet_times= 0
            null_times = 0
            for j in range(len(recovered[i])):
                if len(recovered[i][j]) > byte_loc:
                    char_ascii = ord(recovered[i][j][byte_loc])
                   if (char_ascii >= 0x41 and char_ascii <= 0x5A) or (char_ascii >= 0x61 and char_ascii <= 0x7A):
                        alphabet_times += 1
                else:
                    null_times += 1
            if null_times == len(recovered[i]):
                break
            if alphabet_times >= 7:
                


def main():
    readCiphertext('ciphertext')
    print(ciphertexts)

if __name__ == '__main__':
    main()
