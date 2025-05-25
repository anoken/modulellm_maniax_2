#!/bin/bash

curl -X POST "http://localhost:8000/v1/chat/completions" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "qwen2.5-0.5B-p256-ax630c",
    "messages": [{"role": "user", "content": "あなたはどのようなAIモデルですか？"}],
    "temperature": 0.7
  }'