from Heuristics.helper import line_checker

def sanity_check(tictactoe, mark, n):
    combos = []
    combos_2 = []
    combos_3 = []
    combos_4 = []

    if n == 2:
        combo = "-" + mark + mark
        combos_2.append((combo,1))

        combo = mark + mark + "-"
        combos_2.append((combo,1))

        combo = mark + "-" + mark
        combos_2.append((combo,1))

    if n == 3:
        combo = mark + "-" + mark + mark
        combos_3.append((combo,1))

        combo = mark + mark + "-" + mark
        combos_3.append((combo,1))

        combo = mark + mark + mark + "-"
        combos_3.append((combo,1))

        combo = "-" + mark + mark + mark
        combos_3.append((combo,1))

    if n == 4:
        combo = mark + "-" + mark + mark + mark
        combos_4.append((combo,1))

        combo = mark + mark + "-" + mark + mark
        combos_4.append((combo,1))

        combo = mark + mark + mark + "-" + mark
        combos_4.append((combo,1))

        combo = "-" + mark + mark + mark + mark
        combos_4.append((combo,1))

        combo = mark + mark + mark + mark + "-"
        combos_4.append((combo,1))

    if n == 2:
        combos = combos_2
    if n == 3:
        combos = combos_3
    if n == 4:
        combos = combos_4

    count = line_checker(combos, tictactoe, n)

    # # checks horizontal_lines
    # for i in range(tictactoe.board_size):
    #     rivi: str = tictactoe.state[
    #         i * tictactoe.board_size : i * tictactoe.board_size + tictactoe.board_size
    #     ]
    #     # print(rivi)
    #     for combo in combos:
    #         if rivi.__contains__(combo):
    #             # print("mark", mark, "osuma rivillä", rivi)
    #             count += 1
    #             # print("count", count)

    # # checks vertical_lines
    # for i in range(tictactoe.board_size):
    #     rivi = ""
    #     for j in range(tictactoe.board_size):
    #         rivi += tictactoe.state[j * tictactoe.board_size + i]
    #     # print(rivi)
    #     for combo in combos:
    #         if rivi.__contains__(combo):
    #             # print("mark", mark, "osuma rivillä", rivi)
    #             count += 1
    #             # print("count", count)

    # # checks diagonal lines from top row to right-down
    # for i in range(tictactoe.board_size):
    #     max_length = tictactoe.board_size - i
    #     rivi = ""
    #     if i <= tictactoe.board_size - n - 1:
    #         for j in range(tictactoe.board_size):
    #             if len(rivi) < max_length:
    #                 rivi += tictactoe.state[i + j * (tictactoe.board_size + 1)]
    #     for combo in combos:
    #         if rivi.__contains__(combo):
    #             count += 1

    # # checks diagonal lines from top row to left-down
    # # print("checkpoint 1")
    # for i in range(tictactoe.board_size - 1, -1, -1):
    #     max_length = i + 1
    #     rivi = ""
    #     if i >= n:  ########CORRECTION
    #         for j in range(tictactoe.board_size):
    #             if len(rivi) < max_length:
    #                 rivi += tictactoe.state[i + j * (tictactoe.board_size - 1)]
    #         # print(rivi)
    #     for combo in combos:
    #         if rivi.__contains__(combo):
    #             # print("checkpoint 2. mark", mark, "osuma rivillä", rivi)
    #             count += 1
    #             # print("count", count)

    # # checks diagonal lines from left column to right-down
    # for j in range(
    #     1, tictactoe.board_size
    # ):  # top-left corner has already been checked. Thus starting from row 1.
    #     max_length = tictactoe.board_size - j
    #     rivi = ""
    #     if j <= tictactoe.board_size - n - 1:  #########CORRECTION
    #         for i in range(tictactoe.board_size):
    #             if len(rivi) < max_length:
    #                 rivi += tictactoe.state[
    #                     j * tictactoe.board_size + i * (tictactoe.board_size + 1)
    #                 ]
    #         # print(rivi)
    #     for combo in combos:
    #         if rivi.__contains__(combo):
    #             # print("checkpoint 3. mark", mark, "osuma rivillä", rivi)
    #             count += 1
    #             # print("count", count)

    # # checks diagonal lines from right column to left-down
    # # print("checkpoint 2")
    # for j in range(
    #     1, tictactoe.board_size
    # ):  # top-right corner has already been checked. Thus starting from row 1.
    #     max_length = tictactoe.board_size - j
    #     rivi = ""
    #     if j <= tictactoe.board_size - n - 1:  #########CORRECTION
    #         for i in range(tictactoe.board_size):
    #             if len(rivi) < max_length:
    #                 rivi += tictactoe.state[
    #                     (tictactoe.board_size - 1)
    #                     + j * (tictactoe.board_size)
    #                     + i * (tictactoe.board_size - 1)
    #                 ]
    #         # print(rivi)
    #     for combo in combos:
    #         if rivi.__contains__(combo):
    #             # print("checkpoitn 4. mark", mark, "osuma rivillä", rivi)
    #             count += 1
    #             # print("count", count)

    return count
