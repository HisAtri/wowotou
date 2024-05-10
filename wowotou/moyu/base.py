from typing import Iterable


class Base4:
    @staticmethod
    def encode(data: bytes, mapping: str = 'abcd') -> str:
        if len(mapping) != 4:
            raise ValueError("Mapping must contain exactly 4 characters")
        encoded_data = []
        for byte in data:
            # 遍历字节的每个2位组，从最高位开始
            for i in [6, 4, 2, 0]:
                two_bits = (byte >> i) & 0b11
                mapped_value = mapping[two_bits]
                encoded_data.append(mapped_value)

        return ''.join(encoded_data)

    @staticmethod
    def decode(data: str, mapping: str = 'abcd') -> bytes:
        # 确保映射表长度是4
        if len(mapping) != 4:
            raise ValueError("Mapping must contain exactly 4 characters")

        if len(set(mapping)) != len(mapping):
            raise ValueError("Mapping characters must be unique")

        decoded_data = bytearray()
        byte: int = 0
        round = 0

        # 遍历每个字符
        for char in data:
            index = mapping.index(char)
            two_bits: int = index
            round += 1
            if round == 4:
                byte = (byte << 2) + two_bits
                decoded_data.append(byte)
                byte = 0
                round = 0
            else:
                byte = (byte << 2) + two_bits
        return bytes(decoded_data)


if __name__ == '__main__':
    data = '我要玩原神'.encode(encoding='utf-8')
    encoded_data = Base4.encode(data=data, mapping='原神启动')
    print(encoded_data)
    decoded_data = Base4.decode(data=encoded_data, mapping='原神启动')
    print(decoded_data.decode(encoding='utf-8'))
