def three_odd_numbers(nums):
    """Is the sum of any 3 sequential numbers odd?"

        >>> three_odd_numbers([1, 2, 3, 4, 5])
        True

        >>> three_odd_numbers([0, -2, 4, 1, 9, 12, 4, 1, 0])
        True

        >>> three_odd_numbers([5, 2, 1])
        False

        >>> three_odd_numbers([1, 2, 3, 3, 2])
        False
    """
    nums2 = nums[1:]
    nums3 = nums2[1:]

    for x in nums:
        for y in nums2:
            for z in nums3:
                if x < y < z and (x+y+z)%2!=0:
                    return True
    return False
