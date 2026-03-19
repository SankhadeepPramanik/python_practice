def encode(s):
    if not s:
        return ""

    result = []
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result.append(s[i - 1] + str(count))
            count = 1

    # last group
    result.append(s[-1] + str(count))

    return ''.join(result)

result = encode("aaabbcccc")
print(result)  # Output: "a3b2c4" (a repeated 3 times, b repeated 2 times, c repeated 4 times)