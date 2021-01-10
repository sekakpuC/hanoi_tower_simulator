def hanoi_tower_simulator(num_discs: int, source_bar, target_bar):
    if num_discs == 1:
        print(f"moving disc from {source_bar} to {target_bar}")
    else:
        hanoi_tower_simulator(num_discs - 1, source_bar, get_extra_bar(source_bar, target_bar))
        hanoi_tower_simulator(1, source_bar, target_bar)
        hanoi_tower_simulator(num_discs - 1, get_extra_bar(source_bar, target_bar), target_bar)


def get_extra_bar(source_bar, target_bar):
    if source_bar == 0:
        if target_bar == 1:
            return 2
        return 1

    elif source_bar == 1:
        if target_bar == 0:
            return 2
        return 0

    elif source_bar == 2:
        if target_bar == 0:
            return 1
        return 0


if __name__ == "__main__":
    hanoi_tower_simulator(4, 0, 2)
