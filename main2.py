import threading as T
import queue as Q
import funcs as F
from collections import defaultdict


N_MAX = 1000000
N_THREADS = 10

tree = defaultdict(list)

connexions = [
    (2, 1),
    (3, 5)
]

def x_to_index(x):
    return (x - 5) // 2

def index_to_x(index):
    return 2*index + 5

def find_connections(x):
    index = x_to_index(x)
    for n in range(x, N_MAX, 2*N_THREADS):
        if F.is_prime(n):
            queues[index].put((n, F.find_parent(n)))
            # print(f"Thread {index} puts {n}, queue size: {queues[index].qsize()}")
    print(f"Thread {index} FINISHED, queue size: {queues[index].qsize()}")
    return

def collect():
    for i in range(N_MAX):
        print("COLLECTOR :)")

if __name__ == "__main__":
    pool, queues = {}, {}
   
    collector = T.Thread(name="Collector", target=collect)
    # collector.start()

    for index in range(N_THREADS):
        pool[index] = T.Thread(name=index, target=find_connections, args=[index_to_x(index)])
        queues[index] = Q.Queue()
        if index == 0 or index%5 != 0:
            pool[index].start()
