import os

# 设置目标文件夹路径
folder_path = './Fusion'

# 获取文件夹内所有文件的列表
files = os.listdir(folder_path)
# 排除隐藏文件和文件夹
files = [f for f in files if not f.startswith('.') and os.path.isfile(os.path.join(folder_path, f))]

# 按文件名排序
files.sort()

# 遍历文件并重命名
for index, file in enumerate(files, start=1):
    # 构造新文件名（保持原始扩展名不变）
    new_file_name = f"{index}{os.path.splitext(file)[1]}"
    
    # 构造原始和新的完整文件路径
    original_file_path = os.path.join(folder_path, file)
    new_file_path = os.path.join(folder_path, new_file_name)
    
    # 重命名文件
    os.rename(original_file_path, new_file_path)

    print(f"Renamed {file} to {new_file_name}")
    
print("Renaming completed.")
