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

# スクリプトが置かれているディレクトリを取得
current_dir = os.path.dirname(os.path.abspath(__file__))

# 鍵を生成
key = Fernet.generate_key() # Fernet.generate_key()は暗号学的に安全なランダム生成アルゴリズム

# スクリプトと同じディレクトリに鍵ファイルを保存
key_path = os.path.join(current_dir, "secret.key") # "secret.key"は、好きな名前に変更できます。
with open(key_path, "wb") as key_file:
    key_file.write(key)

print(f"暗号化用の鍵を生成しました！保存先: {key_path}") # 出力した場所も表示

"""
キーを暗号化した状態で設定ファイルに保存し、起動時に復号化する方法です。
このスクリプトはキーを暗号化して設定ファイルとして保存するものです。
スクリプトと同じディレクトリに鍵ファイルを作成するように改良を加えています。
cryptographyライブラリのFernet.generate_key()は、暗号化と復号化に必要な**ランダムなバイト列（鍵）**を生成します。
"""
