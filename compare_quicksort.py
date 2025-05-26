import random
import time
import matplotlib.pyplot as plt
import numpy as np

# Детермінований QuickSort (опорний елемент — останній)
def deterministic_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    left = [x for x in arr[:-1] if x < pivot]
    right = [x for x in arr[:-1] if x >= pivot]
    return deterministic_quick_sort(left) + [pivot] + deterministic_quick_sort(right)

# Рандомізований QuickSort (опорний елемент — випадковий)
def randomized_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]
    left = [x for i, x in enumerate(arr) if x < pivot and i != pivot_index]
    right = [x for i, x in enumerate(arr) if x >= pivot and i != pivot_index]
    return randomized_quick_sort(left) + [pivot] + randomized_quick_sort(right)

# Функція для вимірювання середнього часу виконання
def measure_time(sort_func, arr, repeats=5):
    total_time = 0
    for _ in range(repeats):
        copied = arr.copy()
        start = time.perf_counter()
        sort_func(copied)
        total_time += time.perf_counter() - start
    return total_time / repeats

def main():
    sizes = [10_000, 50_000, 100_000, 500_000]
    results_randomized = []
    results_deterministic = []

    for size in sizes:
        test_array = [random.randint(0, 1_000_000) for _ in range(size)]
        t_randomized = measure_time(randomized_quick_sort, test_array)
        t_deterministic = measure_time(deterministic_quick_sort, test_array)

        results_randomized.append(t_randomized)
        results_deterministic.append(t_deterministic)

        print(f"Розмір масиву: {size}")
        print(f"   Рандомізований QuickSort: {t_randomized:.4f} секунд")
        print(f"   Детермінований QuickSort: {t_deterministic:.4f} секунд\n")

    # Побудова графіку
    plt.figure(figsize=(8, 6))
    plt.plot(sizes, results_randomized, label="Рандомізований QuickSort")
    plt.plot(sizes, results_deterministic, label="Детермінований QuickSort")
    plt.xlabel("Розмір масиву")
    plt.ylabel("Середній час виконання (секунди)")
    plt.title("Порівняння рандомізованого та детермінованого QuickSort")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
