
def hanoi(A, B, C, n):
    if n == 0:
        return []
    result = hanoi(A, C, B, n - 1)
    result.append(A + " " + C)
    result = result + hanoi(B, A, C, n - 1)
    return result


def main():
    moves = hanoi("A", "B", "C", int(input()))
    print("\n".join(moves))


if __name__ == '__main__':
    main()
