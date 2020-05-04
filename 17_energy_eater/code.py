
def eat_fruit(fruit):
    if fruit[1] - fruit[0] > 0:
        return True
    else:
        return False


def gained_energy(energy, fruit):
    if energy >= fruit[0]:
        return fruit[1] - fruit[0]
    else:
        return 0


def get_energy(init, fruits):
    energy = init
    for i in range(len(fruits)):
        energy = energy + gained_energy(energy, fruits[i])
    return energy


def insert_fruit_to_list(fruits, a, b):
    inserted = False
    for i in range(len(fruits)):
        if a < fruits[i][0]:
            fruits.insert(i, [a, b])
            inserted = True
            break
    if not inserted:
        fruits.append([a, b])
    return fruits


def main():
    n, init = map(int, input().split())
    fruits = []
    for i in range(n):
        a, b = map(int, input().split())
        if (b - a) > 0:
            fruits = insert_fruit_to_list(fruits, a, b)
    print(get_energy(init, fruits))


if __name__ == '__main__':
    main()
