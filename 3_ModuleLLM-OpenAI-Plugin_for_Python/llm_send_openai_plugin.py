#!/usr/bin/env python3
# Copyright (c) 2025 aNoken

import requests  # HTTPリクエストを送るためのライブラリ
import json      # JSONデータの整形・表示用

# LLM（大規模言語モデル）に問い合わせる関数
def query_llm(message="Hello!",
              model="qwen2.5-0.5B-p256-ax630c",
              temperature=0.7,
              server_url="http://localhost:8000"):
    
    data = {
        "model": model,
        "messages": [{"role": "user", "content": message}],
        "temperature": temperature
    }
    
    # リクエストヘッダー（認証情報など）
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer YOUR_KEY"  
    }
    
    # POSTリクエストを送信して、モデルに問い合わせる
    response = requests.post(f"{server_url}/v1/chat/completions",
                             headers=headers,
                             json=data)
    
    # 応答をJSON形式で返す
    return response.json()

# 実行ブロック
if __name__ == "__main__":
    # モデルに問い合わせて結果を取得
    result = query_llm(message="あなたはどのようなAIモデルですか",
                       model="qwen2.5-0.5B-p256-ax630c",
                       server_url="http://localhost:8000")
    
    # 結果を表示
    print(json.dumps(result, indent=2, ensure_ascii=False))
