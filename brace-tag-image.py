import os
import sys
import base64
import concurrent.futures
from openai import OpenAI

# OpenAIクライアントの初期化
client = OpenAI()

# 環境変数からAPIキーを取得
api_key = os.getenv("OPENAI_API_KEY")
if api_key is None:
    print("エラー: OPENAI_API_KEY が環境変数に設定されていません。")
    sys.exit(1)

# 対応する画像拡張子
IMAGE_EXTENSIONS = ('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.webp')

# 画像をBase64エンコードする関数
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

# 画像にタグを付与する関数
def tag_image(image_path_or_url):
    try:
        if os.path.isfile(image_path_or_url):
            # ローカルファイルの場合はBase64エンコード
            base64_image = encode_image(image_path_or_url)
            image_content = {
                "type": "image_url",
                "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}
            }
        else:
            # URLの場合
            image_content = {
                "type": "image_url",
                "image_url": {"url": image_path_or_url}
            }

        # OpenAI APIへリクエスト
        response = client.chat.completions.create(
            # models: gpt-4o, gpt-4o-mini, gpt-4-turbo, o1 など
            model="gpt-4o",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": "この画像から該当するタグを選んでください: "
                                    "#顔貌写真,#真顔,#笑顔,#口腔内写真,#正面,"
                                    "#右側,#左側,#上顎,#下顎,#CT写真,#パノラマ写真"
                        },
                        image_content
                    ],
                }
            ],
            max_tokens=300,
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"エラー: {e}"

# フォルダ内の画像をパラレルに処理する関数
def process_folder_parallel(folder_path):
    # まず、対象となる画像ファイルのパス一覧を取得
    image_paths = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith(IMAGE_EXTENSIONS):
                image_paths.append(os.path.join(root, file))
    
    # ThreadPoolExecutor を利用して並列処理
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # 各画像の処理を submit して future オブジェクトの辞書を作成
        future_to_image = {executor.submit(tag_image, path): path for path in image_paths}
        for future in concurrent.futures.as_completed(future_to_image):
            image_path = future_to_image[future]
            try:
                tags = future.result()
            except Exception as exc:
                tags = f"生成エラー: {exc}"
            print(f"処理中: {image_path}")
            print(f"付与されたタグ: {tags}\n")

# メイン処理
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("使い方: python tag_image.py <画像ファイルパス | 画像URL | フォルダパス>")
        sys.exit(1)

    input_path = sys.argv[1]

    if os.path.isdir(input_path):
        process_folder_parallel(input_path)
    else:
        tags = tag_image(input_path)
        print(f"付与されたタグ: {tags}")
