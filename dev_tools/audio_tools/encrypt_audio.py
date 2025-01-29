from cryptography.fernet import Fernet
import os
import sys

# 実行パスを取得（PyInstaller用の対応）
base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))

# 鍵をロード（鍵ファイルのパスを確実に指定）
key_path = os.path.join(base_path, "secret.key")
with open(key_path, "rb") as key_file:
    key = key_file.read()

cipher = Fernet(key)

# 暗号化するフォルダのパス
input_folder = os.path.join(base_path, "binary_audio")
output_folder = os.path.join(base_path, "encrypted_audio")

# 暗号化後のフォルダを作成
os.makedirs(output_folder, exist_ok=True)

# フォルダ内の全てのファイルを暗号化
for file_name in os.listdir(input_folder):
    input_path = os.path.join(input_folder, file_name)

    # ファイルを読み込んで暗号化
    with open(input_path, "rb") as f:
        file_data = f.read()
        encrypted_data = cipher.encrypt(file_data)

    # 暗号化されたデータを新しいフォルダに保存
    output_path = os.path.join(output_folder, file_name)
    with open(output_path, "wb") as f:
        f.write(encrypted_data)

print("全ての音源ファイルを暗号化しました！")
