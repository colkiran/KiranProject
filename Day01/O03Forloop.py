
for i in range(1, 11):
    print(i, end=" ")
print("")

print("hello world")
print("-" * 60)

for i in range(10, 0, -1):
    print(i, end=" ")
print()

print("-" * 60)
# continue, break, else

for i in range(1, 31):
    # if i > 22:
    #     break
    if i % 2 == 1:
        continue        # skip the current iteration
    print(i, end=" ")
else:
    print("\nCompleted generating numbers......")

print("-" * 60)

for i in range(1, 6):
    pass
