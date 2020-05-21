
def hanoi(A, B, C, n):
    if n == 0:
        return []
    result = hanoi(A, C, B, n - 1)
    result.append(A + " " + C)
    result = result + hanoi(B, A, C, n - 1)
    return result


def main():
    moves = hanoi("A", "C", "B", int(input()))
    for i in range(len(moves)):
        print(str(i + 1) + " " + moves[i])


if __name__ == '__main__':
    main()
