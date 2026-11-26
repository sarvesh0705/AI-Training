a = [1, 2, 3, 2, 4, 1, 5]

# Frequency
for i in range(len(a)):
    c = 0
    for j in range(len(a)):
        if a[i] == a[j]:
            c = c + 1
    print(a[i], "frequency =", c)

# Repeating elements
print("Repeating:")
for i in range(len(a)):
    c = 0
    for j in range(len(a)):
        if a[i] == a[j]:
            c = c + 1
    if c > 1:
        print(a[i], end=" ")

# Non-repeating elements
print("\nNon-repeating:")
for i in range(len(a)):
    c = 0
    for j in range(len(a)):
        if a[i] == a[j]:
            c = c + 1
    if c == 1:
        print(a[i], end=" ")

# Distinct elements
print("\nDistinct:")
for i in range(len(a)):
    if a[i] not in a[:i]:
        print(a[i], end=" ")

arr = [1, 2, 3, 1, 3, 4, 5]
freq = {}

for i in arr:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

for i in freq:
    if freq[i] > 1:
        print(i)        