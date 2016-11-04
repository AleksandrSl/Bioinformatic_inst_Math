import time
from functools import wraps


def timethis(func):
    '''
    Decorator that reports the execution time
    '''
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print('function:{} runned {:f} seconds'.format(func.__name__, end-start))
        return result
    return wrapper


def find_max_product(x):
    cur_max = 0
    for i1 in range(len(x)):
        for i2 in range(i1 + 1, len(x)):
            if x[i1]*x[i2] > cur_max:
                cur_max = x[i1] * x[i2]
    return cur_max


def find_max_product_optim(x):
    max1 = max(x)
    x[x.index(max1)] = None
    max2 = max(x)
    return max1*max2


def find_max_product_optim_v2(x):
    max1 = 0
    ind1 = None
    max2 = 0

    for i1, el in enumerate(x):
        if el > max1:
            max1 = el
            ind1 = i1
    for el in (x[:ind1] + x[ind1 + 1:]):
        if el > max2:
            max2 = el
    return max1*max2


@timethis
def find_motif(s, m):
    pos = set()
    for i in range(len(s) - len(m) + 1):
        for i2 in range(len(m)):
            if s[i + i2] != m[i2]:
                break
        else:
            pos.add(i)
    return pos


class Finder:

    def __init__(self):
        self.a = 5

    def hash_chunk(self, s):
        len_ = len(s)
        return sum([ord(s[i])*self.a_list[i] for i in range(len_)])

    def rolling_hash(self, leaving_char, entering_char, hash_):
        hash_ = (hash_ - ord(leaving_char) * self.a_list[0]) * self.a + ord(entering_char)
        return hash_

    @timethis
    def find_motif_hash(self, s, motif):
        k = len(motif)
        self.a_list = [self.a ** i for i in range(0, k)] # a_list initialized here cause it is different
        # for motifs of different lengths
        self.a_list.reverse()
        ind = []
        hash_ = None
        motif_hash = self.hash_chunk(motif)
        for i in range(len(s) - k + 1):
            if hash_ is None:
                hash_ = self.hash_chunk(s[:k])
            else:
                hash_ = self.rolling_hash(s[i - 1], s[i + k - 1], hash_)
            if motif_hash == hash_:
                ind.append(i)
        return ind


class Finder2:

    def __init__(self, k):
        self.a = 5
        self.a_list = [self.a ** i for i in range(0, k)]
        self.a_list.reverse()
        self.k = k

    def hash_chunk(self, s):
        len_ = len(s)
        return sum([ord(s[i]) * self.a_list[i] for i in range(len_)])

    def rolling_hash(self, leaving_char, entering_char, hash_):
        hash_ = (hash_ - ord(leaving_char) * self.a_list[0]) * self.a + ord(entering_char)
        return hash_

    @timethis
    def find_motif_hash_v1(self, s, motif):
        assert len(motif) == self.k
        ind = []
        hash_ = None
        motif_hash = self.hash_chunk(motif)
        for i in range(len(s) - self.k + 1):
            if hash_ is None:
                hash_ = self.hash_chunk(s[:self.k])
            else:
                hash_ = self.rolling_hash(s[i - 1], s[i + self.k - 1], hash_)
            if motif_hash == hash_:
                ind.append(i)
        return ind

    @timethis
    def find_motif_hash_v2(self, s, motif): # works faster
        k = self.k
        assert len(motif) == k
        ind = []
        hash_ = None
        motif_hash = self.hash_chunk(motif)
        for i in range(len(s) - k + 1):
            if hash_ is None:
                hash_ = self.hash_chunk(s[:k])
            else:
                hash_ = self.rolling_hash(s[i - 1], s[i + k - 1], hash_)
            if motif_hash == hash_:
                ind.append(i)
        return ind

