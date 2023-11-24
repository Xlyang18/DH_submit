import os

# 定义游戏元素的符号
EMPTY = 0
WALL = 1
PLAYER = 2
BOX = 3
TARGET = 4

# 定义三个关卡的地图
maps = [
    [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 2, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 3, 3, 4, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 4, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 3, 0, 4, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    ],
    [
        # 定义第二关的地图
    ],
    [
        # 定义第三关的地图
    ]
]


# 初始化游戏
def init_game():
    print("\n\n\n推箱子游戏 - 按任意键开始")
    input()


# 初始化当前关卡的地图
def init_map(level):
    return [row[:] for row in maps[level]]


# 绘制地图
def draw_map(maparr):
    os.system("clear" if os.name == "posix" else "cls")
    for row in maparr:
        for cell in row:
            if cell == EMPTY:
                print("  ", end="")
            elif cell == WALL:
                print("■", end="")
            elif cell == PLAYER:
                print("♀", end="")
            elif cell == BOX:
                print("●", end="")
            elif cell == TARGET:
                print("☆", end="")
        print()


# 更新游戏数据
def run_game(maparr):
    player_x, player_y = find_element(maparr, PLAYER)

    key = input("输入 W, A, S, D 移动玩家（或 Q 退出）: ").lower()

    if key == 'q':
        return False
    elif key in ['w', 'a', 's', 'd']:
        move_in_map(maparr, player_x, player_y, key)
        return True
    else:
        print("无效输入。请按 W, A, S, D 移动或按 Q 退出。")
        return True


# 查找玩家在地图中的位置
def find_element(maparr, element):
    for i in range(len(maparr)):
        for j in range(len(maparr[i])):
            if maparr[i][j] == element:
                return i, j


# 移动玩家在地图中
def move_in_map(maparr, player_x, player_y, direction):
    delta_x, delta_y = 0, 0

    if direction == 'w':
        delta_x = -1
    elif direction == 'a':
        delta_y = -1
    elif direction == 's':
        delta_x = 1
    elif direction == 'd':
        delta_y = 1

    new_x, new_y = player_x + delta_x, player_y + delta_y
    target = maparr[new_x][new_y]

    if target == EMPTY or target == TARGET:
        maparr[player_x][player_y] = EMPTY
        maparr[new_x][new_y] = PLAYER
    elif target == BOX:
        new_box_x, new_box_y = new_x + delta_x, new_y + delta_y
        if maparr[new_box_x][new_box_y] == EMPTY or maparr[new_box_x][new_box_y] == TARGET:
            maparr[player_x][player_y] = EMPTY
            maparr[new_x][new_y] = PLAYER
            maparr[new_box_x][new_box_y] = BOX


# 检查游戏是否结束
def end_game(maparr):
    return all(cell != BOX for row in maparr for cell in row)


def main():
    init_game()
    level = 0
    while level < 3:
        maparr = init_map(level)
        while True:
            draw_map(maparr)
            if run_game(maparr):
                if end_game(maparr):
                    level += 1
                    if level < 3:
                        print("恭喜！你已完成本关。")
                        input("按任意键继续下一关。")
                    else:
                        print("恭喜！你已完成所有关卡。")
                        break
            else:
                print("再见！")
                break


if __name__ == "__main__":
    main()
