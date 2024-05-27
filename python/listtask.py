numbers = [1, 1, 2, 3, 4, 4, 5, 6, 6]
duplicates = []
seen = []

for number in numbers:
    if number in seen:
        if number not in duplicates:
            duplicates.append(number)
    else:
        seen.append(number)

print(duplicates)
