class Solution:
    def combinationSum4(self, nums, target):

        results = []

        def back_track(tmp_result):
            if sum(tmp_result) == target:
                results.append(tmp_result[:])

                return

            if sum(tmp_result) > target:
                return

            for num in nums:
                tmp_result.append(num)
                back_track(tmp_result)
                # tmp_result.pop(-1)

        back_track([])

        return len(results)

"""
Results:
Time Limit Exceeded	
"""