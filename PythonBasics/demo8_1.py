def split_file(file_name, chunk_size):
    try:
        with open(file_name, 'rb') as file:
            part_num = 1
            while True:
                chunk = file.read(chunk_size)
                if not chunk:
                    break
                part_file_name = f"{file_name}.part{part_num}"
                with open(part_file_name, 'wb') as part_file:
                    part_file.write(chunk)
                part_num += 1
            print(f"文件成功分割成 {part_num - 1} 个部分。")
    except FileNotFoundError:
        print("文件未找到！")


if __name__ == "__main__":
    file_name = input("请输入需切割的文件名：")
    chunk_size = int(input("请输入需要切割的块大小（单位为字节）："))
    split_file(file_name, chunk_size)
