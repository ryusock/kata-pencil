# Pencil Durability Kata
This code kata simulates a graphite pencil.

## Dependencies
Python 2.7 or 3.4+. Assuming running on OS X.

This project uses the Python package `pytest` for testing. Ensure that the Python package installer `pip` is installed beforehand.

## Tests
Test are split between the three major functions of the application: write, erase, edit. I implemented each function after writing each test file to practice more Test Driven Development.

Run `make init` to install `pytest`. Then run `make test` to run all tests.

## Running
Open the Python interpreter and enter
```
from stationary import Pencil, Paper
```
Initialize a new `Pencil` and `Paper` and you're all set. Details below.

### Pencil
**Pencil(point_dur, length, eraser_dur)**

`point_dur`, `length`, and `eraser_dur` are ints representing the point durability, length, and eraser durability of the Pencil instance. Defaults are set to 10, 5, and 24 respectively.

Enter `pencil.write(text, paper)` to write some `text` on a `paper` instance. Writing decreases point durability, and once durability and length are used up, the pencil no longer writes. Sharpening is done automatically when durability is insufficient and length is greater than zero. Capital letters cost 2 durabilities, white space costs 0, and all other characters cost 1.

Enter `pencil.erase(text, paper)` to erase the last matching pattern of `text` from a `paper` instance. Erasing decreases eraser durability, and once that is spent, the pencil no longer erases.

Enter `pencil.edit(text, paper, start)` to write over a `paper` instance's text with some other `text` at starting index `start`. There were some likely intentional ambiguities in the specs, so I made some key assumptions with my implementation:
- If an edit goes over the length of the paper (e.g. see `test_edit_collision_out_of_bounds` in `test_edit.py`), the pencil attempts to edit whatever space is available on the paper before giving up. Doing so does *not* raise an exception.
- Edits are still technically writes, so the same rules on point durability and length for writing apply here. If a pencil's total durability is used up, it can no longer edit (write new characters or @'s).
- While editing *over* a whitespace with a non-whitespace character means the latter is written, editing a whitespace over a non-whitespace doesn't make sense. That is considered a collision and results in a @ character.
- Writing a collision (@) *still degrades the pencil*. Following convention above, the degradation cost is still one. This created some interesting test cases where a pencil couldn't write in a capital, but a @ was fine. (See `test_edit_collision_and_point_degradation` in `test_edit.py`).

### Paper
**Paper(text)**

Paper is simply an abstraction for the string to write/erase/edit. The default string is the empty string.
