My solutions to Advent of Code 2021 (https://adventofcode.com/2021), in Python3.


### Day 3, part 2

The challenges in the first two days are pretty straightforward, nothing surprising. Day 3 part 2 is when it starts getting interesting.

The approach I decided to take was to sort each string on each character we're considering, but since there are only two possible values (0 and 1), this is really just a simple bucket sort, which I did in place to avoid unnecessary memory usage. At first I was thought this was overkill, and I was sure there was some one-liner that could take care of it (which always happens on leetcode). Luckily, other people's implementations are equally verbose, if not more so.

I then used recursion on each subsequent smaller list since it was easier than iterating and keeping track of a new slice of the list.

In the previous challenges, I was able to just do one pass through the input without reading it all into memory, but unfortunately I don't think that was possible on this one, since you have to potentially look over every item n times, where n is the length of the binary strings.

The time complexity of this solution is O(nm^2), where n is the number of binary strings and m is the length of each binary string. To see why, consider the worst case scenario, where we have to iterate over and swap every single element in the list m times.

Space complexity is O(nm), from reading the entire input into memory.

### Day 4, part 1

This challenge was pretty straight-forward, but instead of doing the obvious and making a grid for each board, I realized that all we're really interested in is whether the chosen numbers fill up a row or column. So I created a hashmap of numbers to boards, and incremented counters pertaining to the row and column they're in. This means I don't have to search through every board to find instances of the numbers, but instead can access them in constant time.

### Day 5, part 1

I started off with doing a solution that was optimal as possible (e.g. having lists of intervals rather than actually making the whole grid). But that was so much of a pain that I switched to just making a grid, and I'm glad I did since that was enough of a pain itself.

### Day 6, part 1

The key to this one is to realize that each lanternfish's timer is only ever at most 8 days. That means you can group them together by the states of their timers (e.g. 5 that have 4 days left).

### Day 11

Really enjoyed this one. Game of Life is more interesting than I expected. Dumbo octopi are apparently adorable. Glad they weren't dying like in Game of Life instead of flashing, which is also adorable.

### Day 12, part 2

ngl, this one was tough and annoying.

### Day 13, part 2

I may have been embarrassingly excited when my code printed the square that was expected after folding the transparent paper covered with dots.

This one was enjoyable. I've been relieved to discover that after day 5 or so, the difficulty level no longer monotonically increases.
