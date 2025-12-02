text = ""
charset = "abcdefghijklmnopqrstuvwxyz"

for i in range(1, 26):
    result = ""
    for c in text:
        if c in charset:
            result += charset[(charset.index(c) + i) % 26]
        else:
            result += c
    print(result)
