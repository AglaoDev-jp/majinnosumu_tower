"""
作成者: AglaoDev-jp  
Copyright © 2024 AglaoDev-jp
ライセンス情報:
- コード: MIT License
This software is licensed under the MIT License. For details, see the LICENSE file.
"""
import os

input_folder = "置換フォルダ"  # スクリプトと同じディレクトリ内にフォルダをいれてフォルダ名を指定してください

# 置換前後の文字列
old_text = "置換する部分" # 変更する部分の文字を""内に記入
new_text = "この文字に置換したい" # 変更したい文字を""内に記入

# スクリプトの現在のディレクトリを取得
script_dir = os.path.dirname(os.path.abspath(__file__))

# フォルダパスを作成
folder_path = os.path.join(script_dir, input_folder)

# フォルダが存在するか確認
if not os.path.exists(folder_path):
    print(f"指定されたフォルダ '{input_folder}' が見つかりません。スクリプトと同じディレクトリにフォルダがあることを確認してください。")
else:
    # フォルダ内のファイルを順に処理
    for filename in os.listdir(folder_path):
        # 置換対象の文字列がファイル名に含まれているか確認
        if old_text in filename:
            # 新しいファイル名を作成
            new_filename = filename.replace(old_text, new_text)
            
            # フルパスを作成
            old_file_path = os.path.join(folder_path, filename)
            new_file_path = os.path.join(folder_path, new_filename)
            
            # ファイル名を変更
            os.rename(old_file_path, new_file_path)
            print(f"Renamed: {filename} -> {new_filename}")

    print("ファイル名の置換が完了しました。")
