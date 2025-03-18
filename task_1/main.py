import random
import timeit
from lru_cache import LRUCache


# Функції без кешу
def range_sum_no_cache(array, L, R):
    return sum(array[L : R + 1])


def update_no_cache(array, index, value):
    array[index] = value


# Функції з LRU-кешем
cache_size = 1000
cache = LRUCache(cache_size)


def range_sum_with_cache(array, L, R):
    cached_result = cache.get((L, R))

    if cached_result is not None:
        return cached_result

    result = sum(array[L : R + 1])
    cache.put((L, R), result)

    return result


def update_with_cache(array, index, value):
    array[index] = value
    cache.invalidate(index)


N = 100000
Q = 50000
test_data = [random.randint(1, 1000) for _ in range(N)]
queries = []

for _ in range(Q):
    if random.random() < 0.5:
        L = random.randint(0, N - 1)
        R = random.randint(L, N - 1)
        queries.append(("Range", L, R))
    else:
        index = random.randint(0, N - 1)
        value = random.randint(1, 1000)
        queries.append(("Update", index, value))


def test_no_cache():
    for query in queries:
        if query[0] == "Range":
            range_sum_no_cache(test_data, query[1], query[2])
        else:
            update_no_cache(test_data, query[1], query[2])


def test_with_cache():
    for query in queries:
        if query[0] == "Range":
            range_sum_with_cache(test_data, query[1], query[2])
        else:
            update_with_cache(test_data, query[1], query[2])


if __name__ == "__main__":
    num_tests = 10

    time_no_cache = timeit.timeit(test_no_cache, number=num_tests)
    time_with_cache = timeit.timeit(test_with_cache, number=num_tests)

    print(f"Час виконання без кешування ({num_tests} запусків): {time_no_cache:.2f} секунд")
    print(f"Час виконання з LRU-кешем ({num_tests} запусків): {time_with_cache:.2f} секунд")
