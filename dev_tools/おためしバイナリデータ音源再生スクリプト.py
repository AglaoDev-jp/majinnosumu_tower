import os
import tempfile # 一時ファイルや一時ディレクトリを作成・操作する標準のモジュール
import pygame

def play_binary_audio(binary_path):
    # バイナリデータを読み込む
    with open(binary_path, "rb") as bin_file:
        binary_data = bin_file.read()

    # 一時ファイルとして音源を復元
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_file:
        temp_file.write(binary_data)
        temp_file_path = temp_file.name

    # Pygameで再生
    pygame.mixer.init()
    pygame.mixer.music.load(temp_file_path)
    pygame.mixer.music.play()

    # 再生終了まで待機
    while pygame.mixer.music.get_busy():
        pass

# スクリプトのディレクトリを基準にパスを修正
script_dir = os.path.dirname(os.path.abspath(__file__))
binary_audio_path = os.path.join(script_dir, "binary_audio", "音楽.bin") # お試しで聞きたい音楽のファイル名.bin
binary_sound_effect_path = os.path.join(script_dir, "binary_sound_effects", "効果音.bin") # お試しで聞きたいk効果音のファイル名.bin

# 再生例
play_binary_audio(binary_audio_path)
play_binary_audio(binary_sound_effect_path)

"""
使い方
1."binary_audio"フォルダと"binary_sound_effects"フォルダをこのスクリプトと同じディレクトリに置いてください。
2.お試しで聞きたい音楽のファイル名、効果音のファイル名をそれぞれコピペしてください(変換した音源にはファイル名に.mp3と残っていますが拡張子は.binです)
3.参照して起動してください。

"""