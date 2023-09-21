# Input the string
input_string = input()

# Create a dictionary to store character frequencies
char_count = {}

# Count the occurrences of each character
for char in input_string:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

# Sort the characters by frequency (in descending order) and then alphabetically
sorted_chars = sorted(char_count.items(), key=lambda x: (-x[1], x[0]))

# Print the top 3 sorted characters along with their frequencies
for char, count in sorted_chars[:3]:
    print(f"{char} {count}")
