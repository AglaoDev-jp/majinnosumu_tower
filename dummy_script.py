import importlib.util
import traceback
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
import base64

# エラーログファイルのパスを定義
log_file = os.path.join(os.path.dirname(__file__), "error.log")

def log_error(e):
    """エラー内容をログファイルに記録する"""
    with open(log_file, "w") as f:
        traceback.print_exc(file=f)
    print(f"An error occurred. Check {log_file} for details.")
    raise

try:
    # 実行ファイルかどうかの判定
    if getattr(sys, 'frozen', False):
        execution_path = sys._MEIPASS  # PyInstallerで生成された場合
        print("Running from PyInstaller executable.")
    else:
        execution_path = os.path.dirname(__file__)  # スクリプト実行の場合
        print("Running from Python script.")

    # デバッグ情報
    print(f"Execution Path: {execution_path}")
    print(f"sys.path before: {sys.path}")

    # srcフォルダのパスを検索パスに追加
    src_path = os.path.join(execution_path, "src")
    if src_path not in sys.path:
        sys.path.append(src_path)

    print(f"sys.path after: {sys.path}")

    # assetsフォルダが正しく存在するか確認
    assets_path = os.path.join(execution_path, "assets")
    if os.path.exists(assets_path):
        print(f"Assets directory found: {assets_path}")
    else:
        print(f"Assets directory not found: {assets_path}")
        raise FileNotFoundError(f"Assets directory is missing at: {assets_path}")

    # srcフォルダ内の.pydファイルを検索
    pyd_files = [f for f in os.listdir(src_path) if f.endswith(".pyd")]
    if pyd_files:
        # 最初に見つかった.pydファイルを使う
        main_pyd_file = pyd_files[0]
        main_pyd_path = os.path.join(src_path, main_pyd_file)
        print(f"Found .pyd file: {main_pyd_path}")

        try:
            # .pydファイルをロード
            spec = importlib.util.spec_from_file_location("main", main_pyd_path)
            main = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(main)
            print("Module 'main' loaded successfully!")
        except Exception as e:
            print(f"Failed to load module 'main': {e}")
            log_error(e)
    else:
        raise FileNotFoundError(f"No .pyd file found in {src_path}.")

    # sys._MEIPASS のデバッグ情報を出力
    if getattr(sys, 'frozen', False):
        print(f"sys._MEIPASS content:")
        for root, dirs, files in os.walk(sys._MEIPASS):
            for name in files:
                print(os.path.join(root, name))

except Exception as e:
    log_error(e)
