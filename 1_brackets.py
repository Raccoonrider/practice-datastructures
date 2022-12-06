line = input()

brackets = { ")":"(", "]":"[", "}":"{"}

def get_brackets(line):
    stack = []
    for pos, char in enumerate(line, start=1):
        if char in "([{":
            stack.append((pos,char))
        elif char in ")]}":
            if not stack:
                return pos
            bracket = stack.pop()
            if bracket[1] != brackets[char]:
                return pos
    if len(stack):
        return stack[-1][0]
    return 'Success'

print(get_brackets(line))