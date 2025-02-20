"""
作成者: AglaoDev-jp  
Copyright © 2024 AglaoDev-jp
ライセンス情報:
- コード: MIT License
This software is licensed under the MIT License. For details, see the LICENSE file.
"""
import json
import os

def extract_text(obj, extracted_text):
    """JSONオブジェクトから'text'キーの値を抽出"""
    if isinstance(obj, dict):
        for key, value in obj.items():
            if key == "text" and isinstance(value, str):
                extracted_text.append(value)
            else:
                extract_text(value, extracted_text)
    elif isinstance(obj, list):
        for item in obj:
            extract_text(item, extracted_text)

def process_json_files_in_directory(directory):
    """ディレクトリ内のJSONファイルを処理し、抽出したテキストを同名のテキストファイルに保存"""
    for file_name in os.listdir(directory):
        if file_name.endswith(".json"):
            json_file_path = os.path.join(directory, file_name)
            extracted_text = []

            try:
                with open(json_file_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    extract_text(data, extracted_text)

                # 出力ファイル名をJSONファイル名に合わせる（.json -> .txt）
                output_file_name = os.path.splitext(file_name)[0] + ".txt"
                output_file_path = os.path.join(directory, output_file_name)

                # 抽出したテキストを保存
                with open(output_file_path, "w", encoding="utf-8") as output_file:
                    output_file.write("\n".join(extracted_text))

                print(f"Extracted text saved to {output_file_name}")

            except Exception as e:
                print(f"Error processing file {file_name}: {e}")

if __name__ == "__main__":
    script_directory = os.path.dirname(os.path.abspath(__file__))
    process_json_files_in_directory(script_directory)
