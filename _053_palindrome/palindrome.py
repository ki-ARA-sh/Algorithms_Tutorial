# import sys
# sys.setrecursionlimit(200000)


def is_palindrome(string):
    if string[0] != string[2]:
        return False
    return True
    # for i in range(len(string) // 2):
    #     if string[i] != string[len(string) - 1 - i]:
    #         return False
    # return True


def palindrome(base):
    if '?' not in base:
        if len(base) < 3:
            return 1
        for i in range(len(base) - 2):
            if base[i] == base[i + 2]:
                return 0
            # if is_palindrome(base[i:(i + 3)]):
            #     return 0
            # for j in range(i + 2, len(base), 2):
            #     if not is_palindrome(base[i:(j + 1)]):
            #         result += 1
        return 1 # result % 1000000007
    return (palindrome(base.replace('?', 'a', 1)) + palindrome(base.replace('?', 'b', 1))) % 1000000007


def palindrome_creative(base):
    if len(base) < 3:
        return 2 ** (base.count('?'))
    odds = base[1::2]
    evens = base[::2]
    odd_nums = 2
    if ('a' in odds) or ('b' in odds):
        if ('aa' in odds) or ('bb' in odds):
            return 0
        odd_nums = 1
        last_none_q_index = -1
        if '?' in odds:
            for i in range(len(odds)):
                if odds[i] != '?':
                    if last_none_q_index > -1:
                        if odds[last_none_q_index] == 'a':
                            if odds[i] == 'a' and ((i - last_none_q_index) % 2 == 1):
                                return 0
                            elif odds[i] == 'b' and ((i - last_none_q_index) % 2 == 0):
                                return 0
                        else:
                            if odds[i] == 'b' and ((i - last_none_q_index) % 2 == 1):
                                return 0
                            elif odds[i] == 'a' and ((i - last_none_q_index) % 2 == 0):
                                return 0
                    last_none_q_index = i
    even_nums = 2
    if ('a' in evens) or ('b' in evens):
        if ('aa' in evens) or ('bb' in evens):
            return 0
        even_nums = 1
        last_none_q_index = -1
        if '?' in evens:
            for i in range(len(evens)):
                if evens[i] != '?':
                    if last_none_q_index > -1:
                        if evens[last_none_q_index] == 'a':
                            if evens[i] == 'a' and ((i - last_none_q_index) % 2 == 1):
                                return 0
                            elif evens[i] == 'b' and ((i - last_none_q_index) % 2 == 0):
                                return 0
                        else:
                            if evens[i] == 'b' and ((i - last_none_q_index) % 2 == 1):
                                return 0
                            elif evens[i] == 'a' and ((i - last_none_q_index) % 2 == 0):
                                return 0
                    last_none_q_index = i
    return (even_nums * odd_nums) % 1000000007


def main():
    print(palindrome_creative(input()))
    # print(palindrome(input()))


if __name__ == '__main__':
    main()