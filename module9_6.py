def all_variants(text):
    for y in range(len(text)):
        for x in range(y,len(text)):
            yield text[y: x+1]

a = all_variants("abc")
for i in a:
    print(i)
