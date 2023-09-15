s = "cabca"
result = 0
letters = list()
for x in s:
    if x not in letters:
        result += 1
        letters.append(x)
print(result)