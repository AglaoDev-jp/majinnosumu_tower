"""
作成者: AglaoDev-jp  
Copyright © 2024 AglaoDev-jp
ライセンス情報:
- コード: MIT License
This software is licensed under the MIT License. For details, see the LICENSE file.
"""
import os
import json

def remove_voice_and_save():
    # スクリプトのあるディレクトリを取得
    current_dir = os.path.dirname(os.path.abspath(__file__))
    json_folder = os.path.join(current_dir, "scenario（一部音声ありver）")  # JSONファイルが入ったフォルダを想定
    output_folder = os.path.join(current_dir, "processed_json")  # 出力フォルダ

    # 出力フォルダがない場合は作成
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # JSONファイルを探す
    for file_name in os.listdir(json_folder):
        if file_name.endswith(".json"):
            file_path = os.path.join(json_folder, file_name)
            output_path = os.path.join(output_folder, file_name)

            # JSONファイルを読み込む
            with open(file_path, "r", encoding="utf-8") as file:
                data = json.load(file)

            # "voice"項目を削除
            for story in data.get("story", []):
                for segment in story.get("segments", []):
                    if "voice" in segment:
                        del segment["voice"]

            # 新しいJSONファイルとして保存
            with open(output_path, "w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=2)

            print(f"Processed: {file_name}")

if __name__ == "__main__":
    remove_voice_and_save()
