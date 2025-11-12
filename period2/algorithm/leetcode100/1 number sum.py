import collections
from collections import defaultdict
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}  # 用于存储数值及其索引
        for i, num in enumerate(nums):
            diff = target - num
            if diff in hash_map:
                return [hash_map[diff], i]
            hash_map[num] = i






class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a=[]
        for i in range(len(strs)):
            for j in range(len(strs)):
                if sorted(strs[i]) == sorted(strs[j]):
                    a.append([strs[i], strs[j]])



        return sorted(strs)==sorted


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = collections.defaultdict(list)
        for i in strs:
            key= "".join(sorted(i))
            mp[key].append(i)
        return list(mp.values())
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for num in num_set:
            if num - 1 not in num_set:
                length = 1
                while num + length in num_set:
                    length += 1
                longest = max(longest, length)

        return longest

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
def lengthOfLongestSubstring(s: str) -> int:
    window = {}
    max_len = 0
    left = 0

    for right in range(len(s)):
        if s[right] in window and window[s[right]] >= left:
            left = window[s[right]] + 1  # 重复了，移动左指针
        window[s[right]] = right
        max_len = max(max_len, right - left + 1)

    return max_len

class Solution:
    def findAnagrams(self, s: str, p: str):
        res = []
        if len(s) < len(p):
            return res

        need = collections.Counter(p)
        window = collections.Counter()

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sums={}
        for i  in range(len(nums)):
            sums[i]=sum(nums[i:])
        return(max(sums.values()))
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        low=intervals[0][0]
        high=intervals[0][1]
        r=[]
        for i in intervals:
            low=min(i[0],low)
            if i[0]>high:
                r.append([low,high])
                low=i[0]

            high=max(i[1],high)
        return r

class Solution:
    def merges(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]

        for current in intervals[1:]:
            last = merged[-1]
            if current[0] <= last[1]:
                last[1] = max(last[1], current[1])
            else:
                merged.append(current)

        return merged

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res=[]
        for i in nums:
            if i==target:
                res.append(nums.index(i))
        for i in nums[::-1]:
            if i==target:
                res.append(nums.index(i))
        return [res[0],res[-1]] if res else [-1,-1]


class Solution:
    def jump(self, nums: List[int]) -> int:
        step = 0
        maxp = 0
        l = 0
        while l < len(nums):
            maxp = nums.index(max(nums[maxp:maxp + nums[maxp] + 1]))
            step += 1
            l = maxp

        return step


class Solution:
    def rob(self, nums: List[int]) -> int:
        rob = []
        single = 0
        double = 0
        total = 0
        for i in range(0, len(nums), 2):
            total += nums[i]
            double = total
        rob.append(double)
        total = 0
        for i in range(1, len(nums), 2):
            total += nums[i]
            single = total
        rob.append(single)
        return max(rob)


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = defaultdict(int)
        for i in nums:
            a[i] += 1
        for i,j in enumerate(a):
            if j == 1:
                c=a[j]
                return a[j]
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow=nums[0]
        fast=nums[0]
        while True:
            slow=nums[slow]
            fast=nums[nums[fast]]
            if slow == fast:
                break
        slow=nums[0]
        while slow!=fast:
            slow=nums[slow]
            fast=nums[fast]
        return slow
class Solution:
    def findRepeatDocument(self, documents: List[int]) -> int:
        a=defaultdict(int)
        for i in documents:
            a[i]+=1
            if i in a and a[i]==2:
                return i


class Solution:
    def pathEncryption(self, path: str) -> str:
        for i in range(path):
            if path[i]==".":
                path[i]=" "
        return path

class Solution:
    def permutation(self, goods: str) -> list[str]:
        res = []
        chars = list(goods)

        def backtrack(start):
            if start == len(chars):
                res.append(''.join(chars))
                return
            seen = set()
            for i in range(start, len(chars)):
                if chars[i] in seen:
                    continue
                seen.add(chars[i])
                chars[start], chars[i] = chars[i], chars[start]
                backtrack(start + 1)
                chars[start], chars[i] = chars[i], chars[start]

        backtrack(0)
        return res


class Solution:
    def iceBreakingGame(self, num: int, target: int) -> int:
        for i in  range(target%num):
            a=i
        return a


if __name__ == '__main__':

    num = 7
    Solution().iceBreakingGame(7,3)















# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 if nums[i]+nums[j] == target:
#                     return [i,j]
