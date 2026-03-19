def decode(s):
    result = []
    i = 0

    while i < len(s):
        char = s[i]
        i += 1

        num = 0
        while i < len(s) and s[i].isdigit():
            num = num * 10 + int(s[i]) #why this line works: it converts the string of digits into an integer. For example, if s[i] is '3', num becomes 3. If the next character is '4', num becomes 3 * 10 + 4 = 34. This way, we can handle multi-digit numbers correctly.
            i += 1

        result.append(char * num)

    return ''.join(result)

result = decode("a3b2c4")
print(result)  # Output: "aaabbcccc" (a repeated 3 times, b repeated 2 times, c repeated 4 times)