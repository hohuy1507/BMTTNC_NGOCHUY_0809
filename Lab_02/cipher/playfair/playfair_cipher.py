class PlayFairCipher:
    def __init__(self):
        pass

    def create_matrix_key(self, key):
        key = key.upper().replace("J", "I")
        key = "".join(dict.fromkeys(key))

        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        matrix = list(key)

        for letter in alphabet:
            if letter not in matrix:
                matrix.append(letter)

        playfair_matrix = [matrix[i:i+5] for i in range(0, 25, 5)]
        return playfair_matrix

    def tachchuoi_plaintext(self, text):
        text = text.upper().replace("J", "I").replace(" ", "")
        pairs = []
        i = 0

        while i < len(text):
            a = text[i]
            if i + 1 < len(text):
                b = text[i+1]
                if a == b:
                    pairs.append(a + "X")
                    i += 1
                else:
                    pairs.append(a + b)
                    i += 2
            else:
                pairs.append(a + "X")
                i += 1
        return pairs

    def vitri_plaintext(self, letter, matrix):
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == letter:
                    return row, col

    def playfair_en(self, plain_text, matrix):
        pairs = self.tachchuoi_plaintext(plain_text) # Đã sửa tên hàm
        encrypted_text = ""

        for pair in pairs:
            # Đã sửa tên hàm và thứ tự truyền tham số
            row1, col1 = self.vitri_plaintext(pair[0], matrix)
            row2, col2 = self.vitri_plaintext(pair[1], matrix)

            if row1 == row2:
                encrypted_text += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
            elif col1 == col2:
                encrypted_text += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
            else:
                encrypted_text += matrix[row1][col2] + matrix[row2][col1]
        return encrypted_text

    def playfair_de(self, cipher_text, matrix):
        cipher_text = cipher_text.upper()
        decrypted_text = ""

        for i in range(0, len(cipher_text), 2):
            pair = cipher_text[i:i+2]
            # Đã sửa tên hàm và thứ tự truyền tham số
            row1, col1 = self.vitri_plaintext(pair[0], matrix)
            row2, col2 = self.vitri_plaintext(pair[1], matrix)

            if row1 == row2:
                decrypted_text += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
            elif col1 == col2:
                decrypted_text += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
            else:
                decrypted_text += matrix[row1][col2] + matrix[row2][col1]

        banro = ""
        # Loại bỏ ký tự 'X' nếu nó là ký tự cuối cùng và là ký tự được thêm vào
        for i in range(0, len(decrypted_text)-2, 2):
            if decrypted_text[i] == decrypted_text[i+2]:banro += decrypted_text[i]
            else:
                banro += decrypted_text[i] + "" + decrypted_text[i+1]

        if decrypted_text[-1] == "X":
            banro += decrypted_text[-2]
        else:
            banro += decrypted_text[-2]
            banro += decrypted_text[-1]

        return banro