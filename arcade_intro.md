
# 🎮 Arcade 遊戲框架介紹

## 📌 是什麼？
`arcade` 是一個用 Python 編寫的 **現代 2D 遊戲框架**，專注於**簡潔、易用與教學友好**。  
它是 `pygame` 的精神接班人，使用 `OpenGL` 實現更流暢的畫面渲染，特別適合教學、學習與小型遊戲開發。

官網：[https://api.arcade.academy](https://api.arcade.academy)

---

## 🚀 技術特點

| 項目 | 說明 |
|------|------|
| 語言 | Python 3.6+（建議 3.8+） |
| 圖形引擎 | 使用 `OpenGL` 提供 GPU 加速的 2D 渲染 |
| 架構設計 | 面向物件設計（繼承 `arcade.Window`） |
| 輸出模式 | 原生視窗（支援 macOS / Windows / Linux） |
| 常用元件 | `Sprite`, `SpriteList`, `Texture`, `View`, `Sound`, `PhysicsEngine` |
| 內建功能 | 圖片載入、碰撞偵測、音效播放、鍵盤／滑鼠輸入 |

---

## ✅ 優點

| 優點 | 說明 |
|------|------|
| 🎓 **教學友好** | 內建簡潔 API，極適合初學者、課堂教學與 Workshop |
| 🚀 **現代化設計** | 使用 `OpenGL` 渲染 + 面向物件，取代傳統 `pygame` 程式風格 |
| 📦 **內建豐富資源** | 提供音效、素材、物理引擎、camera 滾動視野等功能 |
| 🔁 **事件循環清晰** | 明確劃分 `on_draw()`, `on_update()`, `on_key_press()` |
| 🧱 **模組化程式架構** | 支援多畫面切換 (`View`)，適合多人開發或遊戲分層設計 |

---

## ❌ 缺點

| 缺點 | 補充說明 |
|------|---------|
| 🐍 只支援 Python | 無法跨語言或跨平台為 Web／行動 App |
| 🔋 效能有限 | 雖使用 OpenGL，但仍不適合大型或高效能遊戲 |
| 📉 社群相對較小 | 相比 `pygame` 與主流引擎（Unity, Godot），資料與範例較少 |
| 📦 第三方整合少 | 不如主流引擎有完整的資源商城、動畫工具、粒子特效等 |

---

## ⚡ 快速上手指引

### 📦 安裝 Arcade

```bash
poetry add arcade
# 或
pip install arcade
```

### 🧪 最簡單的 Hello World 遊戲

```python
import arcade

WIDTH = 800
HEIGHT = 600

class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(WIDTH, HEIGHT, "Hello Arcade")
        arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Hello, Arcade!", 300, 300, arcade.color.WHITE, 24)

game = MyGame()
arcade.run()
```

---

### 🔁 遊戲循環簡介

| 函式 | 用途 |
|------|------|
| `__init__()` | 遊戲初始化邏輯 |
| `setup()` | 可選，初始化或重設場景（常見於遊戲開始、重新開始） |
| `on_draw()` | 每次畫面刷新時呼叫，用來畫出背景、角色、文字等 |
| `on_update(delta_time)` | 每幀遊戲邏輯更新，處理移動、碰撞等 |
| `on_key_press()` | 鍵盤按下事件（也可搭配 `on_key_release`） |

---

## 🔧 補充工具

| 工具 | 說明 |
|------|------|
| `arcade.SpriteList` | 效能優化的 Sprite 管理器 |
| `arcade.View` | 多畫面支援，管理主選單／關卡等 |
| `arcade.PhysicsEngineSimple` | 物件碰撞處理 |
| `arcade.Text` | 螢幕中文字渲染 |
| Tile Map 支援 | 可用 Tiled 製作地圖、角色與場景布局 |

---

## 📚 學習資源推薦

| 資源 | 連結 |
|------|------|
| 官方文件 | [api.arcade.academy](https://api.arcade.academy) |
| 官方範例程式 | [GitHub - arcade/examples](https://github.com/pythonarcade/arcade/tree/development/samples) |
| 教學網站 | [realpython 教學](https://realpython.com/arcade-python-game-framework/) |
| YouTube 教學 | [Search: "arcade python game"](https://www.youtube.com/results?search_query=arcade+python+game) |
