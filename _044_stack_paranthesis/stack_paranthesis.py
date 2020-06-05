
class Stack:
    def __init__(self):
        self.size = 0
        self._stack = []

    def pop(self):
        if self.size > 0:
            self.size -= 1
            ans = self._stack[self.size]
            self._stack = self._stack[:-1]
            return ans
        return None

    def top(self):
        if self.size > 0:
            return self._stack[self.size - 1]
        return None

    def push(self, x):
        self.size += 1
        self._stack.append(x)


def f(phrase):
    pass


def main():
    phrase = input()
    bracket_stack = Stack()
    ans = []
    for i, a_bracket in enumerate(phrase):
        if a_bracket == '(':
            bracket_stack.push(i + 1)
        elif bracket_stack.size > 0:
            ans.append(str(bracket_stack.pop()) + ' ' + str(i + 1))
        else:
            print(-1)
            return
    if bracket_stack.size > 0:
        print(-1)
        return
    for line in ans:
        print(line)


if __name__ == '__main__':
    main()
