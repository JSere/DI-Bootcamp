import random

list_of_numbers = [random.randint(0, 10000) for _ in range(20000)]

target_number = 3728

def find_pairs(numbers, target):
    pairs = []
    length = len(numbers)
    
    
    for i in range(length):
       
        for j in range(i + 1, length):
            if numbers[i] + numbers[j] == target:
                pairs.append((numbers[i], numbers[j]))
                
    return pairs


found_pairs = find_pairs(list_of_numbers, target_number)

print(f"Total pairs found: {len(found_pairs)}")

print("First 5 pairs:", found_pairs[:5])