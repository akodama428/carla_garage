import h5py
import numpy as np
import matplotlib.pyplot as plt
import xml.etree.ElementTree as ET

# H5ファイルを読み込む
with h5py.File('/mnt/ssd/carla_garage/team_code/birds_eye_view/maps_4ppm_cv/Town01.h5', 'r') as hf:
    road_mask = hf['road'][:]
    sidewalk_mask = hf['sidewalk'][:]
    lane_marking_all = hf['lane_marking_all'][:]
    world_offset = np.array(hf.attrs['world_offset_in_meters'], dtype=np.float32)
    pixels_per_meter = hf.attrs['pixels_per_meter'] 

# 画像のスケール変換（ピクセルからメートルへ）
height, width = road_mask.shape
width_meters = width / pixels_per_meter
height_meters = height / pixels_per_meter

# world_offset を適用するための座標範囲
x_min = world_offset[0]
x_max = x_min + width_meters
y_min = world_offset[1] - 395  ## オフセットしないとずれる
y_max = y_min + height_meters

# OpenScenarioのXMLから複数のウェイポイントを取得
tree = ET.parse('/mnt/ssd/carla_garage/leaderboard/data/longest6.xml')  # OpenScenarioファイルのパスを指定
root = tree.getroot()

route_colors = [
    'r', 'g', 'b', 'c', 'm', 'y', 'orange', 'purple', 'brown', 'pink'
]

# マスクを可視化
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.title("Road Mask")
plt.imshow(road_mask, cmap='gray', extent=[x_min, x_max, y_min, y_max])
plt.xlabel("Meters")
plt.ylabel("Meters")

plt.subplot(1, 3, 2)
plt.title("Sidewalk Mask")
plt.imshow(sidewalk_mask, cmap='gray', extent=[x_min, x_max, y_min, y_max])
plt.xlabel("Meters")
plt.ylabel("Meters")

# 各ルートのウェイポイントをプロット
for route_id in range(1):  # ルートID 0～5 @Town01
    waypoints = []
    route = root.find(f".//route[@id='{route_id}']")
    if route is not None:
        for position in route.find('waypoints').iter('position'):
            x = float(position.attrib['x'])
            y = -float(position.attrib['y']) # Y軸反転
            waypoints.append((x, y))
        if waypoints:
            waypoints_x, waypoints_y = zip(*waypoints)
            plt.plot(waypoints_x, waypoints_y, 'o-', color=route_colors[route_id % len(route_colors)], markersize=5, label=f'Route {route_id}')

# plt.legend()

plt.subplot(1, 3, 3)
plt.title("Lane Markings")
plt.imshow(lane_marking_all, cmap='gray', extent=[x_min, x_max, y_min, y_max])
plt.xlabel("Meters")
plt.ylabel("Meters")

plt.show()