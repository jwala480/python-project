# Open file in read mode
with open("data.txt", "r") as f:
    lines = f.readlines()

# Initialize counters
line_count = len(lines)
word_count = 0
char_count = 0

# Process each line
for line in lines:
    # Count words
    words = line.strip().split()
    word_count += len(words)

    # Count characters (excluding newline)
    char_count += len(line.strip())

# Print results
print("Lines:", line_count)
print("Words:", word_count)
print("Characters:", char_count)