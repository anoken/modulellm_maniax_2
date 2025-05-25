#!/bin/bash

curl -X POST http://localhost:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{ 
    "model": "smolvlm-500M-ax630c",
    "messages": [
      {
        "role": "user",
        "content": [
          { "type": "text", "text": "What do you see in this image?" },
          { "type": "image_url",
"image_url": { "url": "data:image/jpeg;base64,'$(base64 -w 0 test_img.jpg)'" } }
        ]
      }
    ],
    "temperature": 0.2 
  }'

