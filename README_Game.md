
---

# 魔人の棲む塔_visual-novel-game ver-5.0  
A visual novel game project  
コード作成、シナリオ作成、テキスト作成、画像生成にChatGPTを使用しています。  
こちらでは、実行ファイルの起動の仕方、ゲームの遊び方をメインに説明します。  

---

## 免責事項
本ゲームの利用や環境設定によるいかなる損害や問題について、作者は一切の責任を負いかねます。  

## 使用上の注意  
本ソフトウェアには以下の制限事項があります。利用者はこれを承諾した上で利用してください。  

1. **暗号化技術に関する法規制の遵守**  
   本ソフトウェアには、暗号化の為`cryptography`ライブラリが使用されています。再配布の際には、暗号化技術に関する輸出規制を含む法規制を遵守してください。  
2. **ライセンス条件の遵守**  
   **再配布を行う場合**は、ライブラリなどのライセンス条件に従ってください。  

---

### 注意事項  

- **セーブデータについて**  
  セーブデータは、実行ファイルと同じフォルダに作成されます。  
  実行ファイルやセーブフォルダを移動するとデータが共有されなくなりますので、必ず同じフォルダ内に配置してください。  
  また、ゲームを削除する時には実行ファイルを削除するだけでなく、セーブフォルダの削除も忘れずに行ってください。

- **セキュリティと禁止事項**  
  本ゲームの実行ファイルは、**PyInstaller** を使用して作成されています。  
  実行ファイルを逆アセンブル、逆コンパイル、リバースエンジニアリングなどを行い、内部のリソース（音源、画像、フォント、スクリプト、シナリオなど）を取り出す行為を**固く禁止**します。    
  ※コード、画像、シナリオは、オープンソースです。  
  ※本ゲームのフォントは、"Noto Sans JP"フォントファミリー (NotoSansJP-Regular.otf, NotoSansJP-Bold.otf, NotoSansJP-Black.otf) を使用しています。  
  > 使用音源については、フリー音源サイトから提供されているものを使用しています。もし必要であれば**必ず各サイトから正式な方法で入手してください。**

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

**誤検出が気になる場合や安全性に不安がある場合は、実行を控えてください。**

---

### このゲームの遊び方

本作は、テキストを読みながら選択肢を選び、ストーリーを進めていくノベルゲームです。  
選択肢によって物語が分岐し、エンディングが変化します。  
バッドエンドが多いため、**こまめなセーブを強くお勧めします**。


#### 起動方法  
1. フォルダ内にある`majinnosumu_tower-ver.5.0.exe` ファイルをダブルクリックするとゲームが始まります。  
2. 起動後、最初の画面では以下の操作が可能です：  
   - **`説明`** を左クリック → 遊び方の説明を表示します。  
   - **`スタート`** を左クリック → ゲームを開始します。  

#### 操作方法  
- **左クリック**：文字送り、選択肢や項目の選択  
- **右クリック**：セーブ/ロード、文字速度調整、音量調整  
- **F11**：フルスクリーン化（Esc または F11で解除）  
- **B キー**：画面を暗くする（背景が明るく文字が読みにくいときに使用してください）  

---

### ゲームの削除方法  

ゲームを削除するには、以下の手順でファイルを削除してください：  
1. **ゲームの保存先フォルダ**を開きます。  
2. フォルダ内の以下のファイルやフォルダを削除します：  
   - `majinnosumu_tower-ver.5.0.exe` （実行ファイル）  
   - 実行ファイルによって作成された `save` フォルダ  
---

## 使用音源について  

本ゲームで使用している音楽・効果音は、以下のフリー音源サイトから提供されています：  

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

これらの素晴らしい音源を提供してくださった制作者、および貢献者の皆様に心より感謝申し上げます。  

---

## クラック対策について

このゲームは基本的にオープンソースですが、音源についてはフリー音源サイトの音源を使用しています。  
そのため音源への不正なアクセスを防止するため、以下の対策を行っています。  

1. **PyInstallerによる実行ファイル化**  
   実行ファイル化することで、通常の方法では音源にアクセスできないようにしています。  
   この方法は、プログラミングに詳しくない方には十分有用であり、抑止効果が期待できます。  
   また、パッケージ化によってゲームとしての利便性も向上します。  
   **ただし注意点として**、専用ツールを使用することでパッケージ化されたファイルから元のコードを取り出される可能性があります。  
   Pythonやプログラミングに詳しい方には比較的容易に突破されてしまう恐れがあります。  
   そのため、この方法は「プログラミングに詳しくない人への対策」としての効果が主であり、完全な防御策とは言えません。  

2. **音源のバイナリデータ化**  
   音源をすべてバイナリデータに変換し、通常の音声形式に戻すには専用のスクリプトが必要な状態にしました。  
   音源の直接的な不正利用のハードルを上げることを目的に行いました。  
   また、音声形式に戻す変換による音質の劣化も避けられません。  
   **ただし注意点として**、解析者がバイナリデータの形式を解読できれば、元の音源に近い状態に復元される可能性があります。  
   この対策は「手間を増やす」効果が主であり、音源を完全に保護するものではありません。  

3. **`cryptography`ライブラリによる暗号化**  
   バイナリデータ化した音源を、`cryptography`ライブラリを使用してAESによる暗号化を行いました。  
   AESは非常に強力な暗号化方式であり、解読には膨大な計算資源と時間が必要です。  
   **ただし注意点として**、暗号鍵がソースコード内にハードコーディングされている場合、その鍵を解析されるリスクがあります。  
   このため、本来であれば暗号鍵を別途安全に管理する仕組みを併用することが理想的です。  

4. **Cythonによる難読化**  
   `cryptography`ライブラリを使用して作成したキーファイルをさらに`cryptography`ライブラリで暗号化、  
   そしてそのキーをソースコードにハードコーディングし、`Cython`でコンパイルすることでコードを難読化しました。  
   `Cython`はPythonコードをC言語に変換し、さらにネイティブコード（バイナリ）にコンパイルするため、以下の効果があります：  

   - **ソースコードが含まれない**  
     通常のPythonスクリプトとは異なり、元のコードがそのまま含まれないため、コードを直接閲覧することはできません。

   - **逆コンパイルが困難**  
     逆コンパイルを試みた場合でも得られるのはC言語やアセンブリコードであり、元のロジックを理解するには高度な技術と労力が必要です。

   - **ロジックの隠蔽**  
     暗号化キーやアルゴリズムの詳細が難読化されるため、単純なリバースエンジニアリングでは情報を特定することが難しくなります。

   **ただし注意点として**、Cythonでコンパイルされたバイナリも解析可能であり、高度な解析者には突破されるリスクがあります。  
   しかし、一般的なリバースエンジニアにとっては強力な抑止効果を持ち、解析の手間を増大させることができます。  

### まとめ
これらの対策は、音源の不正利用を完全に防ぐものではありません。しかし時間稼ぎや心理的な抑止効果を期待し行いました。  
意図をご理解いただき、正当に楽しんでもらえることを願っています。  

---

## 使用言語とライブラリ

### 使用言語
- **Python 3.12.5**

### 使用ライブラリ
#### 標準ライブラリ
- **Tkinter** - GUI（グラフィカルユーザーインターフェース）を作成するための標準ライブラリ
- **os** - OS操作関連の処理
- **json** - シナリオ、ゲームデータの管理
- **sys** - 実行環境やコマンドライン引数の管理、PyInstallerでの凍結状態の判定
- **io** - バイナリデータの操作を行うための標準ライブラリ

#### 外部ライブラリ
- **Pillow (Python Imaging Library)** - 画像処理
- **Pygame** - サウンドの追加
- **cryptography** - データの暗号化・復号化

### 難読化
- **Cython**  

### 実行ファイル化
- **PyInstaller**  

### 使用エディター
- **Visual Studio Code (VSC)**  

---

### 著作権表示とライセンス

### **Python**  
- © Python Software Foundation  
Licensed under the Python Software Foundation License (PSF License).  
[Python license](https://docs.python.org/3/license.html)  
- またはフォルダ内の [LICENSE-PSF.txt](./licenses/LICENSE-PSF.txt) をご確認ください。  
※ PyInstallerを使った実行ファイルには、Pythonのライセンス（PSF License）の添付が必要です。

#### **Tkinter**  
- © Regents of the University of California, Sun Microsystems, Inc., Scriptics Corporation, and other parties  
TkinterはPythonに含まれるGUIライブラリですが、その動作にはTcl/Tkが使用されています。  
- [Tcl/Tk License](https://www.tcl.tk/software/tcltk/license.html)  
- またはフォルダ内の [LICENSE-TclTk.txt](./licenses/third_party/LICENSE-TclTk.txt) をご確認ください。

---

### このプロジェクトでは、以下のオープンソースライブラリを使用しています：

#### **Pillow**  
The Python Imaging Library (PIL)  
- © 1997-2011 by Secret Labs AB  
- © 1995-2011 by Fredrik Lundh and Contributors  
Pillow is the friendly PIL fork. It is  
- © 2010-2024 by Jeffrey A. Clark and contributors  

Pillowは、MIT-CMU License の下でライセンスされています。  
詳しくは以下をご確認ください：  
- [Pillow License](https://github.com/python-pillow/Pillow/blob/main/LICENSE)  
- またはプロジェクト内の [LICENSE-Pillow.txt](./licenses/third_party/LICENSE-Pillow.txt)  

#### **Pygame**  
- © 2000-2024 Pygame developers  

Pygameは、GNU Lesser General Public License (LGPL) の下でライセンスされています。  
詳しくは以下をご確認ください：  
- [Pygame License](https://github.com/pygame/pygame/blob/main/docs/LGPL.txt)  
- またはプロジェクト内の [LGPL.txt](./licenses/third_party/LGPL.txt)  

---

#### **cryptography**  
Copyright (c) 2013-2024, The cryptography developers. All rights reserved.  
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

詳しくは以下をご確認ください：  
- [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0)  
- プロジェクト内のライセンスファイル：  
  - [LICENSE.APACHE.txt](./licenses/third_party/LICENSE.APACHE)  
  - [LICENSE.BSD.txt](./licenses/third_party/LICENSE.BSD)  
  - [LICENSE.OPENSSL.txt](./licenses/third_party/LICENSE.OPENSSL.txt)

---
#### **Cython** 
このプロジェクトの実行ファイルは、Cythonを使用して難読化を行っています。  
Cython © 2007-2023 The Cython Project Developers  
Licensed under the Apache License 2.0.  
- [Apache License 2.0](http://www.apache.org/licenses/LICENSE-2.0)  

#### **PyInstaller**  
このプロジェクトは、PyInstallerを使用して実行ファイル化に対応しています。  
PyInstallerはGNU General Public License (GPL) の下でライセンスされていますが、例外規定により、生成される実行ファイルはGPLの制約を受けません。  

詳しくは以下をご確認ください：  
- [PyInstaller公式ライセンス情報](https://github.com/pyinstaller/pyinstaller/blob/develop/COPYING.txt)  

---

## フォントについて

このゲームでは、"Noto Sans JP"フォントファミリー（NotoSansJP-Regular.otf, NotoSansJP-Bold.otf, NotoSansJP-Black.otf）を使用しています。

- **Noto Sans JP**  
  - © 2014-2024 Google LLC  
  - SIL Open Font License, Version 1.1   

詳しくは以下をご確認ください：  
- [OFL.txt](./licenses/third_party/OFL.txt)  


---

これらのプロジェクトの開発者および貢献者の皆様に、心より感謝申し上げます。

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

