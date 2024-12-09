import random
import statistics
import time
import matplotlib.pyplot as plt
from Algo_and_Struts_05_a_sequential_search import sequential_search


def binary_search(a_list, item):
    """Performs a binary search on a sorted list."""
    first = 0
    last = len(a_list) - 1
    while first <= last:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            return True
        elif item < a_list[midpoint]:
            last = midpoint - 1
        else:
            first = midpoint + 1
    return False

# Experiment setup
sizes = [1000, 10000, 100000, 1000000]
search_methods = {
    "Sequential Search": sequential_search,
   "Binary Search": binary_search
}

""""""

# Collect results
results = {method: {"average": [], "median": []} for method in search_methods}
results["Dictionary Search"] = {"average": [], "median": []}

#Experiment loop
for size in sizes:
    # Create sorted list and dictionary with `size` items
    sorted_list = list(range(size))
    data_dict = {key: True for key in sorted_list}

    # Select 100 random items to search for
    search_items = random.sample(sorted_list, 100)

    # Run experiment for each search method
    for method_name, search_method in search_methods.items():
        times = []
        for item in search_items:
            start_time = time.time()
            search_method(sorted_list, item)
            end_time = time.time()
            times.append(end_time - start_time)
        
        results[method_name]["average"].append(statistics.mean(times))
        results[method_name]["median"].append(statistics.median(times))
    # Dictionary Search (Python's built-in dictionary lookup)
    dict_times = []
    for item in search_items:
        start_time = time.time()
        _ = data_dict.get(item)
        end_time = time.time()
        dict_times.append(end_time - start_time)
    
    results["Dictionary Search"]["average"].append(statistics.mean(dict_times))
    results["Dictionary Search"]["median"].append(statistics.median(dict_times))

print(results)

# Plotting results
plt.figure(figsize=(14, 8))

# Plot average search times
plt.subplot(1, 2, 1)
for method_name, data in results.items():
    plt.plot(sizes, data["average"], label=method_name)
plt.xlabel("Dataset Size")
plt.ylabel("Average Search Time (s)")
plt.title("Average Search Time Comparison")
plt.legend()

# Plot median search times
plt.subplot(1, 2, 2)
for method_name, data in results.items():
    plt.plot(sizes, data["median"], label=method_name)
plt.xlabel("Dataset Size")
plt.ylabel("Median Search Time (s)")
plt.title("Median Search Time Comparison")
plt.legend()

plt.tight_layout()
plt.savefig("search_times_comparison.png")
plt.show()