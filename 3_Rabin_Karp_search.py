pattern = input()
text = input()

p = 1_000_000_007
x = 1

def h(s):
    result = 0
    xi = 1
    for _, c in enumerate(s):
        result += ord(c) * xi % p
        xi *= x
    return result % p

def shift(s, hash_, char):
    hash_ -= ord(s[-1]) * x ** (len(s) - 1) % p
    hash_ = (hash_ + p) % p
    hash_ *= x
    hash_ += ord(char)
    return hash_ % p

size = len(pattern)
pattern_h = h(pattern)
text_h = None

result = []
for i in range(len(text) - size, -1, -1):
    if text_h is None:
        window = text[-size:]
        text_h = h(window)
    else:
        text_h = shift(window, text_h, text[i])
        window = text[i] + window[:-1]
        
    if text_h == pattern_h:
        if text[i:i+size] == pattern:
            result.append(str(i))
            
print(" ".join(result[::-1]))