# (a) Input sentence
sentence = input("Enter a sentence: ").lower()

# (b) Count word frequencies
words = sentence.split()
freq = {}

for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

# (c) Display frequencies
print("\nWord Frequencies:")
for word, count in freq.items():
    print(word, ":", count)