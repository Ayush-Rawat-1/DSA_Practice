class Solution:
    def countRatioSubarrays(self, nums: list[int], a: int, b: int) -> int:
        """
        Calculates the number of valid subarrays where even_count / odd_count <= a / b (with odd_count > 0).
        
        Mathematical Transformation:
        Let x = count of even numbers, y = count of odd numbers.
        Condition: x / y <= a / b  ==>  x * b <= y * a  ==>  y * a - x * b >= 0
        
        By transforming:
        - Odd numbers to  +a
        - Even numbers to -b
        A subarray sum is equal to (y * a - x * b).
        Therefore, a subarray nums[i..j] is valid if Prefix[j+1] - Prefix[i] >= 0,
        which simplifies to Prefix[i] <= Prefix[j+1] (for i < j+1).
        
        This reduces the problem to counting pairs (i, j) with i < j where Prefix[i] <= Prefix[j],
        which can be solved efficiently using Divide & Conquer (Modified Merge Sort).
        """
        n = len(nums)
        
        # Step 1: Build the transformed prefix sums array
        # Prefix array has size (n + 1) to handle subarrays starting at index 0
        prefix = [0] * (n + 1)
        for i in range(n):
            weight = a if nums[i] % 2 != 0 else -b
            prefix[i + 1] = prefix[i] + weight

        def conquer(start: int, mid: int, end: int) -> int:
            """
            Counts cross-half valid pairs (i in left, j in right) such that
            Prefix[i] <= Prefix[j] and merges the two sorted halves.
            """
            left_half = prefix[start : mid + 1]
            right_half = prefix[mid + 1 : end + 1]
            
            len_left, len_right = len(left_half), len(right_half)
            valid_pairs_count = 0

            # Step 2a: Count valid pairs across halves using Two Pointers
            # Since both left_half and right_half are already sorted,
            # for each element in right_half, we find how many elements in left_half are <= right_val.
            left_ptr = 0
            for right_val in right_half:
                while left_ptr < len_left and left_half[left_ptr] <= right_val:
                    left_ptr += 1
                valid_pairs_count += left_ptr

            # Step 2b: Standard Merge Sort step (In-place merge back into prefix array)
            i = j = 0
            k = start
            
            while i < len_left and j < len_right:
                if left_half[i] <= right_half[j]:
                    prefix[k] = left_half[i]
                    i += 1
                else:
                    prefix[k] = right_half[j]
                    j += 1
                k += 1

            while i < len_left:
                prefix[k] = left_half[i]
                i += 1
                k += 1

            while j < len_right:
                prefix[k] = right_half[j]
                j += 1
                k += 1

            return valid_pairs_count

        def divide(start: int, end: int) -> int:
            """
            Recursively divides the prefix array range [start, end] into smaller segments,
            counting valid pairs within each segment and across segments.
            """
            if start >= end:
                return 0

            mid = (start + end) // 2
            
            # Count valid pairs in the left sub-array
            total_valid_pairs = divide(start, mid)
            # Count valid pairs in the right sub-array
            total_valid_pairs += divide(mid + 1, end)
            # Count cross-half valid pairs and merge
            total_valid_pairs += conquer(start, mid, end)

            return total_valid_pairs

        # Step 3: Run divide and conquer over the full prefix range [0, n]
        return divide(0, n)
