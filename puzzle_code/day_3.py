def get_list():
    with open("inputs/day_3.txt", "r") as f:
        strings = [list(item.strip()) for item in f.readlines()]
        return [list(map(int, item)) for item in strings]

def sum_all_lists(master_list):
    return [sum(column) for column in zip(*master_list)]

def reduce_elements(num):
    if num < .5:
        return 0
    elif num > .5:
        return 1
    else:
        return 'u bum'

def get_binary_elements(master_list):
    denominator = len(master_list)
    summary_list = sum_all_lists(master_list)
    gamma_list =  [reduce_elements(number / denominator) for number in summary_list]
    epsilon_list =  [abs(num - 1) for num in gamma_list]
    print(gamma_list)
    print(epsilon_list)
    return {'gamma_bin_list': gamma_list,'epsilon_bin_list': epsilon_list}

def process_lists_to_numbers(dict_):
    gamma_bin = int(''.join(map(str, dict_['gamma_bin_list'])))
    gamma_dec = int(''.join(map(str, dict_['gamma_bin_list'])), 2)
    epsilon_bin = int(''.join(map(str, dict_['epsilon_bin_list'])))
    epsilon_dec = int(''.join(map(str, dict_['epsilon_bin_list'])), 2)
    return {
        'gamma_bin' : gamma_bin,
        'epsilon_bin' : gamma_bin,
        'gamma_dec' : gamma_dec,
        'epsilon_dec' : epsilon_dec,
        'product': (gamma_dec * epsilon_dec)
    }


def main():
    processed_input = get_list()
    output = process_lists_to_numbers(get_binary_elements(processed_input))
    print(output)
    

if __name__ == "__main__":
    main()
