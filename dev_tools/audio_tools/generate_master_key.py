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

# スクリプトのあるディレクトリを取得
script_dir = os.path.dirname(os.path.abspath(__file__))

# マスターキーを生成
master_key = Fernet.generate_key()

# master_keyを使ってsecret.keyを暗号化
cipher_master = Fernet(master_key)

try:
    # 既存のsecret.keyをスクリプトと同じディレクトリから読み込み
    secret_key_path = os.path.join(script_dir, "secret.key")
    with open(secret_key_path, "rb") as key_file:
        secret_key = key_file.read()

    # デバッグ: secret_keyを正しく参照できているか確認
    print(f"[DEBUG] secret.key loaded successfully, size: {len(secret_key)} bytes")

    # secret.keyを暗号化
    encrypted_secret_key = cipher_master.encrypt(secret_key)

    # 暗号化されたsecret.keyをスクリプトと同じディレクトリに保存
    encrypted_key_path = os.path.join(script_dir, "encrypted_secret.key")
    with open(encrypted_key_path, "wb") as encrypted_file:
        encrypted_file.write(encrypted_secret_key)

    # デバッグ: 暗号化されたキーの保存場所を確認
    print(f"[DEBUG] Encrypted key saved to: {encrypted_key_path}")

    # マスターキーをキーファイルとして保存
    master_key_path = os.path.join(script_dir, "master.key")
    with open(master_key_path, "wb") as master_file:
        master_file.write(master_key)

    # デバッグ: マスターキーの保存場所を確認
    print(f"[DEBUG] Master key saved to: {master_key_path}")

except FileNotFoundError:
    print("[ERROR] secret.key not found in the script directory.")
except Exception as e:
    print(f"[ERROR] An error occurred: {e}")
