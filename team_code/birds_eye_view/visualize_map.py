import h5py
import matplotlib.pyplot as plt

# H5ファイルを読み込む
with h5py.File('/mnt/ssd/carla_garage/team_code/birds_eye_view/maps_4ppm_cv/Town12.h5', 'r') as hf:
    road_mask = hf['road'][:]
    sidewalk_mask = hf['sidewalk'][:]
    lane_marking_all = hf['lane_marking_all'][:]

# マスクを可視化
plt.figure(figsize=(15, 5))
plt.subplot(1, 3, 1)
plt.title("Road Mask")
plt.imshow(road_mask, cmap='gray')

plt.subplot(1, 3, 2)
plt.title("Sidewalk Mask")
plt.imshow(sidewalk_mask, cmap='gray')

plt.subplot(1, 3, 3)
plt.title("Lane Markings")
plt.imshow(lane_marking_all, cmap='gray')

plt.show()
