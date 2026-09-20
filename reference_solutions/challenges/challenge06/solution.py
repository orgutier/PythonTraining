# Time: O(n), Space: O(n)
# Every number is visited a constant number of times: once when added to
# the set, and once more only if it turns out to be the start of a run
# (x - 1 not in the set) -- the inner while loop across all outer
# iterations combined only ever advances through each number once.
def longest_consecutive(nums: list[int]) -> int:
    """
    Return the length of the longest run of consecutive integers present
    anywhere in nums (order in the list doesn't matter).

    Edge cases handled:
      - Empty list -> returns 0.
      - Duplicate values (e.g. [1, 1, 2]) -> the set collapses duplicates,
        so they don't inflate the run length.
      - Single-element list -> returns 1.
      - Negative numbers -> work the same as positive ones; consecutive
        just means each next value is exactly +1.
      - An already-contiguous list -> still detected correctly since only
        the true start of the run (no x-1 present) kicks off counting.
    """
    num_set = set(nums)
    longest = 0

    for x in num_set:
        if x - 1 in num_set:
            continue  # not the start of a run, skip it

        length = 1
        current = x
        while current + 1 in num_set:
            current += 1
            length += 1

        longest = max(longest, length)

    return longest
