import struct

def encode_student_info(name, age, phone, address):
    # 编码学生姓名（UTF-8）编码学生年龄（ASCII） 编码学生手机号（ASCII） 编码学生家庭住址（GBK）
    name_encoded = name.encode('utf-8')
    age_encoded = struct.pack('B', age)
    phone_encoded = phone.encode('ascii')
    address_encoded = address.encode('gbk')

    # 计算各字段的长度
    name_length = len(name_encoded)
    phone_length = len(phone_encoded)
    address_length = len(address_encoded)

    tlv_data = (
        struct.pack('B', 0x01) + struct.pack('>H', name_length) + name_encoded +
        struct.pack('B', 0x02) + struct.pack('>H', 1) + age_encoded +
        struct.pack('B', 0x03) + struct.pack('>H', phone_length) + phone_encoded +
        struct.pack('B', 0x04) + struct.pack('>H', address_length) + address_encoded
    )

    return tlv_data

students = [
    ("张三", 18, "13712345678", "北京市朝阳区"),
    ("李四", 17, "18809876543", "上海市闵行区"),
    ("王五", 19, "16129384756", "湖北省武汉市"),
    ("马六", 20, "18912332111", "河北省石家庄市")
]

# 对每个学生信息进行编码
for student in students:
    encoded_data = encode_student_info(*student)
    print("Encoded data for {}: {}".format(student[0], encoded_data.hex()))
