
def f(c, nums):
    if (c == 0) or (len(nums) == 0) or (nums[0] <= c):
        return 0
    d = min(c, max(0, nums[0] - c))
    del nums[0]
    return d + f(c - d, nums)


def main():
    n, c = map(int, input().split())
    nums = list(map(int, input().split()))
    nums.sort(reverse=True)
    print(c - f(c, nums))


if __name__ == '__main__':
    main()
