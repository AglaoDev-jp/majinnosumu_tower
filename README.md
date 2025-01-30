
---

# 魔人の棲む塔_visual-novel-game ver-3.1

A visual novel game project  
コード作成、シナリオ作成、テキスト作成、画像生成にChatGPTを使用しています。  
このリポジトリは、ゲームの**ソースコード**を記載しています  
  
---

**製作期間**

- **ver-1.0**: 2024年6月 ~ 2024年9月中旬
- **ver-2.0**: 2024年10月31日 ~ 2024年11月11日  
- **ver-3.0**: 2024年11月11日 ~ 2024年11月23日
- **ver-3.1**: 2024年11月23日

※ このリポジトリは個人学習のために使用しています。そのため、プルリクエスト（Pull Request）は、お受けすることができません。ご了承ください。  

---

## 免責事項
本ゲームの利用や環境設定によるいかなる損害や問題について、作者は一切の責任を負いかねます。

---

## 使用言語とライブラリ

### 使用言語
- **Python 3.12.5**

### 使用ライブラリ
- **Tkinter** - GUI（グラフィカルユーザーインターフェース）を作成するための標準ライブラリ
- **Pillow (Python Imaging Library)** - 画像処理（外部ライブラリ）
- **Pygame** - サウンドの追加（外部ライブラリ）
- **os** - OS操作関連の処理（標準ライブラリ）
- **json** - シナリオ、ゲームデータの管理（標準ライブラリ）
- **sys** - 実行環境やコマンドライン引数の管理、PyInstallerでの凍結状態の判定（標準ライブラリ、ver-3.0, ver-3.1より追加）

### 使用エディター
- **Visual Studio Code (VSC)**  

---

## 著作権表示とライセンス

- **Python**  
    © Python Software Foundation  
    Licensed under the Python Software Foundation License (PSF License).  
    [Python license](https://docs.python.org/3/license.html) またはフォルダ内の [LICENSE-PSF.txt](./licenses/third_party/LICENSE-PSF.txt) をご確認ください。  
    ※コードのみであればライセンス添付は不要ですが、PyInstallerを使って実行ファイル化する際にはPythonのライセンス（PSF License）の添付が必要です。

- **Tkinter**  
    © Regents of the University of California, Sun Microsystems, Inc., Scriptics Corporation, and other parties  
    TkinterはPythonに含まれるGUIライブラリですが、その動作にはTcl/Tkが使用されています。  
    [Tcl/Tk License](https://www.tcl.tk/software/tcltk/license.html) またはフォルダ内の [LICENSE-TclTk.txt](./licenses/third_party/LICENSE-TclTk.txt) をご確認ください。

---

### このプロジェクトでは、以下のオープンソースライブラリを使用しています：

- **Pillow**  
    The Python Imaging Library (PIL) is  
    © 1997-2011 by Secret Labs AB  
    © 1995-2011 by Fredrik Lundh and Contributors.  
    Pillow is the friendly PIL fork. It is  
    © 2010-2024 by Jeffrey A. Clark and contributors  
    Licensed under the Historical Permission Notice and Disclaimer (HPND) License.  
    [Pillow License](https://github.com/python-pillow/Pillow/blob/main/LICENSE)

- **Pygame**  
    © 2000-2024 Pygame developers  
    Licensed under the GNU Lesser General Public License (LGPL).  
    [Pygame License](https://github.com/pygame/pygame/blob/main/docs/LGPL.txt)

サードパーティライブラリのライセンス詳細は、[THIRD_PARTY_LICENSES.txt](./licenses/third_party/THIRD_PARTY_LICENSES.txt) から確認できます。  
## 使用ライブラリのインストール方法は下記に記載しています。  

---

## フォントについて
本ゲームのフォントは、"Noto Sans JP"フォントファミリー (NotoSansJP-Regular.otf, NotoSansJP-Bold.otf, NotoSansJP-Black.otf) を使用しています。  

- **Noto Sans JP**  
    © 2014-2024 Google LLC  
    Licensed under the SIL Open Font License, Version 1.1  
    Noto Sans JPは自由に利用できるフォントライセンスに基づいており、再配布および改変も許可されていますが、フォント自体の販売は禁止されています。  
    詳細については、[OFL.txt](./licenses/third_party/OFL.txt) をご確認ください。  

- **PyInstaller**  
  本ソースコードは、PyInstallerを使用する実行ファイル化に対応しました。  
  [PyInstallerの公式ライセンス情報](https://github.com/pyinstaller/pyinstaller/blob/develop/COPYING.txt) をご参照ください。　

---

これらのプロジェクトの開発者および貢献者の皆様に、心より感謝申し上げます。  

---

## 音源について
ソースコードフォルダには、音楽や効果音の音源自体は含まれておりません。ゲームで使用する音楽と効果音は、以下の提供元サイトからダウンロードをお願いします。
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

---

## 問題点と改善履歴

### ver-3.1での改善点
今までの記述では実行ファイル化を行うことができなかったため、大幅な変更を行いました。以下は主な改善点です：
- PyInstallerによる実行ファイル化に対応するため、`asset`フォルダを参照する`base_path`を定義しました（ソースコードからの起動にも対応）。
- セーブデータの保存先を、実行ファイルが存在するフォルダ内に作成されるよう変更しました（スクリプトを直接実行する場合は、ソースコードが存在するフォルダ内に保存されます）。
- ファイルの読み込みフラグをリストで管理する方式に変更し、フラグ管理全体の記述を簡素化・最適化しました。
- すべてのファイルパス定義を見直し、適切な形式に修正しました。
- 画像形式をすべてPNGに統一しました。  
- 不要な記述や重複するコードを削除しました（エラーハンドリングなど意図的に残している部分もあります）。  
- `platform`ライブラリを削除しました。これに伴い、セーブデータの保存先を実行ファイルまたはスクリプトの存在するフォルダに統一しました。これにより、OSによる動作の違いをなくし、コードの可読性とメンテナンス性を向上させました。  

### 注意点  
`platform`ライブラリの削除を行い、セーブデータの保存先が実行ファイルまたはスクリプトの存在するフォルダに統一しましたが、以下のような難点もあります：  
- **保存場所の固定化**  
  ユーザーのプロファイルディレクトリに保存する場合と違い、セーブデータがアプリケーションの配置場所に依存しています。  
  セーブフォルダまたは実行ファイルを異なるフォルダに配置した場合にはデータが共有されません。  
  必ず同一のディレクトリに、実行ファイルと`saves`フォルダを配置してください。

---

### 残る問題点
- 画像はフルスクリーン表示可能だが、テキストのサイズは変更されず、位置のみ調整される。
- 画像エフェクトが未実装。
- 音楽のフェードイン・フェードアウトが未実装。
- 行やセグメント単位でのみ、音楽や画像の変更が可能。
- 行を超えた文字送りができない（文字量が多いと画面外にはみ出す）。
- テキストを途中で一時停止または再開する機能がない。
- 文字送りアニメーションやページ送りアニメーションがない。
- すべて関数で書かれているため、コードが長くなっている。
- グローバル変数の使用が多い。

---

## ソースコードについて

ソースコードからゲームを遊ぶためには、以下の手順に従ってください。

1. **Pythonのインストール**  
   `.py`ファイルの実行には、Pythonがインストールされている環境が必要です。

2. **使用ライブラリのインストール**  
   使用ライブラリのPillowとPygameは、別途インストールが必要です。`requirements.txt`ファイルを作成してありますので、以下の手順でインストールしてください。

   - コマンドラインインターフェース (CLI: ターミナル、コマンドプロンプト、PowerShellなど) を使用し、`cd`コマンドで`requirements.txt`ファイルのあるディレクトリに移動します。  
   例: `majinnosumu_tower_visual_novel_game-ver-3.1`フォルダを右クリックして「パスをコピー」、または`requirements.txt`ファイルを右クリックして「プロパティ」の「場所」をコピーなど。  
   
   ```shell
   # 例: デスクトップにフォルダがある場合 (パスはPC環境により異なります)
   cd "C:\..\..\Desktop\majinnosumu_tower_visual_novel_game-ver-3.1"
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
   cd "C:\..\..\Desktop\majinnosumu_tower_visual_novel_game-ver-3.1\src"
   ```

   - フォルダに移動後、以下のコマンドでゲームを起動します。  
   ```shell
   python main.py
   ```

5. **コードエディターでの実行**  
   一部のコードエディター（VSCなど）では、直接ファイルを実行することが可能です。  
     
---

## `voice` チャンネルについて

- 音量調整部分は、コメントアウトで非表示にしてあります。`voice` チャンネルを使用する際は、音量調整を有効にするためにコメントアウトを解除してください。
- `voice` を使用する際は、音源ファイルを `asset` フォルダ内の `voice` フォルダに移動し、他の音源フラグと同様に JSON ファイル内で "voice" フラグを使って参照してください。

---

このソースコードでは、**PyInstaller**を使用してPythonスクリプトを単一の実行ファイルに変換して使用することができました。  
この手順を実施することで、Python環境をインストールしていない環境でもゲームを実行できるようになります。配布にも適した形に仕上げることが可能です。  

### ディレクトリ構成の例

以下のようなディレクトリ構成を推奨します：

```
プロジェクトフォルダ/
├── assets/          <- ゲームデータ（画像、音声ファイルなど）
├── src/             <- ソースコード（main.pyなど）
└── icon.ico         <- アイコン画像（任意）
```

---

### 必要なライブラリのインストール

1. **依存ライブラリのインストール**  
   `requirements.txt` を使用して以下のコマンドでインストールします：

   ```shell
   pip install -r requirements.txt
   ```

   もしくは、個別に以下のコマンドを実行してください：

   - Pillowのインストール  
     ```shell
     pip install Pillow
     ```

   - Pygameのインストール  
     ```shell
     pip install pygame
     ```

2. **PyInstallerのインストール**  
   実行ファイル作成に必要なPyInstallerをインストールします：

   ```shell
   pip install pyinstaller
   ```

---

### 実行ファイルの作成方法

1. **プロジェクトフォルダに移動する**  
   コマンドプロンプトまたはターミナルで、プロジェクトフォルダに移動します：

   ```shell
   cd <プロジェクトフォルダのパス>
   ```

   **例**: デスクトップにフォルダがある場合  
   ```shell
   cd C:\Users\<ユーザー名>\Desktop\majinnosumu_tower
   ```

2. **実行ファイルの作成**  
   以下のコマンドを実行します：

   ```shell
   pyinstaller --onefile --noconsole --add-data "assets;assets" --icon=icon.ico --name="majinnosumu_tower-ver.3.1" src/main.py
   ```

---

### オプションの詳細説明

- **`--onefile`**: すべてのファイルを1つの実行ファイルにまとめます。  
- **`--noconsole`**: コンソールウィンドウを非表示にします（ゲームでは不要な場合が多いです）。  
- **`--add-data "assets;assets"`**: 必要なデータフォルダ（`assets`）を含めます。  
  ※ Windowsではセミコロン（`;`）、Mac/Linuxではコロン（`:`）を使用してください。  
- **`--icon=icon.ico`**: 実行ファイルにアイコンを設定します。必要に応じてパスを変更してください。  
- **`--name="majinnosumu_tower-ver.3.1"`**: 実行ファイルの名前を指定します（任意の名前に変更可能）。  

---

### 実行ファイルの確認

PyInstallerが成功すると、以下のようなディレクトリ構成が作成されます：

```
プロジェクトフォルダ/
├── build/           <- 一時ファイル（削除してOK）
├── dist/            <- 実行ファイルが保存されるフォルダ
│   └── majinnosumu_tower-ver.3.1.exe
├── src/             <- ソースコード
├── assets/          <- ゲームデータ
├── icon.ico         <- アイコン画像
└── *.spec           <- PyInstallerの設定ファイル（削除してOK）
```
実行ファイルは`dist`フォルダ内に出力されます。  
`dist`フォルダ内に作成された実行ファイル（例: `majinnosumu_tower-ver.3.1.exe`）を使用して、ゲームを実行できます。  
生成された実行ファイルは、Python環境を必要とせずに動作し、配布にも適した形になっています。distフォルダ内に作成された実行ファイルをそのまま配布するだけで、他のユーザーがゲームをプレイできるようになります。

---

### 注意事項

- **セキュリティに関する注意**  
  PyInstallerはスクリプトを実行ファイルにまとめるだけのツールであり、コードの暗号化や高度な保護機能を提供するものではありません。  
  そのため、悪意のあるユーザーが実行ファイルを解析し、コードやデータを取得する可能性があります。セキュリティが重要なプロジェクトで使用する場合は、追加の保護手段を検討してください。  
- **OSに応じた調整**  
　MacやLinux環境で作成する場合、`--add-data` オプションのセパレータやアイコン指定の書式が異なる可能性があるようです。  
  詳細は[PyInstaller公式ドキュメント](https://pyinstaller.org)をご確認ください。  
  実行ファイル化において発生した問題は、PyInstallerのログを確認してください。  

- **ライセンスとクレジットに関する注意**   
    **推奨事項**  
     PyInstallerのライセンスはGPLv2（GNU General Public License Version 2）ですが、例外的に商用利用や非GPLプロジェクトでの利用を許可するための追加条項（特別例外）が含まれています。  
     実行ファイルを配布するだけであれば、PyInstallerの特別例外が適用されるため、GPLv2ライセンスの条件に従う必要はないようです。
     ライセンス条件ではありませんが、プロジェクトの信頼性を高めるため、READMEやクレジットに「PyInstallerを使用して実行ファイルを作成した」旨を記載することを推奨します。  

    **PyInstallerのライセンスが必要な場合**  
     PyInstallerのコードをそのまま再配布する場合、もしくは改変して再利用する場合は、GPLv2ライセンスに従う必要があります。  
     この場合、以下を実施してください：  
      - PyInstallerのライセンス文を同梱する。  
      - ソースコードを同梱するか、ソースコードへのアクセス手段を提供する。  
    **詳細情報**  
     PyInstallerのライセンスについて詳しく知りたい場合は、[公式リポジトリのLICENSEファイル](https://github.com/pyinstaller/pyinstaller/blob/develop/COPYING.txt)をご参照ください。  

---

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

