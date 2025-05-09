
---

# 魔人の棲む塔_visual-novel-game ver-5.0

A visual novel game project  
コード作成、シナリオ作成、テキスト作成、画像生成に OpenAIの対話型AI「ChatGPT」を使用しています。  
このブランチでは、ゲームの**ソースコード**を記載しています。  
ゲームファイル(実行ファイル)のダウンロードは[こちら](https://github.com/AglaoDev-jp/majinnosumu_tower/releases/download/version-5.0/majinnosumu_tower_v.5.0.zip)  
ゲームプレイ(実行ファイル)のREADMEは[こちら](./README_Game.md)

---

本プロジェクトの制作にあたり、OpenAIの対話型AI「ChatGPT」のサポートを受けて、画像生成、アイデア出し、コード修正、文章の表現の改善、翻訳などをスムーズに行うことができました。開発に携わったすべての研究者、開発者、関係者の皆様に、心より感謝申し上げます。    

---

## ゲームファイル(実行ファイル)のセキュリティに関する注意事項
本ソフトウェアは、**悪意のあるコード（ウイルス・マルウェア）は含まれていません。**  
しかし、一部のアンチウイルスソフト（Norton,Avast,AVG,SecureAge,Zillya など）により、**誤検出**されることがあります。  
これはファイルサイズや圧縮方法による影響であり、悪意のある動作はありません。  

### ** 誤検出が起こる理由**
- **ファイルサイズが大きいこと**
- **圧縮やパッキング処理を行っていること**
- **デジタル署名がないこと**

これらの要因により、一部のウイルス対策ソフトが誤って「疑わしい」と判断することがあります。  

### **安全性を確認する方法**
本ソフトウェアが安全かどうかを確認する場合は、以下の方法を推奨します：
- **[VirusTotal](https://www.virustotal.com/)にアップロードし、スキャン結果を確認する** 
- **仮想環境（VirtualBox, Windows Sandbox など）で実行してみる**
- **公式の配布元（GitHub）からダウンロードする**

### **※誤検出が気になる場合や、安全性に不安がある場合は、ダウンロードや実行を控えてください。**

---

## 免責事項
本ゲームの利用や環境設定によるいかなる損害や問題について、作者は一切の責任を負いかねます。  

---

**製作期間**

- **ver-1.0**: 2024年6月 ~ 2024年9月中旬
- **ver-2.0**: 2024年10月31日 ~ 2024年11月11日  
- **ver-3.0**: 2024年11月11日 ~ 2024年11月23日
- **ver-4.0**: 2024年11月23日 ~ 2024年11月28日
- **ver-5.0**: 2024年11月28日 ~ 2024年12月29日

※ このリポジトリは個人学習のために使用しています。そのため、プルリクエスト（Pull Request）は、お受けすることができません。ご了承ください。  

---

## 使用言語とライブラリ

### 使用言語
- **Python 3.12.5**

### 使用ライブラリ
#### 標準ライブラリ
- **Tkinter** - GUI（グラフィカルユーザーインターフェース）を作成するための標準ライブラリ
- **json** - シナリオ、ゲームデータの管理
- **os** - OS操作関連の処理
- **sys** - 実行環境やコマンドライン引数の管理、PyInstallerでの凍結状態の判定
- **io** - バイナリデータの操作を行うための標準ライブラリ

#### 外部ライブラリ
- **Pillow (Python Imaging Library)** - 画像処理
- **Pygame** - サウンドの追加
- **cryptography** - データの暗号化・復号化（ver-5.0より追加）

### 難読化
- **Cython（ver-5.0より追加）**

### 実行ファイル化
- **PyInstaller**

### 使用エディター
- **Visual Studio Code (VSC)**  

---

### 著作権表示とライセンス
  可能な限り調べましたが、コピーライト表記などはっきりしないものも多くありました。間違いがなければいいのですが…  

### **Python**  
- © Python Software Foundation  
Licensed under the Python Software Foundation License (PSF License).  
[Python license](https://docs.python.org/3/license.html)  
- またはフォルダ内の [LICENSE-PSF.txt](./licenses/LICENSE-PSF.txt) をご確認ください。  
※ コードのみであればライセンス添付は不要ですが、PyInstallerを使って実行ファイル化する際にはPythonのライセンス（PSF License）の添付が必要です。  
   (内部にPythonの一部が組み込まれるため)
※ Python 3.8.6以降、PSF LicenseとZero-Clause BSDライセンスのデュアルライセンスとなっていますが、
  これはドキュメント内のコード例やレシピ、その他のコードを使用する場合に必要となるようです。  
  通常の使用であれば PSF License のみで大丈夫みたいです。

#### **Tkinter**  
- © Regents of the University of California, Sun Microsystems, Inc., Scriptics Corporation, and other parties  
TkinterはPythonに含まれるGUIライブラリですが、その動作にはTcl/Tkが使用されています。  
- [Tcl/Tk License](https://www.tcl.tk/software/tcltk/license.html)  
- またはフォルダ内の [LICENSE-TclTk.txt](./licenses/third_party/LICENSE-TclTk.txt) をご確認ください。

---

### このプロジェクトでは、以下のオープンソースライブラリを使用しています：

#### **Pillow**  
The Python Imaging Library (PIL)  
- © 1997 by Secret Labs AB  
- © 1995 by Fredrik Lundh and Contributors  
Pillow is the friendly PIL fork. It is  
- © 2010 by Jeffrey A. Clark and contributors  
 
Pillow is licensed under the MIT-CMU License.  
MIT-CMU License は、MIT License をベースにしたシンプルで柔軟なライセンスですが、以下のような特徴があります：  
- **著作権表示とライセンス文を必ず含める必要があります。**  
- **カーネギーメロン大学 (CMU) の名前やロゴを無断で使用することは禁止されています。**  
- 特定の文脈（CMUに関連するプロジェクトやソフトウェア）で主に使われるライセンスです。

> ※ 過去のバージョンでは、`pip show` などで Historical Permission Notice and Disclaimer (HPND) License が表示されることがあるようです。これは、古いバージョンに残っているメタデータによるもののようです（実際、私の環境でも確認できました）。
 
- [Pillow License](https://github.com/python-pillow/Pillow/blob/main/LICENSE)  
- またはプロジェクト内の [LICENSE-Pillow.txt](./licenses/third_party/LICENSE-Pillow.txt)  
※ Pillowの公式ドキュメントによれば、「Only use start year in copyright, remove end years（コピーライトには開始年のみ記載し、終了年は不要）」とありますので、開始年の記載だけで問題はなさそうです。

#### **Pygame**
- © 2000-2024 Pygame developers  

Pygameは、**GNU Lesser General Public License (LGPL)** の下でライセンスされています。  
このライセンスでは、以下の条件を満たす必要があります：  
- **ライセンス文を配布物に含めること。**  
- **ライブラリを改変した場合、その改変部分のソースコードを公開すること。**

### **PyInstallerを使った場合の対応**
- PyInstallerを使用してPygameをバンドルした場合でも、LGPLライセンスの条件を満たしています。  
  - ライブラリは動的リンクとして扱われます。
  - アプリケーションのソースコードを公開する義務はありません。
- ただし、以下の対応を行う必要があります：  
  - ライセンス文（LGPL.txt）を配布パッケージに含める。  
  - Pygameを改変した場合、その改変部分のソースコードを公開する。  

詳細なライセンス条項については、以下を参照してください：  
- [Pygame License](https://github.com/pygame/pygame/blob/main/docs/LGPL.txt)  
- プロジェクト内の [LGPL.txt](./licenses/third_party/LGPL.txt)  

> **備考:** PyInstallerでバンドルされた場合、ユーザーがライブラリを差し替える権利は担保されています。そのため、アプリケーション全体をオープンソースにする必要はありません。
### 静的リンクとの違い  
### **LGPLの基本ルール**
- 動的リンクが原則

  LGPLライセンスでは、ライブラリをアプリケーションに「動的リンク」することが前提です。  
  動的リンクとは、実行時にライブラリを別ファイルとして参照する方法を指します（例: .dll, .so）  
  LGPLライセンスでは、Pygameをリンクしているアプリケーションのソースコードを公開する必要はありません。  
  ただし、利用者がライブラリを差し替えられる仕組みを提供する必要があります。  

  Pygameを「静的リンク」してアプリケーションに組み込んだ場合、LGPLライセンスの適用範囲が広がり、  
  アプリケーション全体にLGPLが適用される可能性があります。  

- 静的リンク
  - 静的リンクでは、ライブラリのコードがアプリケーションのバイナリに直接埋め込まれるため、ライブラリの差し替えができなくなります。  
  この場合、アプリケーション全体がLGPLの影響を受ける可能性があります。

- 動的リンク（PyInstallerのケース）
  - PyInstallerはライブラリを個別のモジュールとして扱うため、実行時に動的にロードされます。
  この形式は、技術的にはPyInstallerで作成された実行ファイルの依存ライブラリ（例: Pygameの.dllファイル）を他のバージョンや改変版に置き換えることが可能です。  
  このため、アプリケーションがクローズドソースでも配布が可能のようです。　　

※ 明確なコピーライトを見つけることができませんでした。
  
---

#### **cryptography**  
- Copyright (c) 2013-2024, The cryptography developers. All rights reserved.  
このプロジェクトでは、音源データの暗号化・復号化に`cryptography`ライブラリを使用しています。  
このライブラリは以下のライセンスに基づき配布されています：  
- Apache License 2.0  
- 一部コンポーネントはBSDライセンス（3-Clause License）  

また、`cryptography`ライブラリのバックエンドとしてOpenSSLが使用されており、バージョンによりライセンスが異なります：  

- **OpenSSL 3.0以降**：Apache License 2.0  
- **OpenSSL 3.0未満**（1.1.1やそれ以前）：OpenSSL License および SSLeay License のデュアルライセンス  

現在使用しているバージョンは以下の通りです：  
**OpenSSL 3.4.0 22 Oct 2024**  
このバージョンは**Apache License 2.0**に基づいて配布されています。
- Copyright (c) 1998-2024 The OpenSSL Project Authors  
- Copyright (c) 1995-1998 Eric A. Young, Tim J. Hudson  
- All rights reserved.  
※ All rights reserved.と書かれているものは、著作権者がすべての権利を保有していることを示す表現なんだそうです。  
  
詳しくは以下をご確認ください：  
- [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0)  
- プロジェクト内のライセンスファイル：  
  - [LICENSE.APACHE.txt](./licenses/third_party/LICENSE.APACHE)  
  - [LICENSE.BSD.txt](./licenses/third_party/LICENSE.BSD)  
  - [LICENSE.OPENSSL.txt](./licenses/third_party/LICENSE.OPENSSL.txt)  

**注意**:  
このソースコード(ソフトウェア)は、日本国内での使用を想定しています。  
国外配布を行う場合、該当国の暗号化技術に関する規制をご確認ください。  
暗号化技術は輸出規制や各国の法律の対象となる場合があります。  
特に、他国への配布時は適切な手続きが必要です。  

---
#### **Cython** 
このプロジェクトの実行ファイルは、Cythonを使用して難読化を行っています。  
- Cython © 2007-2023 The Cython Project Developers  
- Licensed under the Apache License 2.0.  
- [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0)  

#### **PyInstaller**  
このプロジェクトは、**PyInstaller** を使用して実行ファイル化に対応しています。  
PyInstaller は GNU GPL ライセンスですが、例外規定により  
**生成される実行ファイル自体は GPL の制約を受けません**。

- **著作権表示：**  
  ```
  Copyright (c) 2010–2023, PyInstaller Development Team  
  Copyright (c) 2005–2009, Giovanni Bajo  
  Based on previous work under copyright (c) 2002 McMillan Enterprises, Inc.
  ```

#### ⚖️ PyInstaller のライセンス構成について

PyInstaller は以下のように**複数のライセンス形態**で構成されています：

- 🔹 **GNU GPL v2 or later（例外付き）**  
  本体およびブートローダに適用されます。  
  → **生成された実行ファイルは任意のライセンスで配布可能**です（依存ライブラリに従う限り）。

- 🔹 **Apache License 2.0**  
  ランタイムフック（`./PyInstaller/hooks/rthooks/`）に適用されています。  
  → 他プロジェクトとの連携や再利用を意識した柔軟なライセンス。

- 🔹 **MIT License**  
  一部のサブモジュール（`PyInstaller.isolated/`）およびそのテストコードに適用。  
  → 再利用を目的としたサブパッケージに限定適用されています。  

####  詳細情報へのリンク

- [PyInstallerのライセンス文書（GitHub）](https://github.com/pyinstaller/pyinstaller/blob/develop/COPYING.txt)  
- [PyInstaller公式サイト](https://pyinstaller.org/en/v6.13.0/index.html)  

---

## フォントについて

このゲームでは、"Noto Sans JP"フォントファミリー（NotoSansJP-Regular.otf, NotoSansJP-Bold.otf, NotoSansJP-Black.otf）を使用しています。

- **Noto Sans JP**  
  - © 2014-2024 Google LLC  
  - SIL Open Font License, Version 1.1   

### **ライセンスの概要と必要な対応**
Noto Sans JPは、SIL Open Font License (OFL) Version 1.1に基づき、以下の条件で使用できます：

#### **許可される行為**
1. **自由な利用**: フォントは商用・非商用問わず自由に使用できます。
2. **改変および再配布**: 改変後のフォントを含むパッケージを再配布することができます。
3. **埋め込み**: PDFやアプリケーションなどにフォントを埋め込むことが可能です。

#### **義務と禁止事項**
1. **ライセンス文書の添付**:
   - フォントを再配布または改変する場合は、必ずOFLライセンス文書（例: `OFL.txt`）を添付してください。
2. **フォント名の変更**:
   - 改変後のフォントを再配布する場合、フォント名を変更する必要があります。
3. **販売の禁止**:
   - フォントファイル自体を販売することは禁止されています。ただし、フォントを使用したプロダクト（例: 印刷物、アプリ）は販売可能です。

#### **ゲームにおける対応**
- **クレジット表記**:
  - ゲームのクレジットやドキュメント内で、フォント名およびライセンス情報を明記してください。
  - 表記例:  
    ```plaintext
    "Font: Noto Sans JP © 2014-2024 Google LLC, licensed under SIL Open Font License, Version 1.1."
    ```
- **ライセンスファイルの同梱**:
  - `OFL.txt`をゲームパッケージの適切な場所（例: `licenses/third_party/`フォルダ）に含めてください。  

詳しくは以下をご確認ください：  
- [OFL.txt](./licenses/third_party/OFL.txt)  

---

これらのプロジェクトの開発者および貢献者の皆様に、心より感謝申し上げます。

---

## 音源について
ソースコードフォルダには、音楽や効果音の音源自体は含まれておりません。  
ゲームで使用する音楽と効果音は、以下の提供元サイトからダウンロードをお願いします。  
ご利用にあたっては、各提供元サイトの規約をよくお読みいただき、適切な利用をお願いします。  

- **フリーBGM DOVA-SYNDROME**  
- **効果音ラボ**  

使用した具体的な曲目や効果音は、以下のリストをご確認ください。    

### フリーBGM DOVA-SYNDROME  
- 「strange lullaby」 - shimtone  
- 「奇妙な話」 - Heitaro Ashibe  
- 「透明な亡霊」 - Heitaro Ashibe  
- 「発見」 - のる  
- 「静かな夜に」 - のる  
- 「怖い系リプレイ音」 - Causality Sound  
- 「ENEMY_ENCOUNTER」 - MagaMaga  
- 「プレリュード第2番「名前を入力してください」」 - 秦暁  

### 効果音ラボ   
- ギャアアアア！  
- オーラ1  
- ガラスが割れる1  
- ゴブリンの鳴き声1  
- ゴブリンの鳴き声2  
- ライオンの鳴き声1  
- 怪獣の足音  
- 崖崩れ  
- 岩にヒビが入る 
- 弓矢が刺さる  
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

---

これらの素晴らしい音源を提供してくださった制作者および貢献者の皆様に、心より感謝申し上げます。  

---

### ver.5.0の改善点
- 一部シナリオを修正しました。
- エンドクレジットを修正しました。
- 効果音を追加しました（弓矢が刺さる）
- 画像を追加しました。
- 画面左上アイコンをゲーム専用の物に変更しました。
- オープニング画面の`スタート`,`説明`にカーソルを移動すると文字の色が変わるようにしました。
- 選択肢の表示のタイミング調整を行いました。
- 選択肢の表示をフェードインするようにしました(正確には疑似フェードイン)
- 文字送りアニメーション(文末に矢印画像の点滅)を実装しました。
- jsonからの`arrow_icon`フラグで文字送りアニメーションの画像を変更できるようにしました(ページ送り用の対応)
- jsonからの`"auto_advance": true`フラグで、入力なしで次の行に進むように変更しました(改行用の対応)
- `cryptography`ライブラリを使用し、バイナリデータ化した音源を`cryptography`ライブラリを使用して対称鍵暗号（AES）による暗号化を行いました。
- `cryptography`ライブラリを使用して暗号化の鍵をさらに暗号化(マスターキー)しました。
- マスターキーをソースコードにハードコーディングしたうえで`Cython`による難読化を行いました。
- Cython化したmainスクリプト(.pydファイル)を起動するため、新たに作成した`dummy_script.py`から.pydファイルを**モジュールとして呼び出す**ロジックを構築しました。  
- 類似のゲームタイトルが既に存在していたため、ゲームタイトルを`魔人の棲む塔`に変更しました(すべてのバージョンを変更しました)

---

### 問題点
- 画像はフルスクリーン表示可能だが、テキストのサイズは変更されず、位置のみ調整される。
- 画像エフェクトが未実装。
- フラグによる音楽のフェードイン・フェードアウトが未実装。
- 行やセグメント単位でしか音楽や画像の変更ができない。
- 文字量が多いと画面外にはみ出す。
- テキストを途中で一時停止、再開する機能がない。
- すべて関数で書かれているため、コードが長くなっている。
- グローバル変数の使用が多い。
- 音源以外のクラック対策が未実装。

---

## ソースコードについて

ソースコードから起動するには、以下の手順に従ってください。
### ※ 制作に必要なツールを`dev_tools`フォルダにまとめてあります。[tools_guide](./dev_tools/tools_guide.md)
### ※ このソースコードで音源使用するには、音源をバイナリデータ化および暗号化が必要です。[audio_tools](./dev_tools/audio_tools/audio_conversion_guide.md)  
### ※ Cython化を行わなくても起動できます。  
### ※ 実行ファイル化の場合にはCython化を推奨します。[Cython化について](./Cython化について.md)  

1. **Pythonのインストール**  
   `.py`ファイルの実行には、Pythonがインストールされている環境が必要です。

2. **使用ライブラリのインストール**  
   使用ライブラリの内、外部ライブラリは別途インストールが必要です。`requirements.txt`ファイルを作成してありますので、以下の手順でインストールしてください。

   - コマンドラインインターフェース (CLI: ターミナル、コマンドプロンプト、PowerShellなど) を使用し、`cd`コマンドで`requirements.txt`ファイルのあるディレクトリに移動します。  
   例: `majinnosumu_tower-ver-5.0`フォルダを右クリックして「パスをコピー」、または`requirements.txt`ファイルを右クリックして「プロパティ」の「場所」をコピーなど。  
   
   ```shell
   # 例: デスクトップにフォルダがある場合 (パスはPC環境により異なります)
   cd "C:\..\..\Desktop\majinnosumu_tower-ver-5.0"
   ```

   - 次のコマンドで必要なライブラリが一括でインストールできます。
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

   cryptographyのインストール
   ```shell
   pip install cryptography
   ```

   PyInstallerのインストール
   ```shell
   pip install pyinstaller
   ```

3. **音源ファイルの配置**  
   1.`dev_tools`フォルダ内の`convert_to_binary.py`を使用して音源をバイナリデータに変換してください。  
   2.`generate_key.py`で暗号キーを作成してください。  
   3.作成した暗号キーを使用し`encrypt_audio.py`で音源を暗号化してください。  
   4.`generate_master_key.py`を使用して、暗号化用の鍵を暗号化するマスターキー`master.key`と暗号化されたキー`encrypted_secret.key`を作成してください。    
   5.暗号化した音源ファイルを`asset`フォルダ内の`encrypted_audio`フォルダに移動してください。  
   6.暗号化されたキー`encrypted_secret.key`を`src`フォルダ内に移動してください。  
   7.`master.key`の内容を、`key_obfuscator.py`を使用して難読化し、それをソースコード内`main.py`にハードコーディングしてください。  
   詳しくは[audio_tools](./dev_tools/audio_tools/audio_conversion_guide.md)を参照してください。  

   ※ 音源のリストは、フォルダ内にもあります  
   ※ ハードコーディングの場所はソースコード内のコメントアウトで記述しています。  
   ※ `sound_effects`フォルダは、今回使用していません。ソースコードのパス生成の記述を変更することで使用することも可能です。  
   ※ `voice`を使用する場合も同様にバイナリデータ化、暗号化を行ってください。`voice`音源は`voice`フォルダに入れてください。  

### `pygame.mixer.Sound`使用時の注意点:
- `pygame.mixer.Sound`は短い音声データ（主に効果音）を扱うことを想定した機能です。そのため、音楽データ全体をメモリ上に展開する形となり、大きな音声ファイルを使用するとメモリ使用量が増加する可能性があります。
- 長時間の音声再生には最適化されていないため、音質やパフォーマンスに影響が出る場合があります。

4. **ゲームの起動**  
   コマンドラインインターフェースを使用して、以下の手順でゲームを起動します。

   - `cd`コマンドで`src`フォルダ内にある`main.py`ファイルのディレクトリに移動します。  
   例: `src`フォルダを右クリックして「パスをコピー」、または`main.py`ファイルを右クリックして「プロパティ」の「場所」をコピーなど。  
   ```shell
   # 例: デスクトップにフォルダがある場合 (パスはPC環境により異なります)
   cd "C:\..\..\Desktop\majinnosumu_tower-ver-5.0\src"
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
- `voice` を使用する際は、音源ファイルを `asset` フォルダ内の `voice` フォルダに移動し、他の音源フラグと同様に JSON ファイル内で `"voice"` フラグを使って参照してください。

---

## PyInstallerによる実行ファイル化

このソースコードでは、**PyInstaller**を使用してPythonスクリプトを単一の実行ファイルに変換して使用することができました。  
この手順を実施することで、Python環境をインストールしていない環境でもゲームを実行できるようになります。配布にも適した形に仕上げることが可能です。  
以下に手順を示します：  
### ※ 実行ファイル化の場合にはCython化を推奨します。[Cython化について](./Cython化について.md)  

### ディレクトリ構成の例

以下のようなディレクトリ構成を推奨します：  

```

プロジェクトフォルダ/
├── assets/               
│   ├── encrypted_audio/  <- (バイナリデータ化、暗号化した音源)  
│   ├── fonts/ 
│   ├── images/ 
│   ├── scenario/ 
│   └── voice/            <- (voiceを使用する場合もバイナリデータ化、暗号化が必要です) 
│    
├── src/                                
│    ├── encrypted_secret.key <- 音源複合化のためのキー
│    └── main.cp312-win_amd64.pyd  <- Cython化したmainスクリプト
│
├── icon.ico              <- アイコン画像（任意）
└── dummy_script.py       <- 起動用のスクリプト

# 事前に音源のバイナリデータ化、暗号化、`main.py`のCython化(main.cp312-win_amd64.pyd)を行ってください。
# 暗号化の元になったデータ(音源、バイナリ音源、secret.key、master.key)を、ファルダ内に残さないようにしてください。
# `setup.py`、`main.pyもしくはmain.pyx`、`main.c`を、ファルダ内に残さないようにしてください。

```

---

### 必要なライブラリのインストール

1. **依存ライブラリのインストール**  
   インストールがまだの場合は`requirements.txt` を使用して以下のコマンドでインストールします：

   ```shell
   pip install -r requirements.txt
   ```

   もしくは、個別に以下のコマンドを実行してください：

   Pillowのインストール
   ```shell
   pip install Pillow
   ```

   Pygameのインストール
   ```shell
   pip install pygame
   ```

   cryptographyのインストール
   ```shell
   pip install cryptography
   ```

   cythonのインストール
   ```shell
   pip install cython
   ```
   
   PyInstallerのインストール
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
   cd C:\Users\<ユーザー名>\Desktop\majinnosumu_tower-ver-5.0
   ```

2. **実行ファイルの作成**  
   以下のコマンドを実行します：

   ```shell
   pyinstaller --onefile --noconsole --name="majinnosumu_tower_v.5.0" --add-data "assets:assets" --add-data "src:src" --add-data "assets/images/demon_tower.png:." --icon=icon.ico dummy_script.py
   ```

### オプションの詳細説明

- **`--onefile`**: すべてのファイルを1つの実行ファイルにまとめます。  
- **`--noconsole`**: コンソールウィンドウを非表示にします（デバックなどを行いたい場合にはこの記述を削除してください）  
- **`--name="majinnosumu_tower-ver-5.0"`**: 実行ファイルの名前を指定します（任意の名前に変更可能）
- **`--add-data "assets;assets"`**: 必要なデータフォルダ（`assets`）を含めます。  
  ※ Windowsではセミコロン（`;`）、Mac/Linuxではコロン（`:`）を使用してください。
  - Windows: `--add-data "assets;assets"`  
  - Mac/Linux: `--add-data "assets:assets"`
- **`--add-data "src:src"`**  
  ソースフォルダ（`src`）を含めます。
- **`--add-data "assets/images/demon_tower.png;."`**  
  個別のファイル（この場合は画像ファイル）を指定して実行ファイルに含めます。このファイルは、Tkinter画面の左上に表示される羽アイコンを変更するための画像です。任意の画像に変更可能です。
- **`--icon=icon.ico`**  
  実行ファイルのアイコンを設定します。アイコンファイルは必ず `.ico` フォーマットで用意する必要があります。このパスは、アイコンファイルの保存場所に応じて適宜変更してください。  
  例:  
  ```shell
  # プロジェクトフォルダ直下にアイコンファイルがある場合：  
   `--icon=icon.ico`

  # アイコンファイルが `assets/images/` ディレクトリ内にある場合：  
   `--icon=assets/images/icon.ico`
  ```

### 実行ファイルの確認

PyInstallerが成功すると、以下のようなディレクトリ構成が作成されます：

```
プロジェクトフォルダ/
├── build/           <- 一時ファイル（削除してOK）
├── dist/            <- 実行ファイルが保存されるフォルダ
│   └── majinnosumu_tower-ver-5.0.exe <- 出来上がった実行ファイル
├── src/             <- ソースコード
├── assets/          <- ゲームデータ
├── icon.ico         <- アイコン画像
├── *.spec           <- PyInstallerの設定ファイル（削除してOK）
└── dummy_script.py
```
実行ファイルは`dist`フォルダ内に出力されます。  
`dist`フォルダ内に作成された実行ファイル（例: `majinnosumu_tower-ver-5.0.exe`）を使用してゲームを実行できます。  
生成された実行ファイルは、Python環境を必要とせずに動作します。  
ひとつのシステムファイルにまとめられていますので、配布にも適した形になっています。  
distフォルダ内に作成された実行ファイルをそのまま配布するだけで、他のユーザーがゲームをプレイできるようになります。  

### 注意事項

- **セキュリティに関する注意**  
  PyInstallerはスクリプトを実行ファイルにまとめるだけのツールであり、コードの暗号化や高度な保護機能を提供するものではありません。  
  そのため、悪意のあるユーザーが実行ファイルを解析し、コードやデータを取得する可能性があります。  
  コードやデータなどにセキュリティが重要なプロジェクトで使用する場合は、追加の保護手段を検討してください。  

- **OSに応じた調整**  
  MacやLinux環境で作成する場合、`--add-data` オプションのセパレータやアイコン指定の書式が異なるようです。  
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

- **このゲームのコード 制作ツールのコード**: MIT License。詳細は[LICENSE-CODE](./licenses/game/LICENSE-CODE)ファイルを参照してください。
- **画像**: Creative Commons Attribution 4.0 (CC BY 4.0)。詳細は[LICENSE-IMAGES](./licenses/game/LICENSE-IMAGES)ファイルを参照してください。
- **シナリオ**: Creative Commons Attribution-ShareAlike 4.0 (CC BY-SA 4.0)。詳細は[LICENSE-SCENARIOS](./licenses/game/LICENSE-SCENARIOS)ファイルを参照してください。

## ライセンスの簡単な説明

- **このゲームのコード 制作ツールのコード**: （MIT License）
このゲームのコードと制作ツールのコードは、MITライセンスのもとで提供されています。自由に使用、改変、配布が可能ですが、著作権表示とライセンスの文言を含める必要があります。

- **画像**: （Creative Commons Attribution 4.0, CC BY 4.0）
このゲームの画像は、CC BY 4.0ライセンスのもとで提供されています。自由に使用、改変、配布が可能ですが、著作権者のクレジットを表示する必要があります。

- **シナリオ**:（Creative Commons Attribution-ShareAlike 4.0, CC BY-SA 4.0）
このゲームのシナリオは、CC BY-SA 4.0ライセンスのもとで提供されています。自由に使用、改変、配布が可能ですが、著作権者のクレジットを表示し、改変後も同じライセンス条件を適用する必要があります。

※これらの説明はライセンスの概要です。詳細な内容は各ライセンスの原文に準じます。

---

## クレジット表示のテンプレート（例）  

### コード
```plaintext
Code by AglaoDev-jp © 2024, licensed under the MIT License.
```

### 画像
```plaintext
Image by AglaoDev-jp © 2024, licensed under CC BY 4.0.
```

### シナリオ
```plaintext
Scenario by AglaoDev-jp © 2024, licensed under CC BY-SA 4.0.
```

---
#### ライセンスの理由
現在のAI生成コンテンツの状況を踏まえ、私は本作品を可能な限りオープンなライセンス設定になるように心がけました。  
問題がある場合、状況に応じてライセンスを適切に見直す予定です。  

このライセンス設定は、権利の独占を目的とするものではありません。明確なライセンスを設定することにより、パブリックドメイン化するリスクを避けつつ、自由な利用ができるように期待するものです。  
  
© 2024 AglaoDev-jp

