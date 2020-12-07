list_of_nums = list(map(int, input("Please divide numbers by space: ").split()))
shift_num = int(input("Input number for shift: "))


def shift_numbers(shifted_nums, func_for_shift):
    shifted_nums = shifted_nums[-func_for_shift:] + shifted_nums[:-func_for_shift]
    return shifted_nums


print(shift_numbers(list_of_nums, shift_num))
