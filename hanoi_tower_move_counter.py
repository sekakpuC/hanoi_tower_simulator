def count_hanoi_tower_moves(num_discs: int):
    if num_discs == 1:
        return 1
    else:
        return count_hanoi_tower_moves(num_discs - 1) * 2 + 1


if __name__ == "__main__":
    for i in range(1, 65):
        print(i, count_hanoi_tower_moves(i))
