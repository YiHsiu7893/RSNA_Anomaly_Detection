import numpy as np
import matplotlib.pyplot as plt

# 讀取npy檔
data = np.load('./DATASETS/Train/image_0.npy')

# 顯示圖片
plt.imshow(data, cmap='gray')  # 使用灰度顏色映射
plt.axis('off')  # 關閉座標軸
plt.show()
