class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        # 

        done = 0
        init_i = 0
        while done < n:        
            curr_i = init_i
            forward = nums[curr_i]
            while True:
                next_i = (curr_i + k) % n
                nums[next_i], forward = forward, nums[next_i]
                done += 1
                curr_i = next_i
                if next_i == init_i:
                    break
            init_i = (init_i + 1) % n
        print(nums)
