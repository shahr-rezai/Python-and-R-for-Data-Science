# (a) Create candidates
votes = {"Alice": 0, "Bob": 0, "Charlie": 0}
rejected = 0

# (b) Accept votes
while True:
    vote = input("Enter vote (or DONE): ")

    if vote.upper() == "DONE":
        break

    found = False
    for name in votes:
        if vote.lower() == name.lower():
            votes[name] += 1
            found = True
            break

    if not found:
        rejected += 1

# (c) Display vote counts
print("\nVote results:")
valid = 0
for name in votes:
    print(name, ":", votes[name])
    valid += votes[name]

print("\nTotal valid votes:", valid)
print("Rejected votes:", rejected)

# (d) Display percentages
print("\nVote percentages:")
for name in votes:
    if valid > 0:
        percent = (votes[name] / valid) * 100
    else:
        percent = 0
    print(name, ":", round(percent, 2), "%")

# (e) Determine winner or tie
highest = -1
winner = ""
tie = False

for name in votes:
    if votes[name] > highest:
        highest = votes[name]
        winner = name
        tie = False
    elif votes[name] == highest:
        tie = True

if valid == 0:
    print("\nNo valid votes cast.")
elif tie:
    print("\nResult: Tie")
else:
    print("\nWinner:", winner)