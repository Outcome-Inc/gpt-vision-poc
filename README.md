# 画像タグ付与ツール

このPythonスクリプトは、OpenAIのAPIを使用して画像に自動的にタグを付与するツールです。ローカル画像ファイルまたは画像URLを入力として処理できます。

## 🚀 **機能**
- ローカル画像ファイルまたはURLから画像を処理
- OpenAI GPT-4o-miniモデルを使用必要であれば他のモデルに変更する(ハードコード)
- 自動的に#顔貌写真,#真顔,#笑顔,#口腔内写真,#正面,#右側,#左側,#上顎,#下顎,#CT写真,#パノラマ写真のタグを付与(ハードコード)
- フォルダ内の複数の画像も一括処理可能

---

## 📦 **インストール**

1. **Pythonのインストール（3.7以上推奨）**

2. **必要なライブラリのインストール**
```bash
pip install openai
```

3. **OpenAI APIキーの設定**
```bash
export OPENAI_API_KEY=your_api_key_here  # Linux/macOS
# または
set OPENAI_API_KEY=your_api_key_here     # Windows
```

---

## 🖼️ **使い方**

### 1️⃣ **単一の画像ファイルを処理する場合**
```bash
python tag_image.py ./path/to/image.jpg
```

### 2️⃣ **画像URLを処理する場合**
```bash
python tag_image.py https://example.com/image.jpg
```

### 3️⃣ **フォルダ内の全ての画像を一括処理する場合**
```bash
python tag_image.py ./path/to/folder
```
リポジトリに含まれるtestフォルダの写真でテストも可能です。
```bash
python tag_image.py ./test-images/
```
#### 🔍 **サンプル画像のテスト結果**
<figure>
  <img src="https://github.com/user-attachments/assets/e291d01b-c1d6-4912-961d-c602f12e5883" alt="Image" width="35%" />
  <figcaption>img1</figcaption>
</figure>

<figure>
  <img src="https://github.com/user-attachments/assets/1d467551-34f6-4853-9f8e-6ff914da5ceb" alt="Image" width="35%" />
  <figcaption>img2</figcaption>
</figure>

<figure>
  <img src="https://github.com/user-attachments/assets/ae60dbaf-830a-4432-8e73-690b0e317c6a" alt="Image" width="35%" />
  <figcaption>img3</figcaption>
</figure>

<figure>
  <img src="https://github.com/user-attachments/assets/0faaf4a1-6e44-4acd-be94-f28395e491bb" alt="Image" width="35%" />
  <figcaption>img4</figcaption>
</figure>

<figure>
  <img src="https://github.com/user-attachments/assets/c29b5038-1819-4b3f-923a-7fd44864aefe" alt="Image" width="35%" />
  <figcaption>img5</figcaption>
</figure>

<figure>
  <img src="https://github.com/user-attachments/assets/b0fee161-e6b3-4b09-b9c6-646d97a138c7" alt="Image" width="35%" />
  <figcaption>img6</figcaption>
</figure>

<figure>
  <img src="https://github.com/user-attachments/assets/01eed552-7ab2-401f-9ac6-b33541378cc0" alt="Image" width="35%" />
  <figcaption>img7</figcaption>
</figure>

<figure>
  <img src="https://github.com/user-attachments/assets/5f5161c5-4f54-4c5a-9c53-d374960f72b1" alt="Image" width="35%" />
  <figcaption>img8</figcaption>
</figure>

モデル4o-mini結果
```bash
~/Development/openai 20s
❯ python brace-tag-image.py ./test-images
![img8](./test/img8.jpeg)
処理中: ./test/img8.jpeg
付与されたタグ: この画像に該当するタグは以下です：
- #顔貌写真
- #真顔
- #正面
![img5](./test/img5.jpeg)
処理中: ./test/img5.png
付与されたタグ: 該当するタグは次の通りです:
- #口腔内写真
- #下顎

処理中: ./test/img4.png
付与されたタグ: 該当するタグは以下の通りです：
- #口腔内写真
- #上顎
- #下顎

処理中: ./test/img3.png
付与されたタグ: 該当するタグは以下です：
- #口腔内写真
- #左側
- #右側
- #下顎

処理中: ./test/img2.png
付与されたタグ: この画像から選ばれるタグは以下の通りです：
- #口腔内写真
- #正面
- #上顎
- #下顎

他のタグは該当しません。

処理中: ./test/img1.png
付与されたタグ: 該当するタグは以下です：
- #口腔内写真
- #正面
- #下顎

処理中: ./test/img6.jpeg
付与されたタグ: 該当するタグは次の通りです：
- #顔貌写真
- #真顔
- #正面
- #右側
- #左側

処理中: ./test/img7.jpeg
付与されたタグ: 該当するタグは以下です：
- #顔貌写真
- #真顔
- #笑顔
- #正面
```

---

## ⚙️ **対応画像形式**
- `.png`, `.jpg`, `.jpeg`, `.bmp`, `.gif`, `.webp`


## 📝 **出力例**
```bash
処理中: ./test/img7.jpeg
付与されたタグ: #自然, #動物
```

---

## 💡 **コードの概要**

- **Base64エンコード:** ローカルファイルはBase64形式に変換してAPIへ送信。
- **API呼び出し:** `client.chat.completions.create`を使用。
- **エラー処理:** APIキー未設定時やAPIエラー発生時は適切なメッセージを表示。

---

## ❗ **注意事項**
- **API使用料:** OpenAI APIは有料です。料金は[OpenAI公式サイト](https://openai.com/pricing)を参照してください。
- **API制限:** APIの使用回数や速度に制限がある場合があります。

---

## 🛠️ **トラブルシューティング**

- **エラー: `OPENAI_API_KEY が環境変数に設定されていません`**
  - → APIキーが正しく設定されているか確認してください。

- **エラー: `InvalidRequestError`**
  - → 画像形式がサポートされているか、APIキーが正しいか確認してください。


---

## 📜 **ライセンス**
MIT License

---

## 🙏 **Author**
Outcome, Ken Nishimoto

