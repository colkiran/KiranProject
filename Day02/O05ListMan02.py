
letters = ['a', 'b', 'c', 'd', 'e']
print(f"letters :{letters}")

print("-" * 60)
# iterating through the list letters
for letter in letters:
    print(letter, end=" ")
print()

print("-" * 60)
for letter in enumerate(letters):
    print(letter, end=" ")
print()                      # line break

print("-" * 60)
for letter in enumerate(letters):
    print(letter[0], letter[1])

print("-" * 60)
for index, letter in enumerate(letters):
    print(index, letter)

print("-" * 60)
my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(my_list)

print("-" * 60)
for ind, lst in enumerate(letters):
    print(f"{ind} \t {lst}")

print("-" * 60)
for ind, lst in enumerate(letters):
    print(f"List({ind})")
    for idx, num in enumerate(lst):
        print(f"\t{idx}\t{num}")

print("-" * 60)
for lst in my_list:
    for num in lst:
        print(num, end=" ")
    print()

print("-" * 60)
print(dir(letters))
