import arcade
import random

# ─── 常數設定 ─────────────────────────────────────────────────────────
CELL_SIZE     = 20                  # 單格尺寸 (像素)
GRID_WIDTH    = 30                  # 格子寬度
GRID_HEIGHT   = 20                  # 格子高度
SCREEN_WIDTH  = CELL_SIZE * GRID_WIDTH
SCREEN_HEIGHT = CELL_SIZE * GRID_HEIGHT
MOVE_DELAY    = 8                   # 幀數間隔：隔多少幀移動一次

# ─── 主遊戲類別 ───────────────────────────────────────────────────────
class SnakeGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "貪吃蛇 Snake")
        arcade.set_background_color(arcade.color.BLACK)
        # 用 SpriteList 管理蛇身與食物
        # TODO:

    def reset(self):
        """重置遊戲狀態"""
        # 座標與方向

        # 清空 SpriteLists        

        # 建立蛇頭    

        # 生一顆食物

    def spawn_food(self):
        """在空格隨機生成食物"""    

        # 更新食物列表        

    def on_draw(self):
        """畫面繪製"""
        # 改用 clear() 取代 start_render()
        self.clear()

        # 繪製食物和蛇身        

        # Game Over 提示                    

    def on_update(self, delta_time: float):
        """遊戲邏輯更新：移動、吃食物、自撞檢查"""        

        # 控制移動速率        

        # 計算下一格位置        

        # 邊界或自撞檢查        

        # 插入新頭 Sprite        

        # 吃到食物：生新食物，否則移除尾巴        

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