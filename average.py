l = input("Give me some numbers: ").split(" ")

l = (int(i) for i in l)

s = 0
length = 0
for xi in l:
    s += xi
    length += 1

print(f"Average is {s/length}.\n")
