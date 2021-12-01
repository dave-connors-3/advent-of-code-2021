def get_list():
    with open("inputs/day_1.txt", "r") as f:
        return [int(item.strip()) for item in f.readlines()]

def get_increases(list_object):
    ticker = 0
    for i, v in enumerate(list_object):
        if i == 0:
            pass
        else:
            if v > list_object[i - 1]:
                ticker += 1
    return ticker

def collapse_list_to_sums(list_object, window_size):
    output = []
    for i, v in enumerate(list_object):
        if i < window_size - 1:
            pass
        else:
            output.append(sum(list_object[i-(window_size-1):i+1]))
    return output

def main():
    numbers = get_list()
    print('Total Increases: ' + str(get_increases(numbers)))
    windowed_numbers = collapse_list_to_sums(numbers, 3)
    print('Total Window Increases: ' + str(get_increases(windowed_numbers)))


if __name__ == "__main__":
    main()