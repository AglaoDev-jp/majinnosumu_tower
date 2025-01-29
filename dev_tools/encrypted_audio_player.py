from cryptography.fernet import Fernet
import os
import sys
import pygame

# 実行パスを取得（PyInstaller用の対応）
base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))

# 鍵をロード
key_path = os.path.join(base_path, "secret.key")
with open(key_path, "rb") as key_file:
    key = key_file.read()

cipher = Fernet(key)

# 暗号化されたフォルダと一時復号化フォルダのパス
encrypted_folder = os.path.join(base_path, "encrypted_audio")
decrypted_folder = os.path.join(base_path, "decrypted_audio")

# 復号化後のフォルダを作成
os.makedirs(decrypted_folder, exist_ok=True)

# 暗号化フォルダ内の全てのファイルを復号化
for file_name in os.listdir(encrypted_folder):
    input_path = os.path.join(encrypted_folder, file_name)

    # ファイルを読み込んで復号化
    with open(input_path, "rb") as f:
        encrypted_data = f.read()
        decrypted_data = cipher.decrypt(encrypted_data)

    # 復号化されたデータを一時フォルダに保存
    output_path = os.path.join(decrypted_folder, file_name)
    with open(output_path, "wb") as f:
        f.write(decrypted_data)

print("全ての音源ファイルを復号化しました！")

# 音源を再生
pygame.mixer.init()

# 再生するファイルを指定
sound_path = os.path.join(decrypted_folder, "再生したいファイル名.mp3.bin") # 再生したいファイル名に変更
pygame.mixer.music.load(sound_path)
pygame.mixer.music.play()

print("音源を再生中...")

# 再生終了まで待機
while pygame.mixer.music.get_busy():
    pass

print("再生が完了しました！")
"""
使い方
1."encrypted_audio"フォルダを、このスクリプトと同じディレクトリに置いてください。
2."音源のファイル名"部分を、視聴したいバイナリデータ名に変更してください。(変換した音源にはファイル名に.mp3と残っていますが拡張子は.binです)
3.参照して起動してください。
4."decrypted_audio"の音源は、複合化した一時ファイルです。視聴し終わったら**必ず削除**してください。

"""
