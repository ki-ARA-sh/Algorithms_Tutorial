
def gray_code(length):
    if length == 1:
        return ["0", "1"]
    a = gray_code(length - 1)
    result = list()
    alternate = False
    for i in range(len(a)):
        result.append(str(int(alternate)) + a[i])
        result.append(str(int(not alternate)) + a[i])
        alternate = not alternate
    return result


def main():
    print('\n'.join(gray_code(int(input()))))


if __name__ == "__main__":
    main()
