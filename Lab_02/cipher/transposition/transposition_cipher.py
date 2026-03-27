import math

class TranspositionCipher:
    def __init__(self):
        pass

    def encrypt(self, text, key):
        # Bắt lỗi an toàn
        if key <= 1 or not text:
            return text
            
        encrypted_text = ""
        for col in range(key):
            pointer = col
            while pointer < len(text):
                encrypted_text += text[pointer]
                pointer += key
                
        return encrypted_text

    def decrypt(self, text, key):
        # Bắt lỗi an toàn
        if key <= 1 or not text:
            return text

        # Tính toán lưới ma trận chuẩn xác
        num_cols = math.ceil(len(text) / key)
        num_rows = key
        # Số ô bị dư ra (mờ đi) ở cột cuối cùng
        num_shaded_boxes = (num_cols * num_rows) - len(text)

        decrypted_text = [''] * num_cols
        col = 0
        row = 0

        for symbol in text:
            decrypted_text[col] += symbol
            col += 1
            
            # Logic mới: Nếu chạy hết số cột, hoặc đang ở cột cuối cùng mà chạm đến ô "mờ"
            if (col == num_cols) or (col == num_cols - 1 and row >= num_rows - num_shaded_boxes):
                col = 0
                row += 1

        return ''.join(decrypted_text)