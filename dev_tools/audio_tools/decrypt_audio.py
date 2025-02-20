"""
作成者: AglaoDev-jp  
Copyright © 2024 AglaoDev-jp

ライセンス情報:
- コード: MIT License
This software is licensed under the MIT License. For details, see the LICENSE file.

External Libraries:

- cryptography:  
  Copyright © 2013-2024 The cryptography developers  
  Licensed under the Apache License, Version 2.0 or the BSD 3-Clause License.  
  For full details, see LICENSE-cryptography.txt or visit:  
  [Cryptography License](https://github.com/pyca/cryptography/blob/main/LICENSE)

  This software includes cryptographic components from OpenSSL 3.4.0 (22 Oct 2024), distributed under the Apache License 2.0.  
  For details, see LICENSE-OpenSSL.txt or [OpenSSL License](https://www.openssl.org/source/license.html).  
  Copyright (c) 1998-2024 The OpenSSL Project Authors  
  Copyright (c) 1995-1998 Eric A. Young, Tim J. Hudson  
  All rights reserved.
  
"""
from cryptography.fernet import Fernet
import os
import sys

# 実行パスを取得（PyInstaller用の対応）
base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))

# 鍵をロード
key_path = os.path.join(base_path, "secret.key")
with open(key_path, "rb") as key_file:
    key = key_file.read()

cipher = Fernet(key)

# 暗号化フォルダと復号化フォルダのパス
input_folder = os.path.join(base_path, "encrypted_audio")
output_folder = os.path.join(base_path, "decrypted_audio")

# 復号化後のフォルダを作成
os.makedirs(output_folder, exist_ok=True)

# フォルダ内の全てのファイルを復号化
for file_name in os.listdir(input_folder):
    input_path = os.path.join(input_folder, file_name)

    # ファイルを読み込んで復号化
    with open(input_path, "rb") as f:
        encrypted_data = f.read()
        decrypted_data = cipher.decrypt(encrypted_data)

    # 復号化されたデータを新しいフォルダに保存
    output_path = os.path.join(output_folder, file_name) 
    with open(output_path, "wb") as f: f.write(decrypted_data)

print("全ての音源ファイルを復号化しました！")
