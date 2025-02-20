"""
作成者: AglaoDev-jp  
Copyright © 2024 AglaoDev-jp
ライセンス情報:
- コード: MIT License
This software is licensed under the MIT License. For details, see the LICENSE file.
"""
import secrets
import string

# ダミーコードを生成する関数
def generate_dummy_code(length):
    return ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(length))

# ""に、マスターキーを入力してください。
# 例として仮で作成したマスターキーを入力しています。
MASTER_KEY = b"9LaqVDBliny7OFGalegvU0n0yk0YGJr6sGRR1tLp4GI=" 

# MASTER_KEY を3つに分割
split_keys = [
    MASTER_KEY[:len(MASTER_KEY)//3],
    MASTER_KEY[len(MASTER_KEY)//3:2*len(MASTER_KEY)//3],
    MASTER_KEY[2*len(MASTER_KEY)//3:]
]

# 変数リスト
variables = [
    "KEYSTORE_UUID", "SECURE_HASH_ID", "APP_SECRET_TOKEN", "CRYPTIC_CODE", 
    "VAULT_ACCESS_KEY", "AUTHORIZATION_STRING", "MASTER_CIPHER", "ENCRYPTION_SEED", 
    "PRIVATE_ACCESS", "SESSION_SALT", "GLOBAL_SECRET_KEY", "ROOT_SECURITY_CODE", 
    "TOKEN_GENERATOR", "PRIMARY_HASH", "ACCESS_TOKEN_ID"
]

# 変数をランダムにシャッフル
secrets.SystemRandom().shuffle(variables)

# ダミーコードも含めたリストを作成
key_length = len(split_keys[0])
data_pool = split_keys + [generate_dummy_code(key_length).encode() for _ in range(len(variables) - len(split_keys))]
secrets.SystemRandom().shuffle(data_pool)

# 変数にランダムに値を代入
assigned_variables = {}
for var in variables:
    assigned_variables[var] = data_pool.pop()

# 結果の出力
print("\n# 難読化されたコード:")
for var, value in assigned_variables.items():
    print(f"{var} = {value}")

# 正しい順番で復元するためのキーリスト
reconstruction_keys = []
for part in split_keys:
    for key, value in assigned_variables.items():
        if value == part:
            reconstruction_keys.append(key)
            break

# MASTER_KEY に正しい順番で代入するコードを出力
reconstruction_code = " + ".join(reconstruction_keys)
print("\n# 復元コード:")
print(f"MASTER_KEY = {reconstruction_code}")
