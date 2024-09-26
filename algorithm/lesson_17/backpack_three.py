# https://www.youtube.com/watch?v=MKvt-k0YE4M&list=PLoWGNURguz9Xk248HDiJICojc-0rlayUW&index=65
# https://www.youtube.com/watch?v=Xup7ZpMxcVU&list=PLoWGNURguz9Xk248HDiJICojc-0rlayUW&index=67


import sys
import heapq


def fractional_knapsack(capacity, values_and_weights):
    order = [(-v / w, w) for v, w in values_and_weights]
    heapq.heapify(order)
    print(f"order: {order}")

    acc = 0
    while order:
        v_per_w, w = heapq.heappop(order)
        if w < capacity:
            acc += -v_per_w * w
            capacity -= w
        else:
            acc += -v_per_w * capacity
            break

    return acc


def main():
    reader = (tuple(map(int, line.split())) for line in sys.stdin)
    n, capacity = next(reader)
    values_and_weights = list(reader)

    print(f"values_and_weights: {values_and_weights}")
    print(f"n: {n}, capacity: {capacity}")

    assert len(values_and_weights) == n
    opt_value = fractional_knapsack(capacity, values_and_weights)

    print("{:.3f}".format(opt_value))


"""
python backpack_three.py < knapsack_input.txt
"""


if __name__ == "__main__":
    main()
