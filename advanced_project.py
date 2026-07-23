import py5
import pandas as pd
import numpy as np
 
# ── データ読み込み ──────────────────────────────────────────────
df = pd.read_csv("Raw_Data.csv")
df.columns = ["time", "ax", "ay", "az", "abs_acc"]
 
# フレームレート相当（約100Hz）でサンプリングされているので
# アニメーション用に再サンプリング（60fps相当）
FPS = 60
duration = df["time"].iloc[-1]
times_60 = np.linspace(0, duration, int(duration * FPS))
abs_acc_interp = np.interp(times_60, df["time"].values, df["abs_acc"].values)
ax_interp     = np.interp(times_60, df["time"].values, df["ax"].values)
ay_interp     = np.interp(times_60, df["time"].values, df["ay"].values)
 
# 加速度の絶対値を 0-1 に正規化
acc_min = abs_acc_interp.min()
acc_max = abs_acc_interp.max()
acc_norm = (abs_acc_interp - acc_min) / (acc_max - acc_min)
 
# ── パーティクル ──────────────────────────────────────────────
class Particle:
    def __init__(self, x, y, color_hue):
        angle  = py5.random(py5.TWO_PI)
        speed  = py5.random(2, 10)
        self.x  = x
        self.y  = y
        self.vx = py5.cos(angle) * speed
        self.vy = py5.sin(angle) * speed
        self.life = 1.0
        self.decay = py5.random(0.012, 0.030)
        self.hue   = color_hue
        self.size  = py5.random(3, 8)
 
    def update(self):
        self.vx *= 0.96
        self.vy *= 0.96
        self.vy += 0.12        # 重力
        self.x  += self.vx
        self.y  += self.vy
        self.life -= self.decay
 
    def draw(self):
        alpha = self.life * 255
        py5.no_stroke()
        py5.fill(self.hue, 220, 255, alpha)
        py5.circle(self.x, self.y, self.size * self.life)
 
    def is_alive(self):
        return self.life > 0
 
# ── グローバル変数 ─────────────────────────────────────────────
particles: list[Particle] = []
frame_idx: int = 0
THRESHOLD = 0.45          # この値以上の正規化加速度で花火を打ち上げ
 
# ── py5 ───────────────────────────────────────────────────────
def setup():
    py5.size(900, 600)
    py5.color_mode(py5.HSB, 360, 255, 255, 255)
    py5.frame_rate(FPS)
 
def draw():
    global frame_idx, particles
 
    # 背景（フェードアウト効果）
    py5.fill(0, 0, 10, 40)
    py5.no_stroke()
    py5.rect(0, 0, py5.width, py5.height)
 
    # 現在フレームのセンサ値
    if frame_idx >= len(acc_norm):
        frame_idx = 0          # ループ再生
 
    a  = acc_norm[frame_idx]
    vx = ax_interp[frame_idx]
    vy = ay_interp[frame_idx]
 
    # 加速度が閾値を超えたら花火を生成
    if a > THRESHOLD:
        n_burst = int(py5.map(a, THRESHOLD, 1.0, 20, 120))
        # X/Y軸加速度を打ち上げ位置にマッピング
        bx = py5.map(vx, -80, 80, py5.width * 0.1, py5.width * 0.9)
        by = py5.map(vy, -80, 80, py5.height * 0.1, py5.height * 0.9)
        bx = py5.constrain(bx, 50, py5.width - 50)
        by = py5.constrain(by, 50, py5.height - 50)
        hue = py5.map(a, THRESHOLD, 1.0, 0, 300)
        for _ in range(n_burst):
            particles.append(Particle(bx, by, hue))
 
    # パーティクル更新・描画
    for p in particles:
        p.update()
        p.draw()
    particles = [p for p in particles if p.is_alive()]
 
    # UI：時間バー
    progress = frame_idx / len(acc_norm)
    py5.no_stroke()
    py5.fill(0, 0, 60, 180)
    py5.rect(20, py5.height - 18, py5.width - 40, 6, 3)
    py5.fill(30, 220, 255, 200)
    py5.rect(20, py5.height - 18, (py5.width - 40) * progress, 6, 3)
 
    # 加速度メーター
    py5.fill(0, 0, 180, 160)
    py5.text_size(13)
    py5.text(f"abs_acc: {abs_acc_interp[frame_idx]:.1f} m/s²  |  "
             f"frame {frame_idx}/{len(acc_norm)}  |  "
             f"particles: {len(particles)}", 24, py5.height - 26)
 
    frame_idx += 1
 
py5.run_sketch()