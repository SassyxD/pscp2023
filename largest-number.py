def create_m4x_number(nums):
    def find_m4x_index(nums):
        if len(nums) == 1:
            return 0

        next_m4x_index = find_m4x_index(nums[1:])
        return 0 if nums[0] >= nums[next_m4x_index + 1] else next_m4x_index + 1

    def concat_m4x(a, b):
        return int(str(a) + str(b)) if int(str(a) + str(b)) > int(str(b) + str(a)) else int(str(b) + str(a))

    def recursive_m4x(nums):
        if len(nums) == 1:
            return nums[0]

        m4x_num_idx = find_m4x_index(nums)
        m4x_num = nums[m4x_num_idx]

        nums.pop(m4x_num_idx)
        remaining_m4x = recursive_m4x(nums)

        return concat_m4x(m4x_num, remaining_m4x)

    return recursive_m4x(nums)

num1 = int(input())
num2 = int(input())
num3 = int(input())

numbers = [num1, num2, num3]

m4x_number = create_m4x_number(numbers)

print(m4x_number)
