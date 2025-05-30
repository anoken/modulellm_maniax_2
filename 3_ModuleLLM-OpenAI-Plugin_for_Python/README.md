# Module LLM OpenAI Plugin Python スクリプト

このフォルダには、Module LLM-StackFlowをOpenAI Pluginを使い、OpenAI API互換インターフェースを通じて呼び出すためのPythonスクリプトが含まれています。

## 概要

StackFlowはModule LLMでAIモデルを実行するためのフレームワークです。このフォルダ内のスクリプトは、OpenAI API互換エンドポイントを使用してModule LLMのさまざまな機能にアクセスするためのPythonサンプルを提供します。

## 含まれるスクリプト

- `llm_send_openai_plugin.py` - テキスト生成のためのLLMモデルにリクエストを送信
- `vlm_send_openai_plugin.py` - 画像認識と説明のためのVision Language Modelにリクエストを送信
- `whisper_tiny_openai_plugin.py` - 音声からテキストへの変換（Whisper互換）
- `melotts_en_openai_plugin.py` - テキストから音声への変換（英語）

## 前提条件

- Python 3.7以上
- requestsライブラリ（`pip install requests`）
- 実行中のModule LLMサーバー（デフォルトでは`http://localhost:8000`）

## サーバーのセットアップ

```bash
root@m5stack-LLM:~# wget -qO /etc/apt/keyrings/StackFlow.gpg https://repo.llm.m5stack.com/m5stack-apt-repo/key/StackFlow.gpg
root@m5stack-LLM:~# echo 'deb [arch=arm64 signed-by=/etc/apt/keyrings/StackFlow.gpg] https://repo.llm.m5stack.com/m5stack-apt-repo jammy ax630c' > /etc/apt/sources.list.d/StackFlow.list
```

```bash
root@m5stack-LLM:~# apt update
root@m5stack-LLM:~# apt install lib-llm
root@m5stack-LLM:~# apt install llm-sys llm-llm llm-vlm
root@m5stack-LLM:~# apt install llm-whisper llm-melotts 
root@m5stack-LLM:~# apt install llm-openai-api
```

## 使用方法

各スクリプトは単独で実行できます：

```bash
# テキスト生成の例
python3 llm_send_openai_plugin.py

# 画像認識の例
python3 vlm_send_openai_plugin.py
# テスト用のメディアファイルを使用します：
# `test_img.jpg` - VLMテスト画像

# 音声認識の例
python3 whisper_tiny_openai_plugin.py
# テスト用のメディアファイルを使用します：
# `test_whisper.wav` - 音声認識のためのテスト音声ファイル

# テキスト読み上げの例
python3 melotts_en_openai_plugin.py
# 出力ファイル: test_voice.mp3
```

## 各スクリプトの機能と引数

### llm_send_openai_plugin.py
テキスト生成のためのLLMリクエストを行います。
- `message`: 入力テキスト
- `model`: 使用するモデル名（デフォルト: "qwen2.5-0.5B-p256-ax630c"）
- `temperature`: 生成の多様性パラメータ（デフォルト: 0.7）
- `server_url`: Module LLMサーバーURL

### vlm_send_openai_plugin.py
画像と質問テキストを送信して、画像の内容を分析します。
- `image_path`: 画像ファイルのパス
- `prompt`: 画像に対する質問
- `model`: 使用するモデル名（デフォルト: "smolvlm-500M-ax630c"）
- `server_url`: Module LLMサーバーURL

### whisper_tiny_openai_plugin.py
音声ファイルをテキストに変換します。
- `file_path`: 音声ファイルのパス
- `model`: 使用するモデル名（デフォルト: "whisper-tiny"）
- `language`: 音声の言語（デフォルト: "ja"）

### melotts_en_openai_plugin.py
テキストを音声に変換します。
- `text`: 音声に変換するテキスト
- `model`: 使用するモデル名（デフォルト: "melotts-en-us"）
- `voice`: 音声のタイプ（デフォルト: "alloy"）
- `output_file`: 出力音声ファイルのパス（デフォルト: "test_voice.mp3"）

## カスタマイズ

各スクリプトの関数呼び出しの引数を変更することで、使用するモデルやパラメータをカスタマイズできます。

## 注意事項

- これらのスクリプトを実行するには、Module LLMサーバーが適切に設定され実行されている必要があります
