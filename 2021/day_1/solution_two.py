

def driver():
    input_depths = []
    with open("input.txt", 'r') as f:
        input_depths = [int(l.strip()) for l in f.readlines()]

    count_larger = 0
    last_depth = None
    for i, depth in enumerate(input_depths):
        if last_depth is None:
            last_depth = depth
            continue
        if depth > last_depth:
            count_larger += 1
        last_depth = depth
    print(count_larger)


if __name__ == '__main__':
    driver()
