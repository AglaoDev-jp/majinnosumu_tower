import os
import json

def add_arrow_icon_to_last_segment_in_story(json_file_path):
    """
    指定した JSON ファイルを読み込み、story 配列の中にある各 segments 配列の最後の要素に
    'arrow_icon': 'page_turn.png' を付与し、同ファイルへ上書き保存します。
    """
    try:
        with open(json_file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # "story" キーが存在し、配列になっているかチェック
        if "story" in data and isinstance(data["story"], list):
            modified = False

            for story_element in data["story"]:
                # 各ストーリー要素に "segments" があり、リストで要素がある場合
                if "segments" in story_element and isinstance(story_element["segments"], list) and len(story_element["segments"]) > 0:
                    # 最後の要素に arrow_icon を付与
                    story_element["segments"][-1]["arrow_icon"] = "page_turn.png"
                    modified = True
                else:
                    # segments が存在しない/空の場合は警告ログを出すだけ
                    print(f"[警告] {json_file_path} の story 要素の一つに 'segments' が存在しないか空でした。")

            # いずれかの segments が修正された場合のみ、ファイルを上書き保存
            if modified:
                with open(json_file_path, 'w', encoding='utf-8') as f:
                    json.dump(data, f, ensure_ascii=False, indent=2)
                print(f"[完了] {json_file_path} 内の各 story の 'segments' に arrow_icon を追加しました。")
            else:
                print(f"[情報] {json_file_path} は修正不要（または 'segments' が全て空）でした。")
        else:
            print(f"[警告] {json_file_path} に 'story' キーが無いか、story が配列ではありません。")

    except Exception as e:
        print(f"[エラー] {json_file_path} の処理中にエラーが発生しました: {e}")


if __name__ == "__main__":
    # スクリプトのあるディレクトリを取得
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # スクリプトのあるディレクトリ内に存在する .json ファイルをすべて取得
    json_files = [f for f in os.listdir(script_dir) if f.lower().endswith(".json")]

    if not json_files:
        print("[情報] このディレクトリに JSON ファイルが見つかりませんでした。")
    else:
        for json_file in json_files:
            json_file_path = os.path.join(script_dir, json_file)
            add_arrow_icon_to_last_segment_in_story(json_file_path)

    print("一連の処理が完了しました。")
