"""
Optimize Python Data Structures — Simple, One-File Demo

What you'll see:
1) Membership test: list  vs  set
2) Queue operations: list.pop(0)  vs  collections.deque.popleft()
3) Top-K frequency: dict+sort  vs  Counter + heapq.nlargest

Run:  python optimize_ds.py
"""

from collections import deque, Counter
from heapq import nlargest
import random
import string
import timeit


# ---------- Dataset builders (small but realistic) ----------
def make_words(n=50_000, vocab=5_000):
    # Create n random "words" drawn from a vocabulary of size `vocab`
    base = ["w" + str(i) for i in range(vocab)]
    return [random.choice(base) for _ in range(n)]


def make_numbers(n=50_000):
    return list(range(n))


# ---------- 1) Membership test: list vs set ----------
def membership_list(data, queries):
    # O(n) average per "in" on list
    hits = 0
    for q in queries:
        if q in data:
            hits += 1
    return hits


def membership_set(data, queries):
    # O(1) average per "in" on set
    s = set(data)
    hits = 0
    for q in queries:
        if q in s:
            hits += 1
    return hits


# ---------- 2) Queue operations: list.pop(0) vs deque.popleft ----------
def queue_with_list(n=20_000):
    q = list(range(n))
    while q:
        q.pop(0)  # O(n) per pop from front (slow)


def queue_with_deque(n=20_000):
    q = deque(range(n))
    while q:
        q.popleft()  # O(1) per pop from front (fast)


# ---------- 3) Top-K frequency: dict+sort vs Counter+nlargest ----------
def topk_dict_sort(items, k=10):
    counts = {}
    for x in items:
        counts[x] = counts.get(x, 0) + 1
    # Sort all pairs by count (O(n log n))
    return sorted(counts.items(), key=lambda kv: kv[1], reverse=True)[:k]


def topk_counter_heap(items, k=10):
    counts = Counter(items)  # C-optimized counting
    # Pull only the top-k (O(n log k))
    return nlargest(k, counts.items(), key=lambda kv: kv[1])


# ---------- Pretty timing helper ----------
def bench(stmt, setup, number=3):
    t = timeit.timeit(stmt, setup=setup, number=number)
    return t / number  # average seconds


if __name__ == "__main__":
    random.seed(42)

    # Build datasets
    nums = make_numbers(50_000)
    queries_hit = [0, 10_000, 25_000, 49_999] * 500  # many queries that exist
    words = make_words(50_000, vocab=5_000)

    print("\n=== 1) Membership test: list vs set ===")
    t_list = bench(
        "membership_list(nums, queries_hit)",
        setup="from __main__ import membership_list, nums, queries_hit",
    )
    t_set = bench(
        "membership_set(nums, queries_hit)",
        setup="from __main__ import membership_set, nums, queries_hit",
    )
    print(f"list  'in'  avg time: {t_list:.4f}s  (O(n) per check)")
    print(f"set   'in'  avg time: {t_set:.4f}s  (O(1) per check)\n")

    print("=== 2) Queue operations: list.pop(0) vs deque.popleft ===")
    t_q_list = bench(
        "queue_with_list()",
        setup="from __main__ import queue_with_list",
        number=1,  # do once (list.pop(0) is slow)
    )
    t_q_deque = bench(
        "queue_with_deque()",
        setup="from __main__ import queue_with_deque",
        number=3,
    )
    print(f"list.pop(0)       time: {t_q_list:.4f}s  (O(n) each pop)")
    print(f"deque.popleft()   time: {t_q_deque:.4f}s (O(1) each pop)\n")

    print("=== 3) Top-K frequency: dict+sort vs Counter+nlargest ===")
    t_topk_sort = bench(
        "topk_dict_sort(words, 10)",
        setup="from __main__ import topk_dict_sort, words",
    )
    t_topk_heap = bench(
        "topk_counter_heap(words, 10)",
        setup="from __main__ import topk_counter_heap, words",
    )
    print(f"dict + full sort  avg time: {t_topk_sort:.4f}s  (O(n log n))")
    print(f"Counter + nlargest avg time: {t_topk_heap:.4f}s (O(n log k))")

    # Show example results (one run) for clarity
    example_topk = topk_counter_heap(words, 5)
    print("\nTop-5 words (fast method):", example_topk)

    print("\nTakeaways:")
    print("- Use SET/DICT for membership & lookups (usually O(1)).")
    print("- Use DEQUE for fast pops/appends at the ends (queues/stacks).")
    print("- Use Counter + nlargest for top-k instead of sorting everything.")
