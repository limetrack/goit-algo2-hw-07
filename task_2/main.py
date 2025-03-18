import timeit
import matplotlib.pyplot as plt
from functools import lru_cache

from splay_tree import SplayTree


# Реалізація LRU-кешу
@lru_cache(maxsize=None)
def fibonacci_lru(n):
    if n < 2:
        return n
    return fibonacci_lru(n - 1) + fibonacci_lru(n - 2)


# Реалізація Splay Tree
def fibonacci_splay(n, tree):
    if n < 2:
        return n
    cached = tree.search(n)
    if cached is not None:
        return cached
    result = fibonacci_splay(n - 1, tree) + fibonacci_splay(n - 2, tree)
    tree.insert(n, result)
    return result


def build_plot(n_values, lru_times, splay_times):
    plt.figure(figsize=(10, 6))
    plt.plot(n_values, lru_times, marker="o", linestyle="-", label="LRU Cache")
    plt.plot(n_values, splay_times, marker="x", linestyle="-", label="Splay Tree")
    plt.xlabel("Число Фібоначчі (n)")
    plt.ylabel("Середній час виконання (секунди)")
    plt.title("Порівняння часу виконання для LRU Cache та Splay Tree")
    plt.legend()
    plt.show()


def print_results(n_values, lru_times, splay_times):
    print("n         LRU Cache Time (s)  Splay Tree Time (s)")
    print("--------------------------------------------------")
    for i in range(len(n_values)):
        print(f"{n_values[i]:<10} {lru_times[i]:<20.8f} {splay_times[i]:<20.8f}")


if __name__ == "__main__":
    n_values = list(range(0, 951, 50))
    lru_times = []
    splay_times = []

    tree = SplayTree()

    for n in n_values:
        lru_time = timeit.timeit(lambda: fibonacci_lru(n), number=10) / 10
        splay_time = timeit.timeit(lambda: fibonacci_splay(n, tree), number=10) / 10

        lru_times.append(lru_time)
        splay_times.append(splay_time)

    build_plot(n_values, lru_times, splay_times)
    print_results(n_values, lru_times, splay_times)
