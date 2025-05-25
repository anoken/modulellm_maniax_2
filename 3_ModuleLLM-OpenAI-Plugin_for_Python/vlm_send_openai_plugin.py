import requests
import json
import base64
import os

# 画像ファイルをBase64エンコードして文字列に変換
def image_to_base64(image_path):
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode('utf-8')

# 画像と言葉のプロンプトをVLMに送信して応答を得る関数
def query_vlm(image_path, prompt="What do you see in this image?",
              model="smolvlm-500M-ax630c", server_url="http://localhost:8000"):
    if not os.path.exists(image_path):
        return {"error": f"画像ファイル '{image_path}' が見つかりません"}

    base64_image = image_to_base64(image_path)
    
    data = {
        "model": model,
        "messages": [{
            "role": "user",
            "content": [
                {"type": "text", "text": prompt},
                {"type": "image_url",
                 "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}}
            ]
        }],
        "temperature": 0.2
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer YOUR_KEY"
    }

    response = requests.post(f"{server_url}/v1/chat/completions",
                             headers=headers, json=data)
    
    return response.json()

# 実行ブロック：画像とプロンプトでVLMに問い合わせ
if __name__ == "__main__":
    result = query_vlm("test_img.jpg", prompt="What do you see in this image?",
                       model="smolvlm-500M-ax630c", server_url="http://localhost:8000")
    print(json.dumps(result, indent=2, ensure_ascii=False))