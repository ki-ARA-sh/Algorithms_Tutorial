
class Editor:
    def __init__(self):
        self.string = ''
        self.pointer = 0

    def move_forward(self):
        if self.pointer < len(self.string):
            self.pointer += 1
        pass

    def move_back(self):
        if self.pointer > 0:
            self.pointer -= 1
        pass

    def insert(self, c):
        self.string = self.string[:self.pointer] + c + self.string[self.pointer:]
        self.pointer += 1
        pass

    def interpret_command(self, a_command):
        if a_command == '+':
            self.move_forward()
        elif a_command == '-':
            self.move_back()
        else:
            self.insert(a_command.split()[1])


def edit_text(commands):
    editor = Editor()
    for a_command in commands:
        editor.interpret_command(a_command)
    return editor.string


def main():
    n = int(input())
    commands = []
    for i in range(n):
        commands.append(input())
    print(edit_text(commands))


if __name__ == '__main__':
    main()
