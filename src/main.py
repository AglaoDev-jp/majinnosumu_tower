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

A heartfelt thanks to all developers and contributors who have made these libraries possible.
"""



import json
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import pygame
import os

# pygameの初期化
pygame.mixer.init()

# 現在のディレクトリを取得
current_dir = os.path.dirname(__file__)

# ストーリーとクレジットのJSONファイルのパスを定義
story_json_file = os.path.join(current_dir, '..', 'assets', 'scenario', 'scenario_01_start_point','scenario_01.json')
credits_json_file = os.path.join(current_dir, '..', 'assets', 'scenario', 'staff_credits_ver2.json')

# セーブディレクトリを作成（存在しない場合）
SAVE_DIR = os.path.join(current_dir, 'saves')
os.makedirs(SAVE_DIR, exist_ok=True)

# JSONファイルを読み込む関数
def load_json(file_path):
    try: # ファイルを開いてJSONデータを読み込む
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError: # ファイルが見つからない場合
        return None
    except json.JSONDecodeError: # JSONデータの解析エラーが発生した場合
        return None

# ストーリーとクレジットのデータを読み込む
story_data = load_json(story_json_file)
credits_data = load_json(credits_json_file)

# スクリプトの現在のディレクトリを取得
current_dir = os.path.dirname(os.path.abspath(__file__))
# サウンド関連の設定
DEFAULT_MUSIC_PATH = os.path.join(current_dir, '..', 'assets', 'audio')
# 絶対パスを作成する
DEFAULT_VOICE_PATH = os.path.abspath(os.path.join(current_dir, '..', 'assets', 'voice'))

current_music = None
current_sfx = None

# Tkinterのウィンドウ設定
root = tk.Tk()
root.title("魔人の棲む塔")
root.geometry("1200x600")

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
def change_background(image_path):
    try:
        canvas_width = root.winfo_width()
        canvas_height = root.winfo_height()

        img = Image.open(image_path)
        img = img.resize((canvas_width, canvas_height), Image.Resampling.LANCZOS)
        bg_image = ImageTk.PhotoImage(img)

        canvas.delete("background")
        canvas.create_image(0, 0, anchor="nw", image=bg_image, tags="background")
        canvas.image = bg_image
        canvas.image_path = image_path
        canvas.tag_lower("background")
    except FileNotFoundError:
        messagebox.showerror("File Not Found", f"The file '{image_path}' could not be found.")

# テキストを1文字ずつ表示する関数
def type_text(canvas, item_id, text, index=0):
    global typing_in_progress
    typing_in_progress = True
    if index < len(text):
        canvas.itemconfig(item_id, text=text[:index+1])
        root.after(typing_speed, type_text, canvas, item_id, text, index+1)
    else:
        typing_in_progress = False
        if waiting_for_choice:
            show_choices()

# オープニング画面を表示する関数
def show_opening_screen():
    enable_right_click()

    global opening_items
    clear_text()
    clear_choices()

    demon_tower_image_path = os.path.join(current_dir, '..', 'assets', 'images', 'demon_tower.webp')
    root.after(100, lambda: change_background(demon_tower_image_path))

    title_item = canvas.create_text(600, 100, text="魔人の棲む塔", font=("Helvetica", 100, "bold"), fill="red")
    opening_items.append(title_item)

    start_game_item = canvas.create_text(600, 400, text="ゲームスタート", font=("Helvetica", 24, "bold"), fill="white")
    opening_items.append(start_game_item)
    canvas.tag_bind(start_game_item, "<Button-1>", lambda e: start_game())

    explanation_item = canvas.create_text(600, 450, text="説明", font=("Helvetica", 24, "bold"), fill="white")
    opening_items.append(explanation_item)
    canvas.tag_bind(explanation_item, "<Button-1>", lambda e: show_explanation())

    root.unbind("<Button-1>")
    root.after(100, adjust_positions)

# ゲームを開始する関数
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
    convert_paths_to_absolute(story_data)

    root.bind("<Button-1>", next_segment)
    next_segment()

# 説明画面を表示する関数
def show_explanation():
    messagebox.showinfo("説明", "左クリック：文字読み、選択肢。\n右クリック：セーブロード、文字速度、音量調整\nF11 でフルスクリーン(Esc or F11で解除)\nB で暗くする(文字が読みにくいときにどうぞ)")

# 次のストーリーセグメントを表示する関数
def next_segment(event=None):
    global current_page, current_segment, text_items, choice_items, waiting_for_choice
    if typing_in_progress or waiting_for_choice:
        return
    if current_page < len(story_data["story"]):
        page = story_data["story"][current_page]

        handle_flags(page.get("flags", []))

        if current_segment < len(page["segments"]):
            segment = page["segments"][current_segment]

            handle_flags(segment.get("flags", []))

            if "text" in segment:
                color = segment.get("color", "white")
                font_size = segment.get("font_size", 20)
                line_height = font_size + 10

                text_item = canvas.create_text(
                    20,
                    20 + line_height * len(text_items),
                    anchor="nw",
                    text="",
                    font=("Helvetica", font_size),
                    fill=color,
                    tags="text"
                )
                text_items.append(text_item)
                type_text(canvas, text_item, segment["text"])

            if "music" in segment:
                play_music(segment["music"])

            if "sound_effect" in segment:
                play_sound_effect(segment["sound_effect"])

            if "voice" in segment:
                play_voice(segment["voice"])

            if "bg_change" in segment:
                change_background(segment["bg_change"])

            if "choices" in segment:
                waiting_for_choice = True
                return

            current_segment += 1
        else:
            current_segment = 0
            current_page += 1
            clear_text()
            next_segment()
    else:
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

# 選択肢テキストを作成する関数
def create_choice_texts(segment):
    global choice_items
    clear_choices()
    choice_start_y = 20 + 30 * len(text_items)
    for i, choice in enumerate(segment["choices"]):
        choice_item = canvas.create_text(
            20,
            choice_start_y + 30 * i,
            anchor="nw",
            text=choice['text'],
            font=("Helvetica", 20, "bold"),
            fill="white",
            tags=("choice",)
        )
        choice_items.append(choice_item)
        canvas.tag_bind(choice_item, "<Enter>", lambda e, item=choice_item: canvas.itemconfig(item, fill="lightgray"))
        canvas.tag_bind(choice_item, "<Leave>", lambda e, item=choice_item: canvas.itemconfig(item, fill="white"))
        canvas.tag_bind(choice_item, "<Button-1>", lambda e, c=choice: select_choice(c))

# 選択肢が選ばれた際に呼び出される関数
def select_choice(choice):
    global waiting_for_choice
    waiting_for_choice = False
    load_choice(choice["choice_file"])

# 選択肢に基づいて新しいシナリオをロードする関数
def load_choice(choice_file):
    global story_data, current_page, current_segment, text_items, choice_items
    story_data = load_json(choice_file)

    convert_paths_to_absolute(story_data)

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

# 音楽を再生する関数
def play_music(music_file, loops=-1):
    global current_music, music_volume
    music_path = os.path.join(DEFAULT_MUSIC_PATH, music_file)
    if current_music != music_path:
        pygame.mixer.music.load(music_path)
        pygame.mixer.music.play(loops=loops)
        pygame.mixer.music.set_volume(music_volume)
        current_music = music_path

# 効果音とボイスのチャンネルを作成
sfx_channel = pygame.mixer.Channel(1)
voice_channel = pygame.mixer.Channel(2)

def play_sound_effect(sfx_file):
    sfx_path = os.path.join(DEFAULT_MUSIC_PATH, sfx_file)
    sfx = pygame.mixer.Sound(sfx_path)
    sfx.set_volume(sfx_volume)
    sfx_channel.play(sfx)

def play_voice(voice_file):
    if not os.path.isabs(voice_file):
        voice_path = os.path.join(DEFAULT_VOICE_PATH, voice_file)
    else:
        voice_path = voice_file

    voice_path = os.path.normpath(voice_path)
    try:
        voice = pygame.mixer.Sound(voice_path)
        voice.set_volume(voice_volume)
        voice_channel.play(voice)
    except FileNotFoundError:
        print(f"Error: File not found at {voice_path}")

# ボリューム調整関数でチャンネルのボリュームを更新
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
    pygame.mixer.music.stop()
    global current_music
    current_music = None

# 各種フラグを処理する関数
def handle_flags(flags):
    for flag in flags:
        if "bg_change" in flag:
            change_background(flag["bg_change"])
        if "music" in flag:
            play_music(flag["music"])
        if "sound_effect" in flag:
            play_sound_effect(flag["sound_effect"])
        if "voice" in flag:
            if not os.path.isabs(flag["voice"]):
                flag["voice"] = os.path.join(DEFAULT_VOICE_PATH, flag["voice"])
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
        if canvas.itemcget(item, "text") == "~END~" and y_positions[i] <= 300:
            root.after(2000, lambda: pygame.mixer.music.fadeout(2000))
            root.after(4000, stop_music)  # 音楽を完全に停止
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

# クレジット画面を表示する関数
def show_credits(ending_name):
    global credits_data
    root.unbind("<Button-1>")

    disable_right_click()

    ending_data = next((ending for ending in credits_data["ending"] if ending["name"] == ending_name), None)

    if not ending_data:
        messagebox.showerror("エラー", "指定されたエンディングが見つかりませんでした。")
        return

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

        text_item = canvas.create_text(x_position, y_positions[i], text=credit["text"], font=("Helvetica", 20), fill="white", anchor="center")
        text_items.append(text_item)

    scroll_credits(canvas, text_items, y_positions)

    # 背景画像を変更
    change_background(os.path.join(current_dir, '..', 'assets', ending_data["bg_image"]))

    # エンディングテーマ曲を再生
    play_music(os.path.join(current_dir, '..', 'assets', ending_data["theme_music"]), loops=0)

# 相対パスを絶対パスに変換する関数
def convert_paths_to_absolute(data):
    for page in data["story"]:
        for flag in page["flags"]:
            if "bg_change" in flag:
                flag["bg_change"] = os.path.join(current_dir, '..', 'assets', flag["bg_change"])
            if "music" in flag:
                flag["music"] = os.path.join(current_dir, '..', 'assets', flag["music"])
            if "sound_effect" in flag:
                flag["sound_effect"] = os.path.join(current_dir, '..', 'assets', flag["sound_effect"])
            if "voice" in flag:
                flag["voice"] = os.path.join(current_dir, '..', 'assets', flag["voice"])
        for segment in page["segments"]:
            if "bg_change" in segment:
                segment["bg_change"] = os.path.join(current_dir, '..', 'assets', segment["bg_change"])
            if "music" in segment:
                segment["music"] = os.path.join(current_dir, '..', 'assets', segment["music"])
            if "sound_effect" in segment:
                segment["sound_effect"] = os.path.join(current_dir, '..', 'assets', segment["sound_effect"])
            if "voice" in segment:
                segment["voice"] = os.path.join(current_dir, '..', 'assets', segment["voice"])
            if "choices" in segment:
                for choice in segment["choices"]:
                    choice["choice_file"] = os.path.join(current_dir, '..', 'assets', choice["choice_file"])

# ゲームをセーブする関数
def save_game(slot):
    global current_page, current_segment, story_data
    save_path = os.path.join(SAVE_DIR, f"save_slot_{slot}.json")  # Save as JSON

    if os.path.exists(save_path):
        result = messagebox.askyesno("上書き確認", f"スロット {slot} には既にセーブデータがあります。上書きしますか？")
        if not result:
            return

    save_data = {
        "current_page": current_page,
        "current_segment": current_segment,
        "story_data": story_data
    }

    with open(save_path, 'w', encoding='utf-8') as file:
        json.dump(save_data, file, ensure_ascii=False, indent=4)

    update_context_menu()

    save_description = story_data["story"][current_page].get("save_description", "No description")
    messagebox.showinfo("セーブ", f"スロット {slot} にセーブしました。\n説明: {save_description}")

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
        convert_paths_to_absolute(story_data)

        for item in opening_items:
            canvas.delete(item)
        opening_items.clear()

        clear_text()
        clear_choices()

        waiting_for_choice = False
        typing_in_progress = False

        root.bind("<Button-1>", next_segment)

        if current_page < len(story_data["story"]):
            next_segment()
        else:
            show_opening_screen()

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
    save_path = os.path.join(SAVE_DIR, f"save_slot_{slot}.json")  # Save as JSON
    if os.path.exists(save_path):
        with open(save_path, 'r', encoding='utf-8') as file:
            save_data = json.load(file)  # Read as JSON
        current_page = save_data["current_page"]
        description = save_data["story_data"]["story"][current_page].get("save_description", "No description")
        return description
    else:
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

# 音量調整用のメニューウィンドウ
# 音量の初期設定
music_volume = 0.5  # 初期の音楽ボリューム
sfx_volume = 0.5    # 初期の効果音ボリューム
voice_volume = 0.5  # 初期のボイスボリューム

def open_volume_menu():
    global music_volume, sfx_volume, voice_volume

    def update_music_volume(val):
        global music_volume
        music_volume = float(val)
        pygame.mixer.music.set_volume(music_volume)  # 音楽のボリュームを更新

    def update_sfx_volume(val):
        global sfx_volume
        sfx_volume = float(val)

    def update_voice_volume(val):
        global voice_volume
        voice_volume = float(val)

    # Tkinterのウィンドウを作成
    volume_window = tk.Toplevel()
    volume_window.title("音量調整メニュー")

    # 音楽のボリューム調整スライダー
    ttk.Label(volume_window, text="音楽のボリューム").pack()
    music_scale = tk.Scale(volume_window, from_=0.0, to=1.0, orient="horizontal", resolution=0.1, command=update_music_volume)
    music_scale.set(music_volume)
    music_scale.pack()

    # 効果音のボリューム調整スライダー
    ttk.Label(volume_window, text="効果音のボリューム").pack()
    sfx_scale = tk.Scale(volume_window, from_=0.0, to=1.0, orient="horizontal", resolution=0.1, command=update_sfx_volume)
    sfx_scale.set(sfx_volume)
    sfx_scale.pack()

    # ボイスのボリューム調整スライダー
    ttk.Label(volume_window, text="ボイスのボリューム").pack()
    voice_scale = tk.Scale(volume_window, from_=0.0, to=1.0, orient="horizontal", resolution=0.1, command=update_voice_volume)
    voice_scale.set(voice_volume)
    voice_scale.pack()

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

