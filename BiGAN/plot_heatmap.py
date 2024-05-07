import os
import cv2
import numpy as np

for filename in os.listdir('data/visCXR/ori'):
    if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".jpeg"):
        ori_path = os.path.join('data/visCXR/ori', filename)
        rec_path = os.path.join('data/visCXR/rec', filename)

        # ori, rec都是64*64，且像素值為[0, 255]
        ori = cv2.imread(ori_path)
        ori = cv2.resize(ori, (64, 64))
        ori = ori.astype(np.float32)

        rec = cv2.imread(rec_path)
        rec = rec.astype(np.float32)

        # mask = (ori和rec的差)^2
        # 計算絕對差值並平方
        mask = np.square(np.abs(ori - rec))
        # 歸一化到[0, 255]範圍
        mask /= 255

        # call熱度圖函式、疊加到ori、縮放到[0, 255]
        heatmap = cv2.applyColorMap(np.uint8(mask), cv2.COLORMAP_HOT)
        cam = heatmap + ori
        cam = (cam/np.max(cam))*255

        #plt.imshow(cv2.cvtColor(cam, cv2.COLOR_BGR2RGB))   # 如果要show的話，上一行不用乘255
        #plt.show()
        cv2.imwrite(f'data/visCXR/heatmap/{filename}', cam)
