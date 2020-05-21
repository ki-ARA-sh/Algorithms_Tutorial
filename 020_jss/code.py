
def get_displacements(places, info):
    where_to = places
    result = 0
    for an_info in info:
        tmp = where_to & (places - an_info)
        if len(tmp) > 0:
            where_to = tmp
        else:
            result = result + 1
            where_to = places - an_info
    return result


def main():
    n = int(input())
    places = set()
    for i in range(n):
        places.add(input())
    q = int(input())
    info = list()
    for i in range(q):
        tmp = set()
        tmp.add(input())
        info.append(tmp)
    print(get_displacements(places, info))


if __name__ == '__main__':
    main()
