
def get_subsets(a_set):
    result = list()
    add_empty_set = True
    for an_item in a_set:
        add_empty_set = False
        a = set()
        a.add(an_item)
        subsets = get_subsets(a_set - a)
        for a_subset in subsets:
            result.append(a_subset)
            result.append(a_subset | a)
            print(result[len(result) - 1])
        break
    if add_empty_set:
        print(set())
        result.append(set())
    return result


def main():
    n = int(input())
    the_set = set(map(int, input().split()))
    subsets = get_subsets(the_set)


if __name__ == "__main__":
    main()