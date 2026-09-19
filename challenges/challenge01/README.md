# Challenge 01 — Group Anagrams

**Do this after:** Week 04 (Data Structures)
**Not pytest-tested.** Grade it yourself against the constraints below.

## Problem

Given a list of strings, group every string with any of its anagrams
(strings made of exactly the same letters, in any order). Return the groups
as a list of lists; the order of the groups, and the order of words within
a group, does not matter.

```python
group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
# ->  [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]   (any order)
```

This is a real, frequently-asked interview question (it's LeetCode #49) --
interviewers use it to check whether you reach for the right data structure
(a dict keyed by some canonical signature of each word) instead of an O(n^2)
compare-every-pair-of-words approach.

## Required signature

```python
def group_anagrams(words: list[str]) -> list[list[str]]:
    ...
```

## Constraints on HOW you write it

These are graded by reading the code, not by a test suite:

1. **No `collections.Counter` and no `collections.defaultdict`.** Group the
   words using a plain `dict` you manage yourself (`dict.setdefault` or an
   explicit `if key not in groups:` check). The point is to prove you
   understand dict operations directly, not that you know a shortcut exists.
2. **The per-word signature (the dict key) must be computed with a
   comprehension**, not a `for` loop with `.append()`. For example, turning
   a word into its sorted-letters signature is a one-line comprehension
   away from `"".join(...)`.
3. **Full type hints** on the function signature (shown above) -- match it
   exactly so the function is a drop-in replacement for the stub.
4. **A docstring with a comprehensive, explicit list of every edge case
   your implementation handles.** At minimum, address: an empty input list;
   an empty string in the input; a single-character word; words that are
   already identical (duplicates); and whether comparison is case-sensitive
   (state your assumption -- don't leave it silently undefined).

## Complexity target

State the time and space complexity of your solution as a comment directly
above the function (e.g. `# Time: O(n * k log k), Space: O(n * k)` where n
is the number of words and k is the max word length) -- and make sure your
actual implementation matches what you claim.
