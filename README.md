
# 魔人の棲む塔_visual-novel-game
A visual novel game project  
コード作成、シナリオ作成、テキスト作成、画像生成にChatGPTを使用しています。  
製作期間: ver.1 2024年6月~2024年9月中旬  
※このリポジトリは個人学習のために使用しています。そのため、プルリクエスト（Pull Request）はお受けすることができません。ご了承ください。  

## 使用言語とライブラリ

### 使用言語
- **Python 3.12.5**

### 使用ライブラリ
- **Tkinter** - GUI作成の標準ライブラリ
- **Pillow (Python Imaging Library)** - 画像処理
- **Pygame** - サウンドの追加
- **OS** - OS操作関連の処理
- **JSON** - シナリオ、ゲームデータの管理

### 使用エディター
- **Visual Studio Code (VSC)**  

## 著作権表示とライセンス

- **Python**  
    © Python Software Foundation  
    Licensed under the Python Software Foundation License (PSF License).  
    [Python license](https://docs.python.org/3/license.html)またはフォルダ内の[LICENSE-PSF.txt](./licenses/third_party/LICENSE-PSF.txt)をご確認ください。  
    ※コードのみであればライセンス添付は不要ですが、PyInstallerを使って実行ファイル化する際にはPythonのライセンス（PSF License）の添付が必要です。

- **Tkinter**  
    © Regents of the University of California, Sun Microsystems, Inc., Scriptics Corporation, and other parties  
    TkinterはPythonに含まれるGUIライブラリですが、その動作にはTcl/Tkが使用されています。
    [Tcl/Tk License](https://www.tcl.tk/software/tcltk/license.html)またはフォルダ内の[LICENSE-TclTk.txt](./licenses/third_party/LICENSE-TclTk.txt)をご確認ください。

### このプロジェクトでは、以下のオープンソースライブラリを使用しています：

- **Pillow**  
    The Python Imaging Library (PIL) is  
    © 1997-2011 by Secret Labs AB  
    © 1995-2011 Fredrik Lundh and Contributors.  
    Pillow is the friendly PIL fork. It is  
    © 2010-2024 by Jeffrey A. Clark and contributors  
    Licensed under the Historical Permission Notice and Disclaimer (HPND) License.  
    [Pillow License](https://github.com/python-pillow/Pillow/blob/main/LICENSE)

- **Pygame**  
    © 2000-2024 Pygame developers  
    Licensed under the GNU Lesser General Public License (LGPL).  
    [Pygame License](https://github.com/pygame/pygame/blob/main/docs/LGPL.txt)

サードパーティライブラリのライセンス詳細は、[THIRD_PARTY_LICENSES.txt](./licenses/third_party/THIRD_PARTY_LICENSES.txt)から確認できます。  
  
これらのプロジェクトの開発者および貢献者の皆様に、心より感謝申し上げます。  


---

## フォントについて
本ゲームのフォントは、PC内の"Helvetica"を参照する設定がされています。  
**注意:**   
環境によっては、代替フォントが表示される場合があります。  
本ゲームファイルには"Helvetica"自体は含まれていません。

- **Helveticaの使用に関するライセンス:**  
"Helvetica"の使用には、特定の条件下でライセンスが必要になる場合があります。ライセンス条件については、各自でご確認ください。

- **代替フォントの利用:**  
Helveticaのライセンス条件や利用に懸念がある場合は、比較的自由なライセンスのフォントの利用を検討してください。

## 音源について
本ゲームファイルには、音楽や効果音の音源自体は含まれておりません。ゲームで使用する音楽と効果音は、以下の提供元サイトからダウンロードをお願いします。
ご利用にあたっては、各提供元サイトの規約をよくお読みいただき、適切な利用をお願いします。

### 音楽
提供: フリーBGM DOVA-SYNDROME  
- 「strange lullaby」 - shimtone  
- 「奇妙な話」 - Heitaro Ashibe  
- 「透明な亡霊」 - Heitaro Ashibe  
- 「発見」 - のる  
- 「静かな夜に」 - のる  
- 「怖い系リプレイ音」 - Causality Sound  
- 「ENEMY_ENCOUNTER」 - MagaMaga  
- 「プレリュード第2番「名前を入力してください」」 - 秦暁  

### 効果音
提供: 効果音ラボ  
- ギャアアアア！  
- オーラ1  
- ガラスが割れる1  
- ゴブリンの鳴き声1  
- ゴブリンの鳴き声2  
- ライオンの鳴き声1  
- 怪獣の足音  
- 崖崩れ  
- 岩にヒビが入る  
- 剣の素振り1  
- 重力魔法2  
- 小キック  
- 全力で踏み込む  
- 地響き  
- 締め付ける2  
- 鉄の扉を閉める  
- 風が吹く1  
- 風に揺れる草木1  
- 魔法使いが空を飛ぶ  
- 雷魔法4  
- 牢屋の扉を閉める  

   （敬称略）
    
素晴らしい音源を提供いただき、心より感謝申し上げます。

## 問題点
このゲームのコードには、作者が考える限り以下の問題点、改善点があります。
- 画像のフルスクリーンはできるが、文字は大きくなっていない（位置を変えているだけ）
- 画像効果がない。
- 音楽のフェードインフェードアウトの実装
- 行単位、セグメント単位でしか音楽の変更、画像の変更ができない。
- 行を跨いで文字送りができない（文字が多いと文字が画面外に出る）
- テキストを行の途中で止めたり進めたりできない。
- 文字送りのアニメーション、ページ送りのアニメーションがない。
- 音量設定のポップアップが無限に出せる。
- ゲームフォルダを別の場所に移動するとセーブが使い物にならなくなる。
- すべて関数で書かれているため、コードが長い。
- グローバル変数を使いすぎている。
- フォントの記述方法が一般的でなく、条件によっては問題があるかもしれない。

---

## このゲームの遊び方

このゲームには上記の問題があるため、実行ファイル化を行っておりません。ゲームを遊ぶためには、以下の手順に従ってください。

1. **Pythonのインストール**  
   `.py`ファイルの実行には、Pythonがインストールされている環境が必要です。

2. **使用ライブラリのインストール**  
   使用ライブラリのPillowとPygameは、別途インストールが必要です。`requirements.txt`ファイルを作成してありますので、以下の手順でインストールしてください。

   - コマンドラインインターフェース (CLI: ターミナル、コマンドプロンプト、PowerShellなど) を使用し、`cd`コマンドで`requirements.txt`ファイルのあるディレクトリに移動します。  
   例: `majinnosumu_tower_visual_novel_game-main`フォルダを右クリックして「パスをコピー」、または`requirements.txt`ファイルを右クリックして「プロパティ」の「場所」をコピーなど。  
   
   ```shell
   # 例: デスクトップにフォルダがある場合 (パスはPC環境により異なります)
   cd "C:\..\..\Desktop\majinnosumu_tower_visual_novel_game-main"
   ```

   - 次のコマンドで必要なライブラリ (PillowとPygame) が一括でインストールできます。
   ```shell
   pip install -r requirements.txt
   ```

   - 個別にインストールしたい場合は、以下のコマンドを使用してください。
   
   Pillowのインストール
   ```shell
   pip install Pillow
   ```

   Pygameのインストール
   ```shell
   pip install pygame
   ```

3. **音源ファイルの配置**  
   音源ファイルを`asset`フォルダ内の`audio`および`sound_effects`フォルダに移動してください。  
   （音源のリストは各フォルダ内にもあります）

4. **ゲームの起動**  
   コマンドラインインターフェースを使用して、以下の手順でゲームを起動します。

   - `cd`コマンドで`src`フォルダ内にある`main.py`ファイルのディレクトリに移動します。  
   例: `src`フォルダを右クリックして「パスをコピー」、または`main.py`ファイルを右クリックして「プロパティ」の「場所」をコピーなど。  
   ```shell
   # 例: デスクトップにフォルダがある場合 (パスはPC環境により異なります)
   cd "C:\..\..\Desktop\majinnosumu_tower_visual_novel_game-main\src"
   ```

   - フォルダに移動後、以下のコマンドでゲームを起動します。  
   ```shell
   python main.py
   ```

5. **コードエディターでの実行**  
   一部のコードエディター（VSCなど）では、直接ファイルを実行することが可能です。

---


## 免責事項
本ゲームの利用や環境設定によるいかなる損害や問題について、作者は一切の責任を負いかねます。

## このゲームのライセンス

- **コード**: MIT License。詳細は[LICENSE-CODE](./licenses/game/LICENSE-CODE)ファイルを参照してください。
- **画像**: Creative Commons Attribution 4.0 (CC BY 4.0)。詳細は[LICENSE-IMAGES](./licenses/game/LICENSE-IMAGES)ファイルを参照してください。
- **シナリオ**: Creative Commons Attribution-ShareAlike 4.0 (CC BY-SA 4.0)。詳細は[LICENSE-SCENARIOS](./licenses/game/LICENSE-SCENARIOS)ファイルを参照してください。

## ライセンスの簡単な説明

- **コード**: （MIT License）
このゲームのコードは、MITライセンスのもとで提供されています。自由に使用、改変、配布が可能ですが、著作権表示とライセンスの文言を含める必要があります。

- **画像**: （Creative Commons Attribution 4.0, CC BY 4.0）
このゲームの画像は、CC BY 4.0ライセンスのもとで提供されています。自由に使用、改変、配布が可能ですが、著作権者のクレジットを表示する必要があります。

- **シナリオ**:（Creative Commons Attribution-ShareAlike 4.0, CC BY-SA 4.0）
このゲームのシナリオは、CC BY-SA 4.0ライセンスのもとで提供されています。自由に使用、改変、配布が可能ですが、著作権者のクレジットを表示し、改変後も同じライセンス条件を適用する必要があります。

※これらの説明はライセンスの概要です。詳細な内容は各ライセンスの原文に準じます。

---

## クレジット表示のテンプレート（例）

### コード
- **作成者**: AglaoDev-jp  
- **著作権**: © 2024 AglaoDev-jp  
- **ライセンス**: MIT License  
- **表示例**: "Code by AglaoDev-jp, licensed under MIT License"

### 画像
- **作成者**: AglaoDev-jp  
- **著作権**: © 2024 AglaoDev-jp  
- **ライセンス**: Creative Commons Attribution 4.0 (CC BY 4.0)  
- **表示例**: "Image by AglaoDev-jp, licensed under CC BY 4.0"  

### シナリオ
- **作成者**: AglaoDev-jp  
- **著作権**: © 2024 AglaoDev-jp  
- **ライセンス**: Creative Commons Attribution-ShareAlike 4.0 (CC BY-SA 4.0)  
- **表示例**: "Scenario by AglaoDev-jp, licensed under CC BY-SA 4.0"  

---
#### ライセンスの理由
現在のAI生成コンテンツの状況を踏まえ、私は本作品を可能な限りオープンなライセンス設定になるように心がけました。  
問題がある場合、状況に応じてライセンスを適切に見直す予定です。  

このライセンス設定は、権利の独占を目的とするものではありません。明確なライセンスを設定することにより、パブリックドメイン化するリスクを避けつつ、自由な利用ができるように期待するものです。  
 
© 2024 AglaoDev-jp

