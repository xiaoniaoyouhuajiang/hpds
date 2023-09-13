import random
import time

nA = 100
nB = 100
nC = 100

A = {'A-%d' % i: ['B-%d' % random.randint(0, nB - 1)
                  for i in range(random.randint(0, 5))]
     for i in range(nA)}

B = {'B-%d' % i: {'C-%d' % random.randint(0, nC - 1)
                  for i in range(random.randint(1, 3))}
     for i in range(nB)}

C = {'C-%d' % i: i for i in range(nC)}

data = ['A-%d' % i for i in range(nA)]


def f(A, B, C, data):
    for a_key in data:
        b_keys = A[a_key]
        for b_key in b_keys:
            for c_key in B[b_key]:
                C[c_key] += 1
                # print([c_key])


start = time.time()

for i in range(10000):
    f(A, B, C, data)

end = time.time()

print("Duration: %0.3f seconds" % (end - start))