# Use Zip
few_words = ['longtext', 'short', 'a']
size = [len(n) for n in few_words]

word = None
le = 0
for wrd, length in zip(few_words, size):
    if length > le:
        word = wrd
        le = length
print(word)
