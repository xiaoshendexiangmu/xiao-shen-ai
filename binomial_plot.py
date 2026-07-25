"""
二项分布可视化：抛10次硬币，出现k次正面的概率
Binomial Distribution: P(X=k) = C(10,k) * 0.5^10
"""

import math
import numpy as np
import matplotlib.pyplot as plt

# 设置中文字体（避免乱码）
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

n = 10      # 抛10次
p = 0.5     # 每次正面的概率

# 计算 k = 0 到 10 的概率
k_values = list(range(n + 1))
probabilities = []

for k in k_values:
    # P(X=k) = C(n,k) * p^k * (1-p)^(n-k)
    prob = math.comb(n, k) * (p ** k) * ((1 - p) ** (n - k))
    probabilities.append(prob)

# 画图
plt.figure(figsize=(10, 6))
bars = plt.bar(k_values, probabilities, color='#9775fa', edgecolor='#6741d9', linewidth=1.5)

# 在柱子上标注概率值
for bar, prob in zip(bars, probabilities):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.005,
             f'{prob:.3f}', ha='center', va='bottom', fontsize=9)

plt.xlabel('正面次数 k', fontsize=14)
plt.ylabel('概率 P(X=k)', fontsize=14)
plt.title(f'二项分布 B(n={n}, p={p})\n抛{n}次硬币出现k次正面的概率', fontsize=15)
plt.xticks(k_values)
plt.ylim(0, max(probabilities) + 0.05)
plt.grid(axis='y', alpha=0.3)

# 保存图片
plt.savefig('binomial_distribution.png', dpi=150, bbox_inches='tight')
print(f"✅ 图片已保存: binomial_distribution.png")
print(f"\n概率分布表 (n={n}, p={p}):")
print(f"{'k':>3} | {'P(X=k)':>8} | {'柱状图':<20}")
print("-" * 35)
for k, prob in zip(k_values, probabilities):
    bar_chars = '█' * int(prob * 100)
    print(f"{k:>3} | {prob:>8.3f} | {bar_chars}")
