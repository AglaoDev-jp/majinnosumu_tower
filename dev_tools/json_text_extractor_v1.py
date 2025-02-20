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
    extracted_text = []
    output_file = os.path.join(directory, "extracted_text.txt")

    for file_name in os.listdir(directory):
        if file_name.endswith(".json"):
            json_file_path = os.path.join(directory, file_name)
            try:
                with open(json_file_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    extract_text(data, extracted_text)
            except Exception as e:
                print(f"Error processing file {file_name}: {e}")

    with open(output_file, "w", encoding="utf-8") as output:
        output.write("\n".join(extracted_text))

    print(f"Text extracted and saved to {output_file}")

if __name__ == "__main__":
    script_directory = os.path.dirname(os.path.abspath(__file__))
    process_json_files_in_directory(script_directory)
