from flask import Flask, render_template, request
# Import thuật toán Rail Fence thay vì Caesar
from cipher.railfence.railfence_cipher import RailFenceCipher

app = Flask(__name__)

# Router cho trang chủ
@app.route("/")
def home():
    return render_template('index.html')

# Router cho trang giao diện Rail Fence
@app.route("/railfence")
def railfence():
    return render_template('railfence.html')

# Router xử lý logic Mã hóa
@app.route("/railfence_encrypt", methods=['POST'])
def railfence_encrypt_route():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    
    cipher = RailFenceCipher()
    encrypted_text = cipher.rail_fence_encrypt(text, key)
    
    # Gọi lại trang html và truyền kết quả cùng dữ liệu cũ sang
    return render_template('railfence.html', 
                           encrypted_result=encrypted_text,
                           plain_text_old=text,
                           key_plain_old=key)

# Router xử lý logic Giải mã
@app.route("/railfence_decrypt", methods=['POST'])
def railfence_decrypt_route():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    
    cipher = RailFenceCipher()
    decrypted_text = cipher.rail_fence_decrypt(text, key)
    
    # Gọi lại trang html và truyền kết quả cùng dữ liệu cũ sang
    return render_template('railfence.html', 
                           decrypted_result=decrypted_text,
                           cipher_text_old=text,
                           key_cipher_old=key)
# Chạy server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)