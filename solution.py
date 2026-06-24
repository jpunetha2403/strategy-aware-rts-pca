def solution(s: str, k: int) -> str:
    # Store frequency of each digit (0-9)
    freq = [0] * 10

    # Count occurrences of every digit
    for ch in s:
        freq[int(ch)] += 1

    # Result builder
    result = []

    # Start from the largest digit
    digit = 9

    # Continue while some digit is still available
    while digit >= 0:

        # If current digit does not exist, move to next smaller digit
        if freq[digit] == 0:
            digit -= 1
            continue

        # Add current digit at most k times consecutively
        use = min(freq[digit], k)

        # Append the digit 'use' times
        result.extend(str(digit) for _ in range(use))

        # Reduce its remaining count
        freq[digit] -= use

        # If no copies remain, move to next smaller digit
        if freq[digit] == 0:
            continue

        # Find next smaller available digit to break the sequence
        smaller = digit - 1

        # Search for a smaller digit having non-zero frequency
        while smaller >= 0 and freq[smaller] == 0:
            smaller -= 1

        # If no smaller digit exists, construction is finished
        if smaller < 0:
            break

        # Insert one occurrence of the smaller digit
        result.append(str(smaller))

        # Reduce its count
        freq[smaller] -= 1

    # Convert list to string and return
    return "".join(result)
