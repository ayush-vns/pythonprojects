def lastchar(s):
    s = s.lower()
    count = 0
    for ch in s:
        if ch in "aeiou":
            count += 1
    return count


r = ["apple", "rsdf", "lion"]
print(r)
r.sort(key=lastchar)
print(r)
