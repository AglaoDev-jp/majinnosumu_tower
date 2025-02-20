"""
作成者: AglaoDev-jp  
Copyright © 2024 AglaoDev-jp
ライセンス情報:
- コード: MIT License
This software is licensed under the MIT License. For details, see the LICENSE file.

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

"""

from PIL import Image  # PillowライブラリからImageモジュールをインポート
import os  # ファイル操作用の標準ライブラリ
import tkinter as tk  # GUIを作成するためのTkinterモジュール
from tkinter import filedialog, messagebox  # フォルダ選択ダイアログとメッセージ表示を利用

# 画像変換関数
def convert_webp_to_format(input_folder, output_folder, output_format="png"):
    # 出力フォルダが存在しない場合は作成
    os.makedirs(output_folder, exist_ok=True)
    
    # 入力フォルダ内のすべてのファイルを取得
    for filename in os.listdir(input_folder):
        # .webpファイルのみを対象とする
        if filename.endswith(".webp"):
            image_path = os.path.join(input_folder, filename)  # 各画像のパスを作成
            try:
                image = Image.open(image_path)  # 画像を開く
                output_filename = f"{os.path.splitext(filename)[0]}.{output_format}"  # 出力ファイル名を決定
                output_path = os.path.join(output_folder, output_filename)  # 出力パスを作成
                
                image = image.convert("RGB")  # JPEG保存のためRGBに変換（PNGも問題なく保存可能）
                image.save(output_path, output_format.upper())  # 指定フォーマットで画像を保存
                print(f"変換完了: {filename} -> {output_filename}")  # 変換完了をコンソールに表示
            except Exception as e:
                print(f"エラーが発生しました: {filename}, エラー内容: {e}")  # エラー内容を表示

# 入力フォルダ選択ダイアログを表示する関数
def select_input_folder():
    folder = filedialog.askdirectory()  # フォルダ選択ダイアログを表示
    if folder:  # 選択された場合
        input_folder_var.set(folder)  # 選択されたフォルダパスを入力欄に設定

# 出力フォルダ選択ダイアログを表示する関数
def select_output_folder():
    folder = filedialog.askdirectory()  # フォルダ選択ダイアログを表示
    if folder:  # 選択された場合
        output_folder_var.set(folder)  # 選択されたフォルダパスを出力欄に設定

# 変換を開始する関数
def start_conversion():
    input_folder = input_folder_var.get()  # 入力フォルダのパスを取得
    output_folder = output_folder_var.get()  # 出力フォルダのパスを取得
    
    # 入力フォルダまたは出力フォルダが選択されていない場合、警告を表示
    if not input_folder or not output_folder:
        messagebox.showwarning("警告", "フォルダを選択してください。")
        return
    
    # 画像変換を実行し、完了メッセージを表示
    convert_webp_to_format(input_folder, output_folder, output_format_var.get())
    messagebox.showinfo("完了", "画像の変換が完了しました。")

# Tkinterウィンドウの設定
root = tk.Tk()
root.title("WebP画像変換ツール")  # ウィンドウタイトル
root.geometry("400x300")  # ウィンドウサイズ

# 入力フォルダ選択用ウィジェット
input_folder_var = tk.StringVar()  # 入力フォルダのパスを保持する変数
tk.Label(root, text="変換する画像フォルダ:").pack(pady=5)  # ラベルを表示
tk.Entry(root, textvariable=input_folder_var, width=40).pack()  # フォルダパスを表示するエントリ
tk.Button(root, text="フォルダを選択", command=select_input_folder).pack(pady=5)  # フォルダ選択ボタン

# 出力フォルダ選択用ウィジェット
output_folder_var = tk.StringVar()  # 出力フォルダのパスを保持する変数
tk.Label(root, text="変換後の画像フォルダ:").pack(pady=5)  # ラベルを表示
tk.Entry(root, textvariable=output_folder_var, width=40).pack()  # フォルダパスを表示するエントリ
tk.Button(root, text="フォルダを選択", command=select_output_folder).pack(pady=5)  # フォルダ選択ボタン

# 変換形式の選択ウィジェット
output_format_var = tk.StringVar(value="png")  # デフォルトでpngを選択
tk.Label(root, text="変換形式:").pack(pady=5)  # ラベルを表示
tk.OptionMenu(root, output_format_var, "png", "jpeg").pack()  # 変換形式のドロップダウンメニュー

# 変換開始ボタン
tk.Button(root, text="変換開始", command=start_conversion).pack(pady=10)  # 変換開始ボタン

# ウィンドウサイズの変更を禁止
root.resizable(False, False)

# Tkinterのメインループ開始
root.mainloop()
