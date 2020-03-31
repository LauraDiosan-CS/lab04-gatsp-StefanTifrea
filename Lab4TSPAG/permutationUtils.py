from random import randint, uniform
from random import shuffle


def generate_new_value(lim1, lim2):
    return uniform(lim1, lim2)

def generate_random_permutation(n):
    '''
    perm = [i for i in range(n)]
    pos1 = randint(0, n - 1)
    pos2 = randint(0, n - 1)
    perm[pos1], perm[pos2] = perm[pos2], perm[pos1]
    return perm
    '''

    perm = [i for i in range(n)]
    shuffle(perm)
    return perm
