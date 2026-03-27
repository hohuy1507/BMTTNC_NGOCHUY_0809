class RailFenceCipher:
    def __init__(self):
        pass

    def rail_fence_encrypt(self, plain_text, num_rails):
        # Bắt lỗi: Nếu key <= 1 hoặc chuỗi rỗng thì không cần mã hóa
        if num_rails <= 1 or not plain_text:
            return plain_text

        rails = [[] for _ in range(num_rails)]
        rail_index = 0
        direction = 1  # 1: đi xuống, -1: đi lên

        for char in plain_text:
            rails[rail_index].append(char)
            # Chạm đỉnh ray -> đổi hướng đi xuống
            if rail_index == 0:
                direction = 1
            # Chạm đáy ray -> đổi hướng đi lên
            elif rail_index == num_rails - 1:
                direction = -1
            
            rail_index += direction

        cipher_text = ''.join(''.join(rail) for rail in rails)
        return cipher_text

    def rail_fence_decrypt(self, cipher_text, num_rails):
        # Bắt lỗi: Nếu key <= 1 hoặc chuỗi rỗng thì trả về nguyên bản
        if num_rails <= 1 or not cipher_text:
            return cipher_text

        # 1. Tính toán độ dài (số lượng ký tự) của từng đường ray
        rail_lengths = [0] * num_rails
        rail_index = 0
        direction = 1

        for _ in range(len(cipher_text)):
            rail_lengths[rail_index] += 1
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction

        # 2. Tách chuỗi cipher_text thành các phần tương ứng gán vào từng đường ray
        rails = []
        start = 0
        for length in rail_lengths:
            rails.append(cipher_text[start:start + length])
            start += length

        # 3. Ráp lại thành plain_text bằng cách đọc theo đường zigzag
        plain_text = ""
        rail_index = 0
        direction = 1

        for _ in range(len(cipher_text)):
            # Lấy ký tự đầu tiên của ray hiện tại
            plain_text += rails[rail_index][0]
            # Cắt bỏ ký tự vừa lấy ra khỏi ray
            rails[rail_index] = rails[rail_index][1:]

            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction

        return plain_text