# League Membership Analyzer

Two conferences' rosters, as sets of player names. Given, don't modify:

```python
east_team_names = {"Ava", "Ben", "Cy", "Dee"}
west_team_names = {"Cy", "Dee", "Emi", "Finn"}
```

Implement:

- `both_conferences(east: set, west: set) -> set` -- `east & west` (**intersection**: players rostered on both sides -- a trade mid-season, or a data error worth flagging).
- `all_players(east: set, west: set) -> set` -- `east | west` (**union**: every player across both rosters).
- `east_only(east: set, west: set) -> set` -- `east - west` (**difference**: on the East roster and nowhere else).
- `west_only(east: set, west: set) -> set` -- `west - east` (the same **difference** operator, the other direction -- note it is not symmetric: `east - west != west - east` in general).
- `symmetric_difference_manual(east: set, west: set) -> set` -- build it by hand from the three operators above: `(east - west) | (west - east)` (players on exactly one roster, not both). This should come out identical to Python's built-in `east ^ west` -- the exercise is proving that to yourself by composing union+difference, not reaching for `^` directly.

See the Study Reference presentation, Topic 4 (Mid tier), for the theory.
