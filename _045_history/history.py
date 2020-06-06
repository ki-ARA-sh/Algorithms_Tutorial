
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


def insert_command(history, command, index):
    return history[:index - 1] + command + history[index - 1:]


def delete_command(history, index):
    return history[0:index - 1] + history[index:]


def main():
    n = int(input())
    history = Stack()
    ans = ''
    for i in range(n):
        command = input().split()
        if command[0] == 'insert':
            ans = insert_command(ans, command[2], int(command[1]))
            history.push('delete ' + command[1])
        elif command[0] == 'delete':
            history.push('insert ' + command[1] + ' ' + ans[int(command[1]) - 1])
            ans = delete_command(ans, int(command[1]))
        else:
            command = history.pop()
            command = command.split()
            if command[0] == 'insert':
                ans = insert_command(ans, command[2], int(command[1]))
            else:
                ans = delete_command(ans, int(command[1]))
        # print(ans)
    print(ans)


if __name__ == '__main__':
    main()
