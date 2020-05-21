
def main():
    n = int(input())
    result = dict()
    for i in range(n):
        name, mark = input().split()
        result[name] = int(mark)
    return result




if __name__ == "__main__":
    dictionary = main()
    print(dictionary)