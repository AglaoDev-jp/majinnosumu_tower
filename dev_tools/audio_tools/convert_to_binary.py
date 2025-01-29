import os

# 音源ファイルをバイナリ形式に変換して保存する関数
def convert_to_binary(input_folder, output_folder):
    # 出力フォルダを作成（存在しない場合）
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # フォルダ内のファイルをすべて処理
    for file_name in os.listdir(input_folder):
        input_path = os.path.join(input_folder, file_name)
        
        # ファイルが音源の場合のみ処理
        if os.path.isfile(input_path) and file_name.endswith(('.mp3', '.wav', '.ogg')):
            with open(input_path, 'rb') as audio_file:
                binary_data = audio_file.read()
            
            # バイナリデータを出力フォルダに保存
            output_path = os.path.join(output_folder, f"{file_name}.bin")
            with open(output_path, 'wb') as bin_file:
                bin_file.write(binary_data)
            
            print(f"Converted: {file_name} -> {output_path}")

# 変換対象のフォルダ
audio_input_folder = "audio"  # 元の音源をフォルダ内に入れてください。

# スクリプトのディレクトリを取得
script_dir = os.path.dirname(os.path.abspath(__file__))

# 音源フォルダのパスを作成
audio_input_folder = os.path.join(script_dir, "audio")

# バイナリ保存先フォルダ
audio_output_folder = os.path.join(script_dir, "binary_audio") # "binary_audio"フォルダが作成され、その中にバイナリデータが作成されます。

# 実行
convert_to_binary(audio_input_folder, audio_output_folder)

