def get_list():
    with open("inputs/day_2.txt", "r") as f:
        list =  [item.strip().split(' ') for item in f.readlines()]
        return [{'direction': item[0], 'distance': item[1]} for item in list]

# def get_direction_dict(directions):
#     for set in directions:

def calculate_position(direction_list):
    positions = {
    'horizontal': 0,
    'vertical': 0,
    'aim': 0
    }

    for item in direction_list:
        if item['direction'] == 'forward':
            positions['horizontal'] += int(item['distance'])
            positions['vertical'] += (int(item['distance']) * positions['aim'])
        elif item['direction'] == 'up':
            positions['aim'] -= int(item['distance'])
        else:
            positions['aim'] += int(item['distance'])

    print(positions)
    print('Product of positions: ' + str(positions['horizontal'] * positions['vertical']))


def main():
    directions = get_list()
    calculate_position(directions)

if __name__ == "__main__":
    main()