"""
作成者: AglaoDev-jp  
Copyright © 2024 AglaoDev-jp

ライセンス情報:
- コード: MIT License
- 画像: CC BY 4.0
- シナリオ: CC BY-SA 4.0

This software is licensed under the MIT License. For details, see the LICENSE file.

Images created by AglaoDev-jp are licensed under CC BY 4.0.  
Scenarios written by AglaoDev-jp are licensed under CC BY-SA 4.0.

External Libraries:

- Tkinter:  
  Copyright © Regents of the University of California, Sun Microsystems, Inc., Scriptics Corporation, and other parties  
  Licensed under the Tcl/Tk License. For full details, see:  
  [Tcl/Tk License](https://www.tcl.tk/software/tcltk/license.html)

- Pillow (a friendly fork of the Python Imaging Library, PIL):  
  The Python Imaging Library (PIL) is  
  Copyright © 1997-2011 by Secret Labs AB  
  Copyright © 1995-2011 Fredrik Lundh and Contributors.  
  Pillow is the friendly PIL fork. It is  
  Copyright © 2010-2024 by Jeffrey A. Clark and contributors  
  Licensed under the MIT-CMU License. See LICENSE-Pillow.txt or visit:  
  [Pillow License](https://pillow.readthedocs.io/en/stable/about.html#license)

- pygame:  
  Copyright © 2000-2024 Pygame developers  
  Licensed under the LGPL License. See LICENSE-pygame.txt or visit:  
  [Pygame License](https://www.pygame.org/docs/license.html)

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

- Noto Sans JP:  
  Copyright © 2014-2024 Google LLC  
  Licensed under the SIL Open Font License, Version 1.1 
    
A heartfelt thanks to all developers and contributors who have made these libraries possible.

"""

import json
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import pygame
import sys
import os
from io import BytesIO
from cryptography.fernet import Fernet

# セーブディレクトリを実行ファイルの存在するフォルダに変更
def get_save_directory():
    if getattr(sys, 'frozen', False):
        save_dir = os.path.join(os.path.dirname(sys.executable), "saves")
    else:
        save_dir = os.path.join(os.path.dirname(__file__), "saves")
    os.makedirs(save_dir, exist_ok=True)
    return save_dir

SAVE_DIR = get_save_directory()

# デバッグ用の確認
print(f"Save directory: {SAVE_DIR}")

# PyInstaller環境か通常実行かを判断して base_path を設定
if getattr(sys, 'frozen', False):
    base_path = sys._MEIPASS
else:
    base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# デバッグ用の確認
print(f"Base path: {base_path}")

# 難読化されたコード:`key_obfuscator.py`で作成したコードをペーストしてください。
AUTHORIZATION_STRING = b'jpBc2EYA3oXDzI'
GLOBAL_SECRET_KEY = b'rEtY4T1h8LtwwG'
ROOT_SECURITY_CODE = b'Dmg319Q0GwnFWq'
KEYSTORE_UUID = b'pMqkkF0CsVsdBF'
PRIMARY_HASH = b'8JXGXR8HznFChS'
APP_SECRET_TOKEN = b'ZBqGzxiUiGOfn7'
MASTER_CIPHER = b'9LaqVDBliny7OF'
SESSION_SALT = b'uJwuAKdRRQpyhf'
ENCRYPTION_SEED = b'rvEfxbIi69kJKi'
VAULT_ACCESS_KEY = b'WAg0HWHkct0DxE'
CRYPTIC_CODE = b'gVLsiq0DTGa4m0'
PRIVATE_ACCESS = b'Jr6sGRR1tLp4GI='
SECURE_HASH_ID = b'GalegvU0n0yk0YG'
TOKEN_GENERATOR = b'StULaF7l2G6aaz'
ACCESS_TOKEN_ID = b'h6mITGS3gxnT8x'

# 復元コード:`key_obfuscator.py`で作成したコードをペーストしてください。
MASTER_KEY = MASTER_CIPHER + SECURE_HASH_ID + PRIVATE_ACCESS

# master_keyを使用してFernetオブジェクトを作成
cipher_master = Fernet(MASTER_KEY)

try:
    # スクリプトのあるディレクトリを取得
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # 既存のencrypted_secret.keyをスクリプトと同じディレクトリから読み込み
    encrypted_key_path = os.path.join(script_dir, "encrypted_secret.key")
    with open(encrypted_key_path, "rb") as encrypted_file:
        encrypted_secret_key = encrypted_file.read()

    # encrypted_secret.keyを復号化
    secret_key = cipher_master.decrypt(encrypted_secret_key)

    # デバッグ: 復号化されたsecret.keyのサイズ確認
    print(f"[DEBUG] Decrypted secret.key size: {len(secret_key)} bytes")

    # secret.keyを利用した暗号化/復号化処理の準備
    cipher = Fernet(secret_key)

    # デバッグ: 暗号化機能が正常に動作しているか確認
    print("[DEBUG] Cipher object successfully created with secret.key")

except FileNotFoundError:
    print("[ERROR] encrypted_secret.key not found in the script directory.")
    sys.exit(1)  # ファイルがない場合は終了
except Exception as e:
    print(f"[ERROR] An error occurred: {e}")
    sys.exit(1)  # その他のエラーでも終了

# リソースパスを取得する関数
def get_resource_path(*path_segments):
    path = os.path.join(base_path, *path_segments)
    # デバッグ: パスセグメントと組み立てられたパスを表示
    print(f"[DEBUG] get_resource_path called with path_segments: {path_segments}")
    print(f"[DEBUG] Constructed resource path: {path}")
    return os.path.join(base_path, *path_segments)

# リソースデータを取得する関数（バイナリデータを読み込む）
def get_resource_data(*path_segments):
    path = get_resource_path(*path_segments)
    print(f"[DEBUG] get_resource_data called with path_segments: {path_segments}")
    print(f"[DEBUG] Resolved path: {path}")

    try:
        with open(path, 'rb') as f:
            data = f.read()

        # ファイルが暗号化されているかどうかをチェック
        if path.endswith('.bin'):
            print(f"[DEBUG] Encrypted data size: {len(data)} bytes")
            # データを復号化
            decrypted_data = cipher.decrypt(data)
            print(f"[DEBUG] Decrypted data size: {len(decrypted_data)} bytes")
            # オプション: 復号化データの先頭数バイトを表示
            print(f"[DEBUG] Decrypted data preview: {decrypted_data[:10]}")
            return decrypted_data
        else:
            return data
    except Exception as e:
        print(f"Error loading resource: {e}")
        return None

RESOURCE_KEYS = ["bg_change", "music", "sound_effect", "voice", "choice_file"]

def convert_paths(data, to_absolute=True):
    for page in data["story"]:
        for flag in page.get("flags", []):
            for key in RESOURCE_KEYS:
                if key in flag:
                    flag[key] = (
                        get_resource_path(flag[key]) if to_absolute else os.path.relpath(flag[key], base_path)
                    )
        for segment in page["segments"]:
            for key in RESOURCE_KEYS:
                if key in segment:
                    segment[key] = (
                        get_resource_path(segment[key]) if to_absolute else os.path.relpath(segment[key], base_path)
                    )
            if "choices" in segment:
                for choice in segment["choices"]:
                    if "choice_file" in choice:
                        choice["choice_file"] = (
                            get_resource_path(choice["choice_file"]) if to_absolute else os.path.relpath(choice["choice_file"], base_path)
                        )

def load_json(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: File not found: {file_path}")
        return None
    except json.JSONDecodeError as e:
        print(f"Error: Failed to parse JSON in file {file_path}: {e}")
        return None

# JSON ファイルのパス定義
story_json_file = get_resource_path('assets', 'scenario',  'C_07_monster_bird.json')
credits_json_file = get_resource_path('assets', 'scenario', 'staff_credits_ver.4.json')

# ストーリーとクレジットのデータを読み込む
story_data = load_json(story_json_file)
if story_data and "story" in story_data:
    convert_paths(story_data, to_absolute=True)

credits_data = load_json(credits_json_file)
if credits_data:
    print("Credits data loaded successfully.")

# デバッグ用記述
print(f"Story JSON path: {story_json_file}")
print(f"Credits JSON path: {credits_json_file}")

try:
    pygame.init()
    pygame.mixer.init()
except pygame.error as e:
    print(f"Audio initialization failed: {e}")
    pygame.mixer = None

# 現在のディレクトリを取得
current_dir = base_path

def get_font_path(file_name):
    return get_resource_path('assets', 'fonts', file_name)

# フォントパスの設定
noto_sans_regular = get_font_path('NotoSansJP-Regular.otf')
noto_sans_bold = get_font_path('NotoSansJP-Bold.otf')
noto_sans_black = get_font_path('NotoSansJP-Black.otf')

current_music = None
current_sfx = None
music_channel = None  # 音楽チャンネルを追加

# Tkinterのウィンドウ設定
root = tk.Tk()
root.title("魔人の棲む塔")
root.geometry("1200x600")

# アイコンファイルのパスを取得
icon_path = (
    os.path.join(sys._MEIPASS, "demon_tower.png") if getattr(sys, "_MEIPASS", False)
    else os.path.join(base_path, "assets", "images", "demon_tower.png")
)
# デバッグ: パスを確認
print(f"[DEBUG] Icon path: {icon_path}")
# アイコンを設定
try:
    icon = tk.PhotoImage(file=icon_path)
    root.iconphoto(True, icon)
except Exception as e:
    print(f"Error setting icon: {e}")

# 文字のタイピング速度（ミリ秒）
typing_speed = 50

# フルスクリーンの状態を管理
is_fullscreen = False

# フルスクリーンをトグルする関数
def toggle_fullscreen(event=None):
    global is_fullscreen
    is_fullscreen = not is_fullscreen
    root.attributes("-fullscreen", is_fullscreen)
    adjust_positions()

# フルスクリーンを終了する関数
def end_fullscreen(event=None):
    global is_fullscreen
    is_fullscreen = False
    root.attributes("-fullscreen", False)
    adjust_positions()

# F11でフルスクリーンのトグル、Escキーでフルスクリーンを終了
root.bind("<F11>", toggle_fullscreen)
root.bind("<Escape>", end_fullscreen)

# 画面の要素の位置を調整する関数
def adjust_positions():
    canvas_width = root.winfo_width()
    canvas_height = root.winfo_height()
    # 背景画像を変更する（もし設定されている場合）
    if hasattr(canvas, 'image_path') and canvas.image_path:
        change_background(canvas.image_path)
    # テキストと選択肢の表示位置を調整
    line_height = 30

    for i, item in enumerate(text_items):
        canvas.coords(item, 20, 20 + i * line_height)

    for i, item in enumerate(choice_items):
        canvas.coords(item, 20, 100 + i * line_height)
    # オープニング画面のアイテムの位置を調整
    for item in opening_items:
        x, y = canvas.coords(item)[:2]
        if "魔人の棲む塔" in canvas.itemcget(item, "text"):
            canvas.coords(item, canvas_width // 2, canvas_height // 5)
        else:
            canvas.coords(item, canvas_width // 2, y)

# キャンバスを設定
canvas = tk.Canvas(root, width=1200, height=600, bg="black")
canvas.pack(fill="both", expand=True)

# ストーリーのページとセグメントの管理
current_page = 0
current_segment = 0

# テキスト、選択肢、オープニング画面アイテムを管理するリスト
text_items = []
choice_items = []
opening_items = []

# 選択肢の待機状態、テキストのタイピングが進行中かどうかを管理
waiting_for_choice = False
typing_in_progress = False

# 背景画像を変更する関数
def change_background(image_file):
    # デバッグ：ファイル名を表示
    print(f"[DEBUG] change_background called with image_file: {image_file}")

    # フルパスを組み立てる
    image_path = get_resource_path('assets', 'images', image_file)
    print(f"[DEBUG] Full path to background image: {image_path}")

    try:
        canvas_width = root.winfo_width()
        canvas_height = root.winfo_height()

        img = Image.open(image_path)  # PILで画像を開く
        img = img.resize((canvas_width, canvas_height), Image.Resampling.LANCZOS)
        bg_image = ImageTk.PhotoImage(img)

        canvas.delete("background")
        canvas.create_image(0, 0, anchor="nw", image=bg_image, tags="background")
        canvas.image = bg_image
        canvas.image_path = image_path
        canvas.tag_lower("background")
    except FileNotFoundError:
        print(f"[ERROR] File not found at: {image_path}")
        messagebox.showerror("File Not Found", f"The file '{image_path}' could not be found.")


# オープニング画面を表示する関数
def show_opening_screen():
    enable_right_click()

    global opening_items
    clear_text()
    clear_choices()

    demon_tower_image_path = get_resource_path('assets', 'images', 'demon_tower.png')
    root.after(100, lambda: change_background(demon_tower_image_path))

    # タイトル表示
    title_item = canvas.create_text(600, 100, text="魔人の棲む塔", font=(noto_sans_bold, 100), fill="red")
    opening_items.append(title_item)

    # ゲームスタートボタン
    start_game_item = canvas.create_text(600, 400, text="ゲームスタート", font=(noto_sans_bold, 24), fill="white")
    opening_items.append(start_game_item)
    canvas.tag_bind(start_game_item, "<Button-1>", lambda e: start_game())
    canvas.tag_bind(start_game_item, "<Enter>", lambda e: canvas.itemconfig(start_game_item, fill="yellow"))
    canvas.tag_bind(start_game_item, "<Leave>", lambda e: canvas.itemconfig(start_game_item, fill="white"))

    # 説明ボタン
    explanation_item = canvas.create_text(600, 450, text="説明", font=(noto_sans_bold, 24), fill="white")
    opening_items.append(explanation_item)
    canvas.tag_bind(explanation_item, "<Button-1>", lambda e: show_explanation())
    canvas.tag_bind(explanation_item, "<Enter>", lambda e: canvas.itemconfig(explanation_item, fill="yellow"))
    canvas.tag_bind(explanation_item, "<Leave>", lambda e: canvas.itemconfig(explanation_item, fill="white"))

    root.unbind("<Button-1>")
    root.after(100, adjust_positions)



# ストーリーの開始処理
def start_game():
    global current_page, current_segment, opening_items, story_data, text_items, choice_items, waiting_for_choice, typing_in_progress

    current_page = 0
    current_segment = 0
    waiting_for_choice = False
    typing_in_progress = False

    clear_text()
    clear_choices()
    
    # オープニングの要素を削除
    for item in opening_items:
        canvas.delete(item)
    opening_items.clear()
    
    # ストーリーデータを再度読み込み
    story_data = load_json(story_json_file)
    if not story_data:
        return
    convert_paths(story_data, to_absolute=True)

    root.bind("<Button-1>", next_segment)
    next_segment()

# 説明画面を表示する関数
def show_explanation():
    messagebox.showinfo("説明", "左クリック：文字読み、選択肢。\n右クリック：セーブロード、文字速度、音量調整\nF11 でフルスクリーン(Esc or F11で解除)\nB で暗くする(文字が読みにくいときにどうぞ)")


def show_navigation_image(canvas, last_text_item, image_path, size, tags, blink_function):
    if last_text_item:
        bbox = canvas.bbox(last_text_item)
        x, y = bbox[2] + 10, bbox[3] - 10
    else:
        x, y = 1150, 500

    img = ImageTk.PhotoImage(Image.open(image_path).resize(size))
    image_id = canvas.create_image(x, y, image=img, tags=tags)
    canvas.image_refs = getattr(canvas, 'image_refs', [])
    canvas.image_refs.append(img)  # 参照を保持してガベージコレクションを防ぐ
    blink_function(canvas, image_id)
    return image_id

def blink_image(canvas, image_id, visible=True):
    if canvas.find_withtag(image_id):
        canvas.itemconfigure(image_id, state="normal" if visible else "hidden")
        root.after(500, blink_image, canvas, image_id, not visible)

def type_text(canvas, item_id, text, index=0, auto_advance=False, arrow_icon=None, has_choices=False):
    """ テキストを1行ずつ表示し、必要に応じて矢印を変更する関数 """
    global typing_in_progress, waiting_for_choice
    
    if index == 0:
        hide_navigation_images(canvas)  # ナビゲーション画像をリセット
        if not has_choices:  # choicesがない場合のみflagsを処理
            handle_flags(story_data["story"][current_page]["segments"][current_segment].get("flags", []))

    typing_in_progress = True

    if index < len(text):
        canvas.itemconfig(item_id, text=text[:index + 1])
        root.after(typing_speed, type_text, canvas, item_id, text, index + 1, auto_advance, arrow_icon, has_choices)
    else:
        typing_in_progress = False

        if not auto_advance and not waiting_for_choice and not has_choices:
            # 矢印アイコンを表示（choicesがない場合のみ表示）
            navigation_icon = arrow_icon or "arrow.png"  # デフォルト矢印
            arrow_path = get_resource_path('assets', 'images', navigation_icon)
            if os.path.exists(arrow_path):
                show_navigation_image(
                    canvas, item_id,
                    arrow_path,
                    (30, 30),
                    "navigation",
                    blink_image
                )
        if auto_advance and not waiting_for_choice:
            root.after(500, next_segment)

# 次のストーリーセグメントを表示する関数
def next_segment(event=None):
    global current_page, current_segment, text_items, choice_items, waiting_for_choice
    if typing_in_progress or waiting_for_choice:
        return

    if current_page < len(story_data["story"]):
        page = story_data["story"][current_page]

        # ページ単位のフラグ処理
        handle_flags(page.get("flags", []))

        if current_segment < len(page["segments"]):
            segment = page["segments"][current_segment]

            # テキストが存在する場合（テキスト描画部分）
            if "text" in segment:
                arrow_icon = segment.get("arrow_icon", None)
                auto_advance = segment.get("auto_advance", False)
                color = segment.get("color", "white")
                font_size = segment.get("font_size", 20)
                line_height = font_size + 10

                text_item = canvas.create_text(
                    20,
                    20 + line_height * len(text_items),
                    anchor="nw",
                    text="",
                    font=(noto_sans_regular, font_size),
                    fill=color,
                    tags="text"
                )
                text_items.append(text_item)

                # テキスト表示
                type_text(
                    canvas, 
                    text_item, 
                    segment["text"], 
                    auto_advance=auto_advance, 
                    arrow_icon=arrow_icon
                )

            # まずフラグを処理してから（音楽・背景変更も含む）
            handle_flags(segment.get("flags", []))

            # 音楽・効果音・ボイス・背景変更などをここで処理
            if "music" in segment:
                play_music(os.path.basename(segment["music"]))
            if "sound_effect" in segment:
                play_sound_effect(os.path.basename(segment["sound_effect"]))
            if "voice" in segment:
                play_voice(os.path.basename(segment["voice"]))
            if "bg_change" in segment:
                change_background(os.path.basename(segment["bg_change"]))

            # 選択肢の表示は最後に判定
            if "choices" in segment:
                waiting_for_choice = True
                root.after(500, show_choices)
                return

            current_segment += 1
        else:
            # 次のページへ
            current_segment = 0
            current_page += 1
            clear_text()
            next_segment()
    else:
        # ストーリー終了時
        hide_navigation_images(canvas) # 画面にあるものを確実に消す
        root.after(1000, show_opening_screen)


# 選択肢を表示する関数
def show_choices():
    global choice_items
    if current_page < len(story_data["story"]):
        page = story_data["story"][current_page]
        if current_segment < len(page["segments"]):
            segment = page["segments"][current_segment]
            if "choices" in segment:
                create_choice_texts(segment)

# フェードインで選択肢を表示する関数
def fade_in_choice_text(canvas, item_id, step=0):
    # アルファ値を計算（0～255の範囲をstepに応じて設定）
    alpha = min(step * 25, 255)  # フェード速度はここで調整
    color = f"#{alpha:02x}{alpha:02x}{alpha:02x}"  # 白に向かってフェードイン

    canvas.itemconfig(item_id, fill=color)

    if alpha < 255:  # 最大値に達していない場合、次のステップをスケジュール
        root.after(50, fade_in_choice_text, canvas, item_id, step + 1)

# 選択肢テキストを作成する関数
def create_choice_texts(segment):
    global choice_items
    clear_choices()
    choice_start_y = 20 + 30 * len(text_items)
    for i, choice in enumerate(segment["choices"]):
        # テキストアイテムを作成  
        choice_item = canvas.create_text(
            20,
            choice_start_y + 30 * i,
            anchor="nw",
            text=choice['text'],
            font=(noto_sans_bold, 20),
            fill="#000000",  # 初期状態は黒
            tags=("choice",)
        )
        choice_items.append(choice_item)

        # フェードイン開始
        root.after(i * 100, fade_in_choice_text, canvas, choice_item, 0)  # 選択肢ごとに少し遅らせる

        # 選択肢のマウスイベントを設定
        canvas.tag_bind(choice_item, "<Enter>", lambda e, item=choice_item: canvas.itemconfig(item, fill="lightgray"))
        canvas.tag_bind(choice_item, "<Leave>", lambda e, item=choice_item: canvas.itemconfig(item, fill="white"))
        canvas.tag_bind(choice_item, "<Button-1>", lambda e, c=choice: select_choice(c))

# 選択肢が選ばれた際に呼び出される関数
def select_choice(choice):
    global waiting_for_choice
    waiting_for_choice = False
    choice_file = os.path.basename(choice["choice_file"])
    print(f"[DEBUG] select_choice called with choice_file: {choice_file}")
    load_choice(choice_file)

# 選択肢に基づいて新しいシナリオをロードする関数
def load_choice(choice_file):
    global story_data, current_page, current_segment, text_items, choice_items

    choice_file_path = get_resource_path('assets', 'scenario', choice_file)
    print(f"[DEBUG] Full path to choice file: {choice_file_path}")

    story_data = load_json(choice_file_path)
    if not story_data:
        print(f"[ERROR] Failed to load choice file: {choice_file_path}")
        return
    convert_paths(story_data, to_absolute=True)

    current_page = 0
    current_segment = 0
    clear_text()
    clear_choices()
    next_segment()

# テキストをクリアする関数
def clear_text():
    global text_items
    for item in text_items:
        canvas.delete(item)
    text_items = []

# 選択肢をクリアする関数
def clear_choices():
    global choice_items
    for item in choice_items:
        canvas.delete(item)
    choice_items = []

# ナビゲーション画像を削除する
def hide_navigation_images(canvas):
    canvas.delete("navigation")

# クリックイベント処理
def on_click(event):
    # 現在のナビゲーション画像を削除
    hide_navigation_images(canvas)

# 音楽を再生する関数（バイナリデータを使用）
def play_music(music_file, loops=-1):
    global current_music, music_volume, music_channel

    # デバッグ: music_file の値を表示
    print(f"[DEBUG] play_music called with music_file: {music_file}")

    # music_file のパスを組み立てる
    music_file_path = get_resource_path('assets', 'encrypted_audio', music_file)

    # デバッグ: 組み立てたパスを表示
    print(f"[DEBUG] Full path to music file: {music_file_path}")

    # 現在の曲と比較（ファイル名のみで比較）
    if current_music == music_file:
        print("[DEBUG] Same music is already playing. Skipping re-play.")
        return  # 同じ音楽が既に再生中の場合はスキップ

    # バイナリデータを取得
    music_data = get_resource_data('assets', 'encrypted_audio', music_file)

    if music_data is None:
        print(f"Error: Music data not found for '{music_file}'")
        return

    try:
        # バイナリデータからSoundオブジェクトを作成
        music_sound = pygame.mixer.Sound(file=BytesIO(music_data))
        # 音楽チャンネルを取得（チャンネル0を音楽用に予約）
        music_channel = pygame.mixer.Channel(0)
        # 音楽を再生
        music_channel.play(music_sound, loops=loops)
        # 音量を設定
        music_channel.set_volume(music_volume)
        current_music = music_file  # ファイル名のみを保存
    except pygame.error as e:
        print(f"Error playing music: {e}")

# 効果音とボイスのチャンネルを作成
sfx_channel = pygame.mixer.Channel(1)
voice_channel = pygame.mixer.Channel(2)

def play_sound_effect(sfx_file):
    # デバッグ：ファイル名を表示
    print(f"[DEBUG] play_sound_effect called with sfx_file: {sfx_file}")

    # フルパスを組み立てる
    sfx_file_path = get_resource_path('assets', 'encrypted_audio', sfx_file)
    print(f"[DEBUG] Full path to sound effect file: {sfx_file_path}")

    # バイナリデータを取得
    sfx_data = get_resource_data('assets', 'encrypted_audio', sfx_file)
    if sfx_data is None:
        print(f"Error: Sound effect data not found for '{sfx_file}'")
        return
    
    try:
        sfx = pygame.mixer.Sound(file=BytesIO(sfx_data))
        sfx.set_volume(sfx_volume)
        sfx_channel.play(sfx)
    except pygame.error as e:
        print(f"Error playing sound effect: {e}")

def play_voice(voice_file):
    # デバッグ：ファイル名を表示
    print(f"[DEBUG] play_voice called with voice_file: {voice_file}")

    # フルパスを組み立てる
    voice_file_path = get_resource_path('assets', 'voice', voice_file)
    print(f"[DEBUG] Full path to voice file: {voice_file_path}")

    # バイナリデータを取得
    voice_data = get_resource_data('assets', 'voice', voice_file)
    if voice_data is None:
        print(f"Error: Voice data not found for '{voice_file}'")
        return
    
    try:
        voice = pygame.mixer.Sound(file=BytesIO(voice_data))
        voice.set_volume(voice_volume)
        voice_channel.play(voice)
    except pygame.error as e:
        print(f"Error playing voice: {e}")

# ボリューム調整関数
def update_sfx_volume(val):
    global sfx_volume
    sfx_volume = float(val)
    sfx_channel.set_volume(sfx_volume)

def update_voice_volume(val):
    global voice_volume
    voice_volume = float(val)
    voice_channel.set_volume(voice_volume)

# 音楽を停止する関数
def stop_music():
    global current_music, music_channel
    if music_channel is not None:
        music_channel.stop()
    current_music = None

# 各種フラグを処理する関数
def handle_flags(flags):
    global current_music
    for flag in flags:
        if "bg_change" in flag:
            # ファイル名のみを取得
            bg_file = os.path.basename(flag["bg_change"])
            change_background(bg_file)
        if "music" in flag:
            # デバッグ: フラグから取得した音楽ファイル名を表示
            print(f"[DEBUG] handle_flags - music flag detected: {flag['music']}")
            # ファイル名のみを取得
            music_file = os.path.basename(flag["music"])
            if current_music != music_file:
                play_music(music_file)
        if "sound_effect" in flag:
            sfx_file = os.path.basename(flag["sound_effect"])
            play_sound_effect(sfx_file)
        if "voice" in flag:
            voice_file = os.path.basename(flag["voice"])
            play_voice(voice_file)
        if "stop_music" in flag:
            stop_music()
        if "end_type" in flag:
            if flag["end_type"] == "scroll_credits":
                clear_canvas()
                show_credits(flag["ending_name"])

# スタッフロールをスクロールさせる関数
def scroll_credits(canvas, text_items, y_positions):
    finished = True
    for i, item in enumerate(text_items):
        canvas.move(item, 0, -2)
        y_positions[i] -= 2
        if canvas.itemcget(item, "text") == "〜END〜" and y_positions[i] <= 300:
            root.after(2000, lambda: music_channel.fadeout(2000))
            root.after(4000, stop_music)
            finished = True
            root.after(7000, clear_canvas)
            root.after(8000, show_opening_screen)
            return
        if y_positions[i] + 20 > 0:
            finished = False
    if not finished:
        root.after(50, scroll_credits, canvas, text_items, y_positions)
    else:
        root.after(2000, clear_canvas)
        root.after(2500, show_opening_screen)

# 右クリックメニューを無効化する関数
def disable_right_click():
    root.unbind("<Button-3>")

# 右クリックメニューを有効化する関数
def enable_right_click():
    root.bind("<Button-3>", show_context_menu)

# キャンバスをクリアする関数
def clear_canvas():
    canvas.delete("all")

def show_credits(ending_name):
    global credits_data, current_music
    root.unbind("<Button-1>")
    disable_right_click()

    # エンディングデータを取得
    ending_data = next(
        (ending for ending in credits_data["ending"] if ending["name"] == ending_name),
        None
    )

    if not ending_data:
        messagebox.showerror("エラー", "指定されたエンディングが見つかりませんでした。")
        return

    # 背景画像ファイル名を取得
    bg_image_file = os.path.basename(ending_data["bg_image"])
    theme_music_file = os.path.basename(ending_data["theme_music"])

    # デバッグ情報
    print(f"[DEBUG] Background Image File: {bg_image_file}")
    print(f"[DEBUG] Theme Music File: {theme_music_file}")

    # 背景画像を変更
    change_background(bg_image_file)

    # エンディングテーマ曲を再生（同じ曲が再生中でない場合のみ）
    if current_music != theme_music_file:
        play_music(theme_music_file, loops=0)
    else:
        print("[DEBUG] Theme music is already playing. Not restarting.")

    # クレジットテキストの生成
    credits = ending_data["credits"]
    y_positions = [600 + 40 * i for i in range(len(credits))]
    text_items = []
    for i, credit in enumerate(credits):
        position = credit.get("position", "center")
        x_position = 600
        if position == "left":
            x_position = 100
        elif position == "right":
            x_position = 1100

        text_item = canvas.create_text(
            x_position,
            y_positions[i],
            text=credit["text"],
            font=(noto_sans_regular, 20),
            fill="white",
            anchor="center"
        )
        text_items.append(text_item)

    # スタッフロールのスクロール開始
    scroll_credits(canvas, text_items, y_positions)

# パスを相対パスに変換する関数
def to_relative_path(path):
    if os.path.isabs(path):
        return os.path.normpath(os.path.relpath(path, base_path))
    return os.path.normpath(path)

def to_absolute_path(path):
    if not os.path.isabs(path):
        return os.path.abspath(os.path.join(base_path, path))
    return os.path.normpath(path)

# リソースパスを変換するヘルパー関数
def convert_resource_paths(data, to_absolute):
    for page in data["story"]:
        for flag in page.get("flags", []):
            for key in RESOURCE_KEYS:
                if key in flag:
                    flag[key] = (
                        to_absolute_path(flag[key]) if to_absolute else to_relative_path(flag[key])
                    )
        for segment in page["segments"]:
            for key in RESOURCE_KEYS:
                if key in segment:
                    segment[key] = (
                        to_absolute_path(segment[key]) if to_absolute else to_relative_path(segment[key])
                    )
            if "choices" in segment:
                for choice in segment["choices"]:
                    if "choice_file" in choice:
                        choice["choice_file"] = (
                            to_absolute_path(choice["choice_file"]) if to_absolute else to_relative_path(choice["choice_file"])
                        )

# ゲームをセーブする関数
def save_game(slot):
    global current_page, current_segment, story_data

    save_path = os.path.join(SAVE_DIR, f"save_slot_{slot}.json")

    if os.path.exists(save_path):
        result = messagebox.askyesno("上書き確認", f"スロット {slot} には既にセーブデータがあります。上書きしますか？")
        if not result:
            return

    save_description = story_data["story"][current_page].get("save_description", "No description")

    save_data = {
        "current_page": current_page,
        "current_segment": current_segment,
        "story_data": story_data,
        "save_description": save_description
    }

    convert_resource_paths(save_data["story_data"], to_absolute=False)

    with open(save_path, 'w', encoding='utf-8') as file:
        json.dump(save_data, file, ensure_ascii=False, indent=4)

    convert_resource_paths(story_data, to_absolute=True)

    messagebox.showinfo("セーブ", f"スロット {slot} にセーブしました。\n説明: {save_description}")
    update_context_menu()

# ゲームをロードする関数
def load_game(slot):
    global current_page, current_segment, story_data, text_items, choice_items, opening_items, waiting_for_choice, typing_in_progress

    save_path = os.path.join(SAVE_DIR, f"save_slot_{slot}.json")

    if os.path.exists(save_path):
        with open(save_path, 'r', encoding='utf-8') as file:
            save_data = json.load(file)

        story_data = save_data["story_data"]
        current_page = save_data["current_page"]
        current_segment = save_data["current_segment"]

        # ロードデータ内のリソースパスを絶対パスに変換
        convert_resource_paths(story_data, to_absolute=True)

        # オープニング画面の要素を削除
        for item in opening_items:
            canvas.delete(item)
        opening_items.clear()

        # テキストや選択肢の初期化
        clear_text()
        clear_choices()

        # 待機フラグのリセット
        waiting_for_choice = False
        typing_in_progress = False

        # 「ゲームスタート」ボタンのクリックイベントを無効化
        root.unbind("<Button-1>")

        # 次のセグメントを表示
        root.bind("<Button-1>", next_segment)
        next_segment()

        # メニューを更新
        update_context_menu()
        messagebox.showinfo("ロード", f"スロット {slot} からロードしました。")
    else:
        messagebox.showwarning("ロード失敗", "指定されたスロットにはセーブデータが存在しません。")

# セーブデータを削除する関数
def delete_save(slot):
    save_path = os.path.join(SAVE_DIR, f"save_slot_{slot}.json")
    if os.path.exists(save_path):
        result = messagebox.askyesno("削除確認", f"スロット {slot} のセーブデータを削除しますか？")
        if result:
            os.remove(save_path)
            messagebox.showinfo("削除完了", f"スロット {slot} のセーブデータを削除しました。")
            update_context_menu()
    else:
        messagebox.showwarning("削除失敗", "指定されたスロットにはセーブデータが存在しません。")

# セーブスロットの説明を取得する関数
def get_save_description(slot):
    save_path = os.path.join(SAVE_DIR, f"save_slot_{slot}.json")
    if os.path.exists(save_path):
        with open(save_path, 'r', encoding='utf-8') as file:
            save_data = json.load(file)
        return save_data.get("save_description", "No description")
    return "空きスロット"

# 右クリックメニューを作成する関数
def create_context_menu():
    context_menu = tk.Menu(root, tearoff=0)
    save_menu = tk.Menu(context_menu, tearoff=0)
    for i in range(1, 31):
        description = get_save_description(i)
        save_menu.add_command(label=f"スロット {i} にセーブ ({description})", command=lambda slot=i: save_game(slot))
    context_menu.add_cascade(label="セーブ", menu=save_menu)

    load_menu = tk.Menu(context_menu, tearoff=0)
    for i in range(1, 31):
        description = get_save_description(i)
        load_menu.add_command(label=f"スロット {i}: {description}", command=lambda slot=i: load_game(slot))
    context_menu.add_cascade(label="ロード", menu=load_menu)

    delete_menu = tk.Menu(context_menu, tearoff=0)
    for i in range(1, 31):
        description = get_save_description(i)
        delete_menu.add_command(label=f"スロット {i} の削除 ({description})", command=lambda slot=i: delete_save(slot))
    context_menu.add_cascade(label="セーブ削除", menu=delete_menu)

    speed_menu = tk.Menu(context_menu, tearoff=0)
    speed_menu.add_command(label="遅い", command=lambda: set_typing_speed(100))
    speed_menu.add_command(label="中間", command=lambda: set_typing_speed(50))
    speed_menu.add_command(label="速い", command=lambda: set_typing_speed(20))
    speed_menu.add_command(label="最速", command=lambda: set_typing_speed(10))
    context_menu.add_cascade(label="文字速度", menu=speed_menu)

    # 音量調整メニュー
    context_menu.add_command(label="音量調整", command=open_volume_menu)

    return context_menu

# 音量の初期設定
music_volume = 0.5
sfx_volume = 0.5
voice_volume = 0.5

volume_window = None

def open_volume_menu():
    global music_volume, sfx_volume, voice_volume, volume_window

    if volume_window is not None and tk.Toplevel.winfo_exists(volume_window):
        volume_window.lift()
        return

    def update_music_volume(val):
        global music_volume, music_channel
        music_volume = float(val)
        if music_channel is not None:
            music_channel.set_volume(music_volume)

    def update_sfx_volume(val):
        global sfx_volume
        sfx_volume = float(val)
        sfx_channel.set_volume(sfx_volume)

    def update_voice_volume(val):
        global voice_volume
        voice_volume = float(val)
        voice_channel.set_volume(voice_volume)

    volume_window = tk.Toplevel()
    volume_window.title("音量調整メニュー")
    volume_window.resizable(False, False)

    ttk.Label(volume_window, text="音楽のボリューム").pack()
    music_scale = tk.Scale(volume_window, from_=0.0, to=1.0, orient="horizontal", resolution=0.1, command=update_music_volume)
    music_scale.set(music_volume)
    music_scale.pack()

    ttk.Label(volume_window, text="効果音のボリューム").pack()
    sfx_scale = tk.Scale(volume_window, from_=0.0, to=1.0, orient="horizontal", resolution=0.1, command=update_sfx_volume)
    sfx_scale.set(sfx_volume)
    sfx_scale.pack()
    
    # # ボイスのボリューム調整スライダー
    # ttk.Label(volume_window, text="ボイスのボリューム").pack()
    # voice_scale = tk.Scale(volume_window, from_=0.0, to=1.0, orient="horizontal", resolution=0.1, command=update_voice_volume)
    # voice_scale.set(voice_volume)
    # voice_scale.pack()
    
    volume_window.protocol("WM_DELETE_WINDOW", on_close_volume_window)

def on_close_volume_window():
    global volume_window
    if volume_window is not None:
        volume_window.destroy()
        volume_window = None

# 右クリックメニューを更新する関数
def update_context_menu():
    global context_menu
    context_menu = create_context_menu()

# 右クリックメニューを表示する関数
def show_context_menu(event):
    context_menu.tk_popup(event.x_root, event.y_root)

context_menu = create_context_menu()

# 右クリックメニューをバインド
root.bind("<Button-3>", show_context_menu)

# 文字のタイピング速度を設定する関数
def set_typing_speed(speed):
    global typing_speed
    typing_speed = speed
    messagebox.showinfo("速度変更", f"文字の速度が {speed} ms に設定されました。")

# 画面を暗くするオーバーレイをトグルする関数
is_overlay_visible = False

def toggle_overlay(event=None):
    global is_overlay_visible
    is_overlay_visible = not is_overlay_visible

    if is_overlay_visible:
        canvas.create_rectangle(
            0, 0, canvas.winfo_width(), canvas.winfo_height(),
            fill='black', stipple='gray50', outline='', tags=('overlay',)
        )
        canvas.tag_lower('overlay')
        canvas.tag_lower('background')
    else:
        canvas.delete('overlay')

# "B"キーでオーバーレイをトグル
root.bind("<b>", toggle_overlay)

# オープニング画面を表示してメインループを開始
show_opening_screen()
root.resizable(False, False)
root.mainloop()
