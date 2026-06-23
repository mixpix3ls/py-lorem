import loremipsum

with open("result.txt", "w") as f:
    f.write(loremipsum.sentence(max_char=20))
