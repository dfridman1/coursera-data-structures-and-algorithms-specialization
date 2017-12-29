# python2


import random


def rabin_karp(text, pattern):
    pattern_hash, hashes = precompute_hashes(pattern, text)
    shifts = []
    for i in xrange(len(text)-len(pattern)+1):
        if hashes[i] == pattern_hash and pattern_matched(pattern, text, i):
            shifts.append(i)
    return shifts


def precompute_hashes(pattern, text):
    p = 1000000007
    x = random.randint(1, p)
    pattern_hash = 0
    for c in reversed(pattern):
        pattern_hash = (ord(c) + x*pattern_hash) % p
    hashes = [0] * len(text)
    y = (x**len(pattern)) % p
    text_hash = 0
    for i in xrange(len(text)-1, len(text)-len(pattern)-1, -1):
        text_hash = (ord(text[i]) + text_hash*x) % p
        hashes[i] = text_hash
    for i in xrange(len(text)-len(pattern)-1, -1, -1):
        hashes[i] = (ord(text[i]) + x*hashes[i+1] - ord(text[i+len(pattern)])*y) % p
    return pattern_hash, hashes


def pattern_matched(pattern, text, i):
    for j, c in enumerate(pattern):
        if c != text[i+j]:
            return False
    return True


def read_data():
    pattern = raw_input()
    text = raw_input()
    return pattern, text


def main():
    pattern, text = read_data()
    shifts = rabin_karp(text, pattern)
    print(' '.join(map(str, shifts)))


if __name__ == '__main__':
    main()
