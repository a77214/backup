import random


def findKthLargest(nums, k):
    def quickselect(left, right, k_smallest):
        # 基本情况：当左右指针相遇时，返回该元素
        if left == right:
            return nums[left]

        # 随机选择基准值索引（避免最坏情况）
        pivot_index = random.randint(left, right)

        # 执行分区操作，返回基准值的最终位置
        pivot_index = partition(left, right, pivot_index)

        # 如果基准值位置正好是k_smallest，直接返回
        if k_smallest == pivot_index:
            return nums[k_smallest]
        # 如果k_smallest在基准值左侧，处理左半部分
        elif k_smallest < pivot_index:
            return quickselect(left, pivot_index - 1, k_smallest)
        # 否则处理右半部分
        else:
            return quickselect(pivot_index + 1, right, k_smallest)

    def partition(left, right, pivot_index):
        pivot = nums[pivot_index]
        # 将基准值交换到最右端
        nums[pivot_index], nums[right] = nums[right], nums[pivot_index]

        store_index = left
        # 遍历数组（不包括最右端的基准值）
        for i in range(left, right):
            if nums[i] < pivot:
                # 将小于基准值的元素交换到store_index位置
                nums[store_index], nums[i] = nums[i], nums[store_index]
                store_index += 1

        # 将基准值交换到最终正确位置
        nums[right], nums[store_index] = nums[store_index], nums[right]
        return store_index

    # 调用quickselect，注意将第k大转换为第k_smallest小
    return quickselect(0, len(nums) - 1, len(nums) - k)

if __name__ == '__main__':
    nums = [1, 3,2,1,9,4,5,2]
    findKthLargest(nums,3)