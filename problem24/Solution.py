def removeStars(s):
    letters = []
    for c in s:
        if c == '*':
            letters.pop()
        else:
            letters.append(c)
    return "".join(letters)

def main():
    s = "leet**cod*e"
    print("ans = ",removeStars(s))

if __name__ == "__main__":
    main()
