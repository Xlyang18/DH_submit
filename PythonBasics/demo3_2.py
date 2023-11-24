def base64_encode(input_string):
    base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    result = []
    # 将输入字符串转换为字节数据
    input_bytes = input_string.encode('utf-8')
    i = 0
    while i < len(input_bytes):
        # 读取3个字节
        chunk = input_bytes[i:i + 3]
        # 将3字节数据转换为一个24位整数
        value = int.from_bytes(chunk, byteorder='big')

        for j in range(3, -1, -1):
            index = (value >> (j * 6)) & 0b111111
            result.append(base64_chars[index])
        i += 3
    # 补充 '=' 字符，以确保编码后的字符串长度为4的倍数
    padding = len(result) % 4
    if padding > 0:
        result.extend(['='] * (4 - padding))
    return ''.join(result)


original_text = "hello xly!"
encoded_text = base64_encode(original_text)
print("字符串 “%s” 经过 Base64 编码结果:\n%s" % (original_text, encoded_text))
