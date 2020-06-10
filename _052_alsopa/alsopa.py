def check_recursive(x, n, curr_num=1, curr_sum=0):
    # Initialize number of ways to express
    # x as n-th powers of different natural
    # numbers
    results = 0

    # Calling power of 'i' raised to 'n'
    p = curr_num ** n
    while p + curr_sum < x:
        # Recursively check all greater values of i
        results += check_recursive(x, n, curr_num + 1, p + curr_sum)
        curr_num = curr_num + 1
        p = curr_num ** n

        # If sum of powers is equal to x
    # then increase the value of result.
    if p + curr_sum == x:
        results = results + 1

    # Return the final result
    return results


def main():
    x = int(input())
    n = int(input())
    print(check_recursive(x, n))


if __name__ == '__main__':
    main()