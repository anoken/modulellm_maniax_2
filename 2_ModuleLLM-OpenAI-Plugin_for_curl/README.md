# Module LLM OpenAI Plugin Shell Scripts

このフォルダには、Module LLM-StackFlowをOpenAI Plugin を使い、OpenAI API互換インターフェースを通じて呼び出すためのcurlスクリプトが含まれています。

## 概要

StackFlowはModule LLMでAIモデルを実行するためのフレームワークです。このフォルダ内のスクリプトは、OpenAI API互換エンドポイントを使用してModule LLMのさまざまな機能にアクセスするためのサンプルを提供します。


## 含まれるスクリプト

- `llm_send_openai_plugin.sh` - テキスト生成のためのLLMモデルにリクエストを送信
- `vlm_send_openai_plugin.sh` - 画像認識と説明のためのVision Language Modelにリクエストを送信
- `whisper_send_openai_plugin.sh` - 音声からテキストへの変換（Whisper互換）
- `melotts_en_send_openai_plugin.sh` - テキストから音声への変換（英語）

## 使用方法

1. Module LLMサーバーが実行されていることを確認してください（デフォルトでは`http://localhost:8000`）

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


2. 任意のスクリプトを実行します：

```bash
# テキスト生成の例
./llm_send_openai_plugin.sh

# 画像認識の例
./vlm_send_openai_plugin.sh

# テスト用のメディアファイルを使用します：
# `test_img.jpg` - VLMテスト画像

# 音声認識の例
./whisper_send_openai_plugin.sh

# テキスト読み上げの例
./melotts_en_send_openai_plugin.sh

# テスト用のメディアファイルを使用します：
# `test_whisper.wav` - 音声認識のためのテスト音声ファイル

```

## カスタマイズ

各スクリプトはテキストエディタで編集することで、使用するモデルやパラメータをカスタマイズできます。リクエストのJSONボディ内で以下の項目を変更可能です：

- `model` - 使用するAIモデルの名前
- `messages` - 入力メッセージとロール
- `temperature` - 生成の多様性を制御するパラメータ（低いほど決定的）

## 注意事項

- これらのスクリプトを実行するには、Module LLMサーバーが適切に設定され実行されている必要があります
- 各スクリプトは実行権限が必要な場合があります。必要に応じて `chmod +x *.sh` を実行してください
