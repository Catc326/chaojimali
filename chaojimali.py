import random

def play_super_mario():
    player = "@"
    enemy = "E"
    coins = "C"
    goal = "G"
    empty = "_"
    
    # 游戏地图
    level = [
        [empty, enemy, coins, empty],
        [empty, coins, empty, empty],
        [empty, empty, coins, enemy],
        [player, coins, enemy, goal]
    ]
    
    player_x, player_y = 3, 0
    coins_collected = 0
    is_game_over = False
    
    print("欢迎来到超级玛丽！")
    print_level(level)
    
    while not is_game_over:
        move = input("请输入你的移动方向 (W/A/S/D): ").upper()
        
        if move not in ["W", "A", "S", "D"]:
            print("无效的移动方向！请重新输入。")
            continue
        
        # 计算新位置
        new_player_x, new_player_y = player_x, player_y
        if move == "W":
            new_player_y -= 1
        elif move == "A":
            new_player_x -= 1
        elif move == "S":
            new_player_y += 1
        elif move == "D":
            new_player_x += 1
        
        # 判断新位置的有效性
        if new_player_x < 0 or new_player_x >= len(level[0]) or new_player_y < 0 or new_player_y >= len(level):
            print("超出边界！请重新输入。")
            continue
        
        # 判断新位置上的元素
        element = level[new_player_y][new_player_x]
        if element == enemy:
            print("遇到敌人！游戏结束。")
            is_game_over = True
        elif element == coins:
            coins_collected += 1
            print(f"收集到 {coins_collected} 个金币！")
            level[new_player_y][new_player_x] = player
        elif element == goal:
            print("恭喜通关！你赢了！")
            is_game_over = True
        else:
            level[new_player_y][new_player_x] = player
            level[player_y][player_x] = empty
        
        player_x, player_y = new_player_x, new_player_y
        print_level(level)
    
def print_level(level):
    for row in level:
        print(" ".join(row))

if __name__ == "__main__":
    play_super_mario()
