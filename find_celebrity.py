# You have a room with n people. A celebrity walks in.Everyone knows the celebrity,
# the celebrity knows no one. Non- celebrities may/may not know anyone in the room.
# Give an algorithm to find the celebrity.

from random import randrange
# Number of persons
N = 100
# the graph of connections built using random values.
G = [ [randrange(2) for i in range(N)] for i in range(N) ]

def create_celebrity():
    C = randrange(N)
    # ensure that we have celebrity at C
    for i in range(N):
        G[i][C] = 1
        G[C][i] = 0
    print("rand celeb : %d" % C)


def bruteforce():
    """Brute force solution to the celebrity problem"""
    n = len(G)
    steps = 0
    for i in range(N):
        is_celeb = 1
        for j in range(N):
            steps += 1
            if i == j: continue
            # i knows j and is not a celebrity
            # j does not know i, break
            if G[i][j] or not G[j][i]:
                is_celeb = 0;
                break
        if is_celeb:
            print("found celeb at %d in %d steps" % (i, steps) )
            return i

def bruteforce_improved():
    """Improvement to brute force"""
    # At every-step we can eliminate either i or j
    u,v = 0,1
    steps = 0
    while u < N and v < N:
        steps += 1
        if u == v: v = u+1
        # if u knows v, then u is not a celeb,
        # if u does not know v, then v is not a celeb
        if G[u][v]: u = u+1
        else : v = v+1
    print("found celeb at %d in %d steps" % (u, steps) )

def linear_time():
    """ finds in linear time : see : 
        Python Algorithms: Mastering Basic Algorithms in the Python Language p.86
        By Magnus Lie Hetland
    """
    u,v = 0,1 # the first two persons
    steps = 0
    # c corresponds to the third to the last person...
    for c in range(2, N):
        steps += 1
        if G[u][v]: u=c # u knows v, replace u
        else:       v=c # otherwise, u is a candidate

    if v==c : c=u #if v has reached end of list, use u.
    else:     c=v

    for i in range(N):
        if c==i: continue
        if G[c][i]:break
        if not G[i][c]: break
    else:
        print("found celeb at %d in %d steps" % (c, steps) )



if __name__ == '__main__':
    create_celebrity()
    bruteforce()
    bruteforce_improved()
    linear_time()
