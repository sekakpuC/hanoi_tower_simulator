import pygame as pygame

from hanoi_tower_move_counter import count_hanoi_tower_moves


def display_num_moves(gd):

    msg_txt = f"{gd['num_moves']}/{gd['expected_moves']}"
    msg = gd["game_font"].render(msg_txt, True, (255, 255, 255))
    gd["screen"].blit(msg, (10,10))


def draw_objects(gd):
    dt = gd["clock"].tick(gd["fps"])

    for e in pygame.event.get():
        if e:
            if e.type == pygame.QUIT:
                exit(0)
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_UP:
                    gd["fps"] *= 2
                elif e.key == pygame.K_DOWN:
                    gd["fps"] /= 2

    scr_width, scr_height = gd["screen"].get_rect().size
    stage_width, stage_height = gd["i_stage"].get_rect().size
    bar_width, bar_height = gd["i_bar"].get_rect().size

    draw_screen(gd)
    draw_stage(gd)

    bar_y = scr_height - bar_height
    bar_x = (scr_width / 6) - (bar_width / 2)
    gd["screen"].blit(gd["i_bar"], (bar_x, bar_y))
    bar_x = (scr_width / 2) - (bar_width / 2)
    gd["screen"].blit(gd["i_bar"], (bar_x, bar_y))

    bar_x = (5 * scr_width / 6) - (bar_width / 2)
    gd["screen"].blit(gd["i_bar"], (bar_x, bar_y))

    bar_center = scr_width / 6
    for i in range(len(gd["bars"][0])):
        disc_size = gd["bars"][0][i]
        disc_width, disc_height = gd["i_discs"][disc_size - 1].get_rect().size
        disc_x = bar_center - (disc_width / 2)
        disc_y = screen_height - stage_height - (disc_height * (i + 1))
        gd["screen"].blit(gd["i_discs"][disc_size - 1], (disc_x, disc_y))

    bar_center = scr_width / 2
    for i in range(len(gd["bars"][1])):
        disc_size = gd["bars"][1][i]
        disc_width, disc_height = gd["i_discs"][disc_size - 1].get_rect().size
        disc_x = bar_center - (disc_width / 2)
        disc_y = screen_height - stage_height - (disc_height * (i + 1))
        gd["screen"].blit(gd["i_discs"][disc_size - 1], (disc_x, disc_y))

    bar_center = 5 * scr_width / 6
    for i in range(len(gd["bars"][2])):
        disc_size = gd["bars"][2][i]
        disc_width, disc_height = gd["i_discs"][disc_size - 1].get_rect().size
        disc_x = bar_center - (disc_width / 2)
        disc_y = screen_height - stage_height - (disc_height * (i + 1))
        gd["screen"].blit(gd["i_discs"][disc_size - 1], (disc_x, disc_y))

    display_num_moves(gd)

    pygame.display.update()


def draw_stage(gd):
    scr_width, scr_height = gd["screen"].get_rect().size
    stage_width, stage_height = gd["i_stage"].get_rect().size
    gd["screen"].blit(gd["i_stage"], (0, scr_height - stage_height))


def draw_screen(gd):
    gd["screen"].blit(gd["i_background"], (0, 0))


def hanoi_tower_simulator(gd, num_discs: int, bars, source_bar, extra_bar, target_bar):
    if num_discs == 1:
        disk = bars[source_bar].pop(-1)
        bars[target_bar].append(disk)
        gd["num_moves"] += 1
        draw_objects(gd)
    else:
        hanoi_tower_simulator(gd, num_discs - 1, bars, source_bar, target_bar, extra_bar)
        hanoi_tower_simulator(gd, 1, bars, source_bar, extra_bar, target_bar)
        hanoi_tower_simulator(gd, num_discs - 1, bars, extra_bar, source_bar, target_bar)


def draw_num_disc_msg(gd):
    msg_txt = f"Select Number of Discs: {gd['num_discs']}"
    msg = gd["game_font"].render(msg_txt, True, (255, 255, 255))
    msg_rect = msg.get_rect()
    msg_width, msg_height = msg_rect.size
    gd["screen"].blit(msg, (gd["screen_width"] / 2 - msg_width / 2, gd["screen_height"] / 2 - msg_height / 2))


def get_num_discs(gd):
    running = True

    while running:
        dt = gd["clock"].tick(60)
        for e in pygame.event.get():
            if e:
                if e.type == pygame.QUIT:
                    exit(0)
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_UP:
                        if gd["num_discs"] < 12:
                            gd["num_discs"] += 1
                    elif e.key == pygame.K_DOWN:
                        if gd["num_discs"] > 1:
                            gd["num_discs"] -= 1
                    else:
                        running = False
        draw_screen(gd)
        draw_num_disc_msg(gd)
        pygame.display.update()


def draw_press_any_key_msg(gd):
    msg_txt = "Press Any Key To Close"
    msg = gd["game_font"].render(msg_txt, True, (255, 255, 255))
    msg_rect = msg.get_rect()
    msg_width, msg_height = msg_rect.size
    gd["screen"].blit(msg, (gd["screen_width"] / 2 - msg_width / 2, gd["screen_height"] / 2 - msg_height / 2))


def get_any_key(gd):
    running = True

    while running:
        dt = gd["clock"].tick(60)
        for e in pygame.event.get():
            if e:
                if e.type == pygame.QUIT:
                    exit(0)
                if e.type == pygame.KEYDOWN:
                    running = False
        draw_screen(gd)
        draw_press_any_key_msg(gd)
        pygame.display.update()

if __name__ == "__main__":

    gd = {}

    gd["num_discs"] = 7

    pygame.init()
    gd["clock"] = pygame.time.Clock()
    gd["fps"] = 2

    gd["screen_width"] = screen_width = 900
    gd["screen_height"] = screen_height = 600
    gd["screen"] = screen = pygame.display.set_mode((screen_width, screen_height))

    gd["i_background"] = pygame.image.load("background.png")
    gd["i_stage"] = pygame.image.load("stage.png")

    gd["game_font"] = pygame.font.Font(None, 40)

    get_num_discs(gd)

    g_bars = [list(range(gd["num_discs"], 0, -1)), [], []]

    gd["bars"] = g_bars

    gd["i_bar"] = pygame.image.load("bar.png")
    gd["i_discs"] = []
    gd["num_moves"] = 0

    gd["expected_moves"] = count_hanoi_tower_moves(gd["num_discs"])

    for i in range(0, 12):
        gd["i_discs"].append(pygame.image.load(f"disc{i + 1}.png"))

    hanoi_tower_simulator(gd, gd["num_discs"], g_bars, 0, 1, 2)

    pygame.time.delay(500)
    get_any_key(gd)
    pygame.quit()
