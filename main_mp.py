import multiprocessing as mp
import funcs as F
import time

PROCS = mp.cpu_count() - 1
N = 1000000


results = []

def find_connections(i):
    ret = []
    for n in range (N*i, N*(i+1)):
        if F.is_prime(n):
            ret.append((n, F.find_parent(n)))
            # print(f"Thread {i} pusts {n}")
    print(f"Thread {i} FINISHED")
    return (i, ret)

def collect_result(result):
    global results
    results.append(result)


pool = mp.Pool(PROCS)
start_time = time.time()
results = pool.map(find_connections, [n for n in range(PROCS)])

pool.close()
pool.join()

end_time = time.time()

print("ELAPSED TIME:", end_time - start_time)

results.sort(key=lambda x: x[0])
[print("Process:", i, "Found:", len(r)) for i, r in results]
primes = [len(r) for i,r in results]

import matplotlib.pyplot as plt
import numpy as np

t = [i for i in range(PROCS)]
res = [sum(primes[:i]) for i in range(PROCS)]
plt.plot(t, res, 'b')
plt.show()