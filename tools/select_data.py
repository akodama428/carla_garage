import os
import random
import subprocess

# 元のデータフォルダのパス
source_dir = "/home/atsushi/carla_garage/data"
# 移動先のフォルダのパス
destination_dir = "/home/atsushi/carla_garage/data_selected"

# 2階層目のフォルダから抽出する数
num_to_select = 25

def move_folders(source, destination, num_to_select):
    """
    mv を使用してフォルダ構造を移動し、2階層目のフォルダから指定された数をランダムに選んで移動する
    """
    # 1階層目のフォルダをループ
    for first_level_folder in os.listdir(source):
        source_first_level_path = os.path.join(source, first_level_folder)
        destination_first_level_path = os.path.join(destination, first_level_folder)

        # 1階層目がディレクトリである場合のみ処理
        if os.path.isdir(source_first_level_path):
            # 移動先の1階層目フォルダを作成
            os.makedirs(destination_first_level_path, exist_ok=True)

            # 2階層目のフォルダを取得
            second_level_folders = [
                f for f in os.listdir(source_first_level_path)
                if os.path.isdir(os.path.join(source_first_level_path, f))
            ]

            # 2階層目のフォルダをランダムに抽出
            selected_folders = random.sample(second_level_folders, min(num_to_select, len(second_level_folders)))

            # mv を使ってフォルダを移動
            for folder in selected_folders:
                source_folder_path = os.path.join(source_first_level_path, folder)
                destination_folder_path = os.path.join(destination_first_level_path, folder)

                print(f"Moving {source_folder_path} to {destination_folder_path} using mv")
                subprocess.run(["mv", source_folder_path, destination_folder_path], check=True)

# 実行
move_folders(source_dir, destination_dir, num_to_select)
