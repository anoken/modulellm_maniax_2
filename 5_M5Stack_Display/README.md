# 第5章 M5Stackをディスプレイにしよう

このフォルダには、Module-LLMとM5Stack CoreS3SEデバイス間の通信を行うためのコードと設定ファイルが含まれています。

## 概要

Module-LLMにはディスプレイがついていませんが、このコードを使用することでM5Stack CoreS3SEディスプレイに動画を送信して表示することができます。UARTシリアル通信を使用して、Module-LLM（Linuxホスト）からM5Stackデバイスへ映像データをリアルタイムで転送します。

## フォルダ構成

このプロジェクトは以下のファイル構成になっています：

- `M5Stack_CoreS3SE_platformio/` - M5Stack側のコード（PlatformIO環境）
  - `platformio.ini` - PlatformIO設定ファイル
  - `src/main.cpp` - M5Stack側のメインプログラム（シリアル受信・表示）
- `Module-LLM/` - Module-LLM（Linuxホスト）側のコード
  - `video_send.py` - 動画ファイルをシリアル通信経由でM5Stackに送信するスクリプト

## 開発環境のセットアップ

### 1. M5Stack側（受信側）

M5Stack CoreS3SEの開発には[PlatformIO](https://platformio.org/)を使用します：

1. [VS Code](https://code.visualstudio.com/)と[PlatformIO拡張機能](https://marketplace.visualstudio.com/items?itemName=platformio.platformio-ide)をインストール
2. PlatformIOでプロジェクトを開く
3. `platformio.ini`の設定を確認（M5Stack CoreS3ボード、必要なライブラリ）
4. USBケーブルでM5Stack CoreS3SEを接続し、ビルド・アップロード


### 2. Module-LLM側（送信側）

Module-LLM上のLinux環境で必要なPythonライブラリをインストールします：

```bash
root@m5stack-LLM:~# pip install opencv-python pyserial
```

## ハードウェア接続

1. M5Stack CoreS3SEとModule-LLMをスタックすることで**Port-C**（UART）ピンのシリアルポートに接続
- M5Stack TXD → Module-LLM RXD
- M5Stack RXD → Module-LLM TXD



## 使用方法

### 1. M5Stack側のプログラム

1. PlatformIOでM5Stack_CoreS3SE_platformioプロジェクトを開く
2. コードをビルドしてM5Stack CoreS3SEにアップロード
3. M5Stack CoreS3SEが起動し、「UART Image Display Started」と表示されれば準備完了

### 2. Module-LLM側のスクリプト実行

1. M5Stackデバイスが適切に接続されていることを確認
2. 必要なライブラリがインストールされていることを確認
3. スクリプトを実行：

```bash
root@m5stack-LLM:~# python3 video_send.py
```

## 技術詳細

### M5Stack側のコード（main.cpp）

M5Stack側のコードは以下の機能を提供します：

- UARTシリアル通信（2Mbps）の初期化
- 受信データからヘッダー情報の解析
- JPEGデータの受信と表示
- エラーハンドリングとログ表示

UART通信は以下の設定で動作します：
- ポート: UART_NUM_2（M5Stack CoreS3SEのPort-C）
- ボーレート: 2,000,000 bps
- データビット: 8ビット
- パリティ: なし
- ストップビット: 1ビット

### Module-LLM側のスクリプト（video_send.py）

`video_send.py`スクリプトは以下の機能を提供します：

- 指定した動画ファイル（デフォルト: BadApple.mp4）を読み込み
- フレームを320x240サイズにリサイズ
- JPEG圧縮を適用
- シリアル通信を通じてM5Stackに送信
- 各フレームごとに適切なヘッダー情報を付加

## パラメータのカスタマイズ

`send_video_serial`関数では以下のパラメータを調整できます：

- `video_path` - 送信する動画ファイルのパス
- `serial_port` - 使用するシリアルポート（デフォルト: '/dev/ttyS1'）
- `baudrate` - 通信速度（デフォルト: 2000000）
- `quality` - JPEG圧縮の品質（デフォルト: 90）

例えば、別の動画ファイルを使用する場合：

```python
send_video_serial("your_video.mp4", "/dev/ttyS1", 2000000, 90)
```




