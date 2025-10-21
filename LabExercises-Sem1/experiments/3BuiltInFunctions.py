def find_mean(data):
    n = len(data)
    total = sum(data)
    mean = total / n
    return mean


def find_median(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2
    
    if n % 2 == 0:
        median = (sorted_data[mid - 1] + sorted_data[mid]) / 2
    else:
        median = sorted_data[mid]
    return median


def find_mode(data):
    frequency = {}
    for value in data:
        frequency[value] = frequency.get(value, 0) + 1

    max_freq = max(frequency.values())
    modes = [key for key, val in frequency.items() if val == max_freq]
    
    if len(modes) == len(frequency):
        return "No mode"
    elif len(modes) == 1:
        return modes[0]
    else:
        return modes 


def find_std_deviation(data):
    mean = find_mean(data)
    squared_diff = [(x - mean) ** 2 for x in data]
    variance = sum(squared_diff) / len(data)
    std_dev = variance ** 0.5
    return std_dev

data = [69, 74, 68, 70, 72, 67, 66, 70, 76, 68, 72, 79, 74, 67, 66, 71, 74]

print("Data:", data)
print("Mean:", find_mean(data))
print("Median:", find_median(data))
print("Mode:", find_mode(data))
print("Standard Deviation:", round(find_std_deviation(data), 2))
