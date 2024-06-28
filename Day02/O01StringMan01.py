
st = "hello world"
print(f"st :{st}")
# strings are stored like lists or arrays
print(f"st[0] :{st[0]}")
# st[0] = "H"
print(f"st[6]  :{st[6]}")
print(f"st[10] :{st[10]}")
# print(f"st[12] :{st[12]}")

print("-" * 60)
# slicing the string using their indexes
print(f"st[0:5] :{st[0:5]}")
print(f"st[6:11] :{st[6:11]}")
print(f"st[0:11] :{st[0:11]}")
print(f"st[0:]   :{st[0:]}")
print(f"st[:11]  :{st[:11]}")
print(f"st[:]    :{st[:]}")
print(f"st[:20]    :{st[:20]}")
print(f"st[20:]    :{st[20:]}")
print("-" * 60)

# Reverse Indexing
print(f"st[-1] :{st[-1]}")
print(f"st[-5] :{st[-5]}")
print(f"st[-11] :{st[-11]}")

print("-" * 60)
# slicing reverse order
print(f"st[-1: -6: -1] :{st[-1:-6:-1]}")
print(f"st[-7:-12:-1]  :{st[-7:-12:-1]}")
print(f"st[-1:-12:-1]  :{st[-1:-12:-1]}")
print(f"st[-1::-1]     :{st[-1::-1]}")
print(f"st[:-12:-1]    :{st[:-12:-1]}")
print(f"st[::-1]       :{st[::-1]}")

print("-" * 60)
# check if the given string is a palindrome - ABBA, malayalam
st = "malayalam"
print("palindrome" if st[:] == st[::-1] else "Not a Palindrome")

print(f"st[:] :{st[:]}")
print(f"st[::-1] :{st[::-1]}")

print("-" * 60)
st = "hello world"
# st is an object of class string
print(type(st))
print(st.count("a"))
l = st.count("l")
print(l)