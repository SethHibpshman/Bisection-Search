# Bisection Search

> A short Python script that approximates the square root of any positive number using the bisection method, narrowing a search interval until the answer is within a chosen tolerance.

## Table of Contents

- [Overview](#overview)
- [Functionality](#functionality)
  - [How It Works](#how-it-works)
  - [Configuration](#configuration)
  - [Example Output](#example-output)
- [System Design](#system-design)
  - [Software](#software)
- [Author](#author)
- [AI Disclosure](#ai-disclosure)
- [License](#license)

## Overview

Bisection Search finds the square root of a number `x` without calling `math.sqrt()`. It starts with an interval known to contain the answer, then repeatedly cuts that interval in half, keeping the half where the root must lie.

The script was written for **Calculus I** at Eastern Washington University as a hands-on look at the bisection method for root finding.

## Functionality

### How It Works

1. **Pick the starting interval.** The square root of `x` always lies between `x` and `1`, so the bounds depend on whether `x` is above or below 1.

| Input | Low Bound | High Bound |
|---|---|---|
| `x >= 1` | `1.0` | `x` |
| `0 < x < 1` | `x` | `1.0` |

2. **Guess the midpoint.** `guess = (low + high) / 2`
3. **Narrow the interval.** If `guess²` is below `x`, the guess becomes the new low bound. Otherwise it becomes the new high bound.
4. **Repeat** until `|guess² - x| < epsilon`.

Each pass halves the interval, so the error shrinks quickly: finding the square root of 16 to within `0.000001` takes 25 iterations.

### Configuration

Both settings are at the top of the script.

| Variable | Default | Description |
|---|---|---|
| `x` | `16` | The number to take the square root of |
| `epsilon` | `0.000001` | How close `guess²` must be to `x` before stopping |

### Example Output

The script prints the bounds on every iteration, then the final answer:

```
low = 1.0 high = 16
low = 1.0 high = 8.5
low = 1.0 high = 4.75
...
low = 3.9999998211860657 high = 4.000000715255737
4.000000044703484 is close to the square root of 16
```

## System Design

### Software

Written in **Python 3** with no dependencies.

```
bisection_search.py    # Full script: configuration, starting bounds, bisection loop, output
```

**Run it:**

```
python bisection_search.py
```

## Author

**Seth Hibpshman**  
Student of Electrical Engineering, Eastern Washington University

## AI Disclosure
_AI (LLM) tools assisted in drafting and editing this README. The script itself was written by the author._

## License

[GNU General Public License v3.0](LICENSE)
