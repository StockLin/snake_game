# 🐍 貪吃蛇 Workshop 指引

此份文件讓你**專注在算法、動作、行為**實作，使用 `arcade` API，快速完成 Snake 遊戲核心功能。  
請打開 `snake.py`，在 `# TODO` 標記處完成對應程式。

---

## 🛠 環境準備

1. 安裝依賴  
    poetry add arcade  
    擇一使用。

2. 確認能啟動模板  
    python snake.py  
    這時會開啟一個空白黑色視窗。

---

## 🎯 填空區段

### 1. 重置遊戲 (reset)

    def reset(self):
        # 重置遊戲狀態：初始化蛇身、方向、計時
        self.snake_coords = [(GRID_WIDTH//2, GRID_HEIGHT//2)]
        self.direction    = (1, 0)
        self._frame       = 0
        self.game_over    = False

        # TODO: 建立並清空 self.snake_list (arcade.SpriteList)
        # TODO: 產生一個蛇頭 (SpriteSolidColor)，設定 center_x/center_y，加入 self.snake_list

        # TODO: 呼叫 self.spawn_food() 生成第一顆食物

### 2. 每幀更新 (on_update)

    def on_update(self, delta_time):
        if self.game_over:
            return

        # 幀數控制移動速度
        self._frame += 1
        if self._frame < MOVE_DELAY:
            return
        self._frame = 0

        # TODO: head_x, head_y = self.snake_coords[0]
        # TODO: dx, dy = self.direction
        # TODO: new_head = (head_x+dx, head_y+dy)

        # TODO: 邊界檢查 → if outside grid: self.game_over = True; return
        # TODO: 自撞檢查 → if new_head in self.snake_coords: self.game_over = True; return

        # TODO: 插入 new_head 到 self.snake_coords 前端
        # TODO: 建立新蛇節點，設定位置，self.snake_list.insert(0, seg)

        # TODO: 如果 new_head == self.food_pos:
        #           self.spawn_food()
        #       else:
        #           移除尾巴：self.snake_list.pop(), self.snake_coords.pop()

### 3. 食物生成功能 (spawn_food)

    def spawn_food(self):
        # 隨機在空格生成食物，並更新 self.food_pos + self.food_list
        # TODO: 建立 empties 列表：所有 (x,y) 不在 self.snake_coords
        # TODO: fx, fy = random.choice(empties)
        # TODO: food = arcade.SpriteSolidColor(CELL_SIZE, CELL_SIZE, arcade.color.RED)
        # TODO: 設定 food.center_x, food.center_y
        # TODO: 清空 self.food_list，append(food)，設定 self.food_pos = (fx, fy)

### 4. 鍵盤輸入 (on_key_press)

    def on_key_press(self, key, modifiers):
        # TODO: if self.game_over and key == arcade.key.R:
        #           self.reset()
        #           return
        dx, dy = self.direction
        # TODO: if key == arcade.key.UP and dy == 0:     self.direction = (0, 1)
        # TODO: if key == arcade.key.DOWN and dy == 0:   self.direction = (0, -1)
        # TODO: if key == arcade.key.LEFT and dx == 0:   self.direction = (-1, 0)
        # TODO: if key == arcade.key.RIGHT and dx == 0:  self.direction = (1, 0)

### 5. 繪製畫面 (on_draw)

    def on_draw(self):
        # TODO: 呼叫 self.clear() 清除畫面
        # TODO: self.food_list.draw()
        # TODO: self.snake_list.draw()
        # TODO: if self.game_over:
        #           arcade.draw_text("Game Over! Press R to Restart", SCREEN_WIDTH/2, SCREEN_HEIGHT/2, arcade.color.WHITE, 24, anchor_x="center", anchor_y="center")

---

## 📚 常用 Arcade API

| API                                 | 說明                                 |
|-------------------------------------|--------------------------------------|
| arcade.Window(w, h, title)          | 建立遊戲視窗                         |
| self.clear()                        | 清除畫面背景                         |
| arcade.SpriteSolidColor(w,h,color)  | 建立純色方塊 Sprite                  |
| sprite.center_x, sprite.center_y    | 設定 Sprite 中心座標                 |
| arcade.SpriteList()                 | 高效管理多個 Sprite                  |
| sprite_list.draw()                  | 一次繪製整組 Sprites                 |
| on_update(self, delta_time)         | 每幀遊戲邏輯更新                     |
| on_draw(self)                       | 每幀畫面繪製                         |
| on_key_press(self, key, mods)       | 處理鍵盤按下事件                     |
| arcade.key.UP/DOWN/LEFT/RIGHT       | 鍵盤方向鍵常數                       |
| random.choice(list)                 | 隨機選取列表元素                     |
| list.insert(idx, item), list.pop()  | 列表操作                             |

完成 TODO 填空後，即可運行並體驗：  
- **算法**：移動、生成、碰撞  
- **行為**：鍵盤控制、生長、Game Over

祝 Workshop 順利！
