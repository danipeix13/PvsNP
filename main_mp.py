import multiprocessing as mp
import funcs as F
import time

PROCS = mp.cpu_count() - 1
N = 50000


results = []

def find_connections(i):
    ret = []
    for n in range (N*i, N*(i+1)):
        if F.is_prime(n):
            ret.append((n, F.find_parent(n)))
            print(f"Thread {i} pusts {n}")
    print(f"Thread {i} FINISHED")
    return (i, ret)

def collect_result(result):
    global results
    results.append(result)


pool = mp.Pool(PROCS)

results = pool.map(find_connections, [n for n in range(PROCS)])
    # time.sleep(5)

pool.close()
pool.join()

results.sort(key=lambda x: x[0])
# results_final = [r for i, r in results]

for core in results:
    print(len(core[1]))