import os
import sys

def count_subsubfolders(folder_path):
    results = {}
    # サブフォルダごとに処理
    for subfolder in os.scandir(folder_path):
        if subfolder.is_dir():
            # サブサブフォルダをカウント
            subsubfolder_count = sum(
                1 for entry in os.scandir(subfolder.path) if entry.is_dir()
            )
            results[subfolder.name] = subsubfolder_count
    return results

# 引数のチェック
if len(sys.argv) != 3:
    print("Usage: python script.py <destination_dir> <output_file>")
    sys.exit(1)

# フォルダパスと出力ファイル名を取得
destination_dir = sys.argv[1]
output_file = sys.argv[2]

# シナリオ数をカウント
results = count_subsubfolders(destination_dir)

# 結果をファイルに保存
with open(output_file, "w") as file:
    for subfolder, count in results.items():
        file.write(f"{subfolder}: {count}\n")

print(f"Results have been saved to {output_file}")