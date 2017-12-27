# python2



class Bracket:
    def __init__(self, char, pos):
        self.char = char
        self.pos = pos

    @staticmethod
    def is_opening(bracket):
        return bracket.char in {'{', '[', '('}

    @staticmethod
    def is_closing(bracket):
        return bracket.char in {'}', ']', ')'}

    @staticmethod
    def match(b1, b2):
        mapping = {
            '[': ']',
            '(': ')',
            '{': '}'
        }
        return mapping[b1.char] == b2.char


def process(s):
    stack = []
    for i, ch in enumerate(s, 1):
        b = Bracket(ch, i)
        if Bracket.is_opening(b):
            stack.append(b)
        elif Bracket.is_closing(b):
            if len(stack) == 0:
                return i
            last_b = stack.pop()
            if not Bracket.match(last_b, b):
                return i
    if len(stack) == 0:
        return 'Success'
    else:
        return stack[0].pos


def generate_data():
    while True:
        try:
            s = raw_input()
            yield s
        except EOFError:
            break


def main():
    for s in generate_data():
        ans = process(s)
        print(ans)

if __name__ == '__main__':
    main()
