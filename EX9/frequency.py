def char_frequency(inputstring):
    fdict = {}
    for char in inputstring:
        if char in fdict:
            fdict[char] += 1
        else:
            fdict[char] = 1
    return fdict

sentence =input("Enter string:")
result = char_frequency(sentence)
print(result)
