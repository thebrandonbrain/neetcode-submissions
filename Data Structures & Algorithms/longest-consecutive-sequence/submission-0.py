class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        highest_counter = 0

        for num in set_nums:
            # Only start counting if num is the beginning
            # of a consecutive sequence
            if num - 1 not in set_nums:
                counter = 0
                x = num

                while x in set_nums:
                    counter += 1
                    x += 1

                highest_counter = max(highest_counter, counter)

        return highest_counter


        