import arcade
import random

# ─── 常數設定 ─────────────────────────────────────────────────────────
CELL_SIZE     = 20                  # 單格尺寸 (像素)
GRID_WIDTH    = 30                  # 格子寬度
GRID_HEIGHT   = 20                  # 格子高度
SCREEN_WIDTH  = CELL_SIZE * GRID_WIDTH
SCREEN_HEIGHT = CELL_SIZE * GRID_HEIGHT
MOVE_DELAY    = 10                  # 幀數間隔：隔多少幀移動一次

# ─── 主遊戲類別 ───────────────────────────────────────────────────────
class SnakeGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "貪吃蛇 Snake")
        arcade.set_background_color(arcade.color.BLACK)
        # 用 SpriteList 管理蛇身與食物
        self.snake_list = arcade.SpriteList()
        self.food_list = arcade.SpriteList()
        
        # 初始化遊戲
        self.reset()

    def reset(self):
        """重置遊戲狀態"""
        # 座標與方向
        self.snake_x = GRID_WIDTH // 2
        self.snake_y = GRID_HEIGHT // 2
        self.direction = (1, 0)
        self.frame_count = 0
        self.game_over = False
        
        # 清空 SpriteLists
        self.snake_list.clear()
        self.food_list.clear()
        
        # 建立蛇頭
        snake_head = arcade.Sprite()
        snake_head.texture = arcade.make_soft_square_texture(CELL_SIZE, arcade.color.GREEN)
        snake_head.center_x = self.snake_x * CELL_SIZE + CELL_SIZE // 2
        snake_head.center_y = self.snake_y * CELL_SIZE + CELL_SIZE // 2
        self.snake_list.append(snake_head)
        
        # 生一顆食物
        self.spawn_food()

    def spawn_food(self):
        """在空格隨機生成食物"""    
        # 找到所有蛇身佔據的位置
        snake_positions = set()
        for snake_part in self.snake_list:
            x = int(snake_part.center_x // CELL_SIZE)
            y = int(snake_part.center_y // CELL_SIZE)
            snake_positions.add((x, y))
        
        # 找到所有空的位置
        empty_positions = []
        for x in range(GRID_WIDTH):
            for y in range(GRID_HEIGHT):
                if (x, y) not in snake_positions:
                    empty_positions.append((x, y))
        
        # 隨機選擇一個空位置放食物
        if empty_positions:
            food_x, food_y = random.choice(empty_positions)
            food = arcade.Sprite()
            food.texture = arcade.make_soft_square_texture(CELL_SIZE, arcade.color.RED)
            food.center_x = food_x * CELL_SIZE + CELL_SIZE // 2
            food.center_y = food_y * CELL_SIZE + CELL_SIZE // 2
            
            # 更新食物列表
            self.food_list.clear()
            self.food_list.append(food)        

    def on_draw(self):
        """畫面繪製"""
        # 改用 clear() 取代 start_render()
        self.clear()

        # 繪製食物和蛇身
        self.food_list.draw()
        self.snake_list.draw()

        # 顯示分數
        arcade.draw_text(f"Score: {len(self.snake_list)}", 10, SCREEN_HEIGHT - 30,
                        arcade.color.WHITE, 20)

        # Game Over 提示
        if self.game_over:
            arcade.draw_text("GAME OVER! Press R to restart", 
                           SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                           arcade.color.WHITE, 16, 
                           anchor_x="center", anchor_y="center")                    

    def on_update(self, delta_time: float):
        """遊戲邏輯更新：移動、吃食物、自撞檢查"""        
        if self.game_over:
            return

        # 控制移動速率
        self.frame_count += 1
        if self.frame_count < MOVE_DELAY:
            return
        self.frame_count = 0

        # 計算下一格位置
        dx, dy = self.direction
        next_x = self.snake_x + dx
        next_y = self.snake_y + dy

        # 邊界或自撞檢查
        if (next_x < 0 or next_x >= GRID_WIDTH or 
            next_y < 0 or next_y >= GRID_HEIGHT):
            self.game_over = True
            return
        
        # 檢查是否撞到自己
        for snake_part in self.snake_list:
            part_x = int(snake_part.center_x // CELL_SIZE)
            part_y = int(snake_part.center_y // CELL_SIZE)
            if next_x == part_x and next_y == part_y:
                self.game_over = True
                return

        # 更新蛇頭位置
        self.snake_x = next_x
        self.snake_y = next_y

        # 插入新頭 Sprite
        new_head = arcade.Sprite()
        new_head.texture = arcade.make_soft_square_texture(CELL_SIZE, arcade.color.GREEN)
        new_head.center_x = self.snake_x * CELL_SIZE + CELL_SIZE // 2
        new_head.center_y = self.snake_y * CELL_SIZE + CELL_SIZE // 2
        self.snake_list.insert(0, new_head)

        # 吃到食物：生新食物，否則移除尾巴
        ate_food = False
        for food in self.food_list:
            food_x = int(food.center_x // CELL_SIZE)
            food_y = int(food.center_y // CELL_SIZE)
            if self.snake_x == food_x and self.snake_y == food_y:
                ate_food = True
                self.spawn_food()
                break
        
        if not ate_food:
            # 移除尾巴
            if len(self.snake_list) > 0:
                tail = self.snake_list[-1]
                tail.remove_from_sprite_lists()        

    def on_key_press(self, key, modifiers):
        """鍵盤輸入：方向控制 + 重置"""
        # Game Over 後按 R 重置
        if self.game_over and key == arcade.key.R:
            self.reset()
            return

        dx, dy = self.direction
        if key == arcade.key.UP    and dy == 0:
            self.direction = (0, 1)
        if key == arcade.key.DOWN  and dy == 0:
            self.direction = (0, -1)
        if key == arcade.key.LEFT  and dx == 0:
            self.direction = (-1, 0)
        if key == arcade.key.RIGHT and dx == 0:
            self.direction = (1, 0)

# ─── 啟動遊戲 ─────────────────────────────────────────────────────────
if __name__ == "__main__":
    game = SnakeGame()
    arcade.run()