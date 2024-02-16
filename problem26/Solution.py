def decodeString(s):
    stack = []
    for ch in s:
        if ch != ']':
            stack.append(ch)
            continue
        substr = ""
        while True:
            item = stack.pop()
            if item == '[': continue
            if item.isalpha():
                substr = item + substr
                continue
            num = item
            while stack and stack[-1].isdigit():
                num = stack.pop() + num
            stack.append(int(num) * substr)
            break
    return "".join(stack)

def main():
    sList = ["3[a]2[bc]", "3[a2[c]]", "2[abc]3[cd]ef"]
    for s in sList:
        print("Decoded = ", decodeString(s))

if __name__ == "__main__":
    main()


