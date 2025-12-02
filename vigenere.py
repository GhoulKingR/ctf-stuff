key = ""
cyphertext = ""
charset = "abcdefghijklmnopqrstuvwxyz"

ki = 0
plaintext = ""
for c in cyphertext:
    if c not in charset:
        if c == " ":
            plaintext += "_"
        else:
            plaintext += c
    else:
        k = key[ki]

        # stuff to do
        p = charset[(charset.index(c) - charset.index(k)) % 26]
        plaintext += p

        ki += 1
        ki %= len(key)

print (plaintext)
