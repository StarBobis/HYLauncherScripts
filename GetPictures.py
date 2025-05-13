import os
import shutil
import sys

def main():
    # 获取AppData/Roaming目录
    appdata_roaming = os.getenv('APPDATA')
    if not appdata_roaming:
        print("无法获取AppData/Roaming目录")
        sys.exit(1)

    # 构建源目录路径
    source_dir = os.path.join(
        appdata_roaming, 'miHoYo', 'HYP', '1_1', 'fedata', 'Cache', 'Cache_Data'
    )

    # 检查源目录是否存在
    if not os.path.exists(source_dir):
        print(f"错误：源目录不存在 - {source_dir}")
        sys.exit(1)

    # 创建目标目录
    dest_dir = os.path.join(os.getcwd(), 'Pictures')
    os.makedirs(dest_dir, exist_ok=True)

    # 遍历并复制文件
    for filename in os.listdir(source_dir):
        src_path = os.path.join(source_dir, filename)
        
        if os.path.isfile(src_path):
            # 移除原始扩展名并添加.png
            base_name = os.path.splitext(filename)[0]
            dest_filename = f"{base_name}.png"
            dest_path = os.path.join(dest_dir, dest_filename)

            try:
                shutil.copy2(src_path, dest_path)
                print(f"已复制：{filename} -> {dest_filename}")
            except Exception as e:
                print(f"复制失败：{filename} | 错误：{str(e)}")

if __name__ == "__main__":
    main()