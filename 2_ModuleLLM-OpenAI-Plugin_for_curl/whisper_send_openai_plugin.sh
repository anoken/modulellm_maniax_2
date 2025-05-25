#!/bin/bash

curl -X POST "http://localhost:8000/v1/audio/transcriptions" \
  -F "file=@test_whisper.wav" \
  -F "model=whisper-tiny" \
  -F "language=ja"