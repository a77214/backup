import random
from collections import defaultdict


def topKFrequent(nums, k):
    # 统计频率 O(n)
    freq = defaultdict(int)
    for num in nums:
        freq[num] += 1
    unique = list(freq.keys())

    def partition(left, right, pivot_idx):
        # 将基准元素交换到末尾
        pivot_freq = freq[unique[pivot_idx]]
        unique[pivot_idx], unique[right] = unique[right], unique[pivot_idx]

        # 分区操作：大于基准的放左边
        store_idx = left
        for i in range(left, right):
            if freq[unique[i]] > pivot_freq:  # 注意这里是降序排列
                unique[store_idx], unique[i] = unique[i], unique[store_idx]
                store_idx += 1

        # 将基准元素放回正确位置
        unique[right], unique[store_idx] = unique[store_idx], unique[right]
        return store_idx

    def quickselect(left, right, k_smallest):
        if left == right:
            return

        # 随机选择基准元素
        pivot_idx = random.randint(left, right)
        true_idx = partition(left, right, pivot_idx)

        if k_smallest == true_idx:
            return
        elif k_smallest < true_idx:
            quickselect(left, true_idx - 1, k_smallest)
        else:
            quickselect(true_idx + 1, right, k_smallest)

    n = len(unique)
    quickselect(0, n - 1, k - 1)  # 找第k-1索引（因为从0开始）
    return unique[:k]


if __name__ == '__main__':
    nums = [1, 3,2,1,9,4,5,2]
    topKFrequent(nums,3)