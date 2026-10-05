"""Print a table of square roots for the numbers 1 through 10."""

import math


def main() -> None:
    print(f"{'Number':>6} | {'Square Root':>11}")
    print("-" * 6 + "-+-" + "-" * 11)
    for n in range(1, 11):
        print(f"{n:>6} | {math.sqrt(n):>11.4f}")


if __name__ == "__main__":
    main()
