# (a) Input text
text = input("Enter text: ").lower()

# (b) Count character frequencies
freq = {}

for ch in text:
    if ch.isalpha():
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

# (c) Display frequencies in alphabetical order
print("\nCharacter frequencies:")
for ch in sorted(freq):
    print(ch, ":", freq[ch])