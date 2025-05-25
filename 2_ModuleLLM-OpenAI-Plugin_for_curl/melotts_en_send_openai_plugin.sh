#!/bin/bash

 curl -X POST "http://localhost:8000/v1/audio/speech" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "melotts-en-us",
    "input": "Hello, how are you today?",
    "voice": "alloy",
    "response_format": "mp3"
  }' \
  -o hello.mp3

