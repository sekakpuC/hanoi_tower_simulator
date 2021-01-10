def hanoi_tower_simulator(num_discs: int, bars, source_bar, extra_bar, target_bar):
    if num_discs == 1:
        disk = bars[source_bar].pop(-1)
        bars[target_bar].append(disk)
        print(bars)
    else:
        hanoi_tower_simulator(num_discs - 1, bars, source_bar, target_bar, extra_bar)
        hanoi_tower_simulator(1, bars, source_bar, extra_bar, target_bar)
        hanoi_tower_simulator(num_discs - 1, bars, extra_bar, source_bar, target_bar)


if __name__ == "__main__":
    g_num_discs = 4
    g_bars = [list(range(g_num_discs, 0, -1)), [], []]

    hanoi_tower_simulator(g_num_discs, g_bars, 0, 1, 2)
