# Number Pair Memory Game

A simple Python memory game where the player matches hidden pairs of numbers.

The game creates a shuffled list of number pairs and hides them behind `*` symbols. The player chooses two indices at a time. If the values match, they stay revealed. If they do not match, the player tries again.

## Features

* Randomly shuffled number pairs
* Input validation for invalid, repeated, or already matched indices
* Simple terminal-based gameplay
* Win message when all pairs are matched



## Example

```text
['*', '*', '*', '*', '*', '*']
Enter an index: 0
Enter an index: 3
No match. Try again.
```
