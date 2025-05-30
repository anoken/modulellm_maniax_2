# ModuleLLM_MAniaX Ⅱ

「ModuleLLM_MAniaX Ⅱ 」のサポートページです。<br>

![image](https://github.com/user-attachments/assets/ad730a38-efad-4238-ae96-7fe404b409cf)


## 紹介

### 書籍情報
タイトル： ModuleLLM_MAniaX Ⅱ <br>
著者： aNo研<br>
形式： A5サイズ・87ページ<br>
発行日： 2025年5月31日<br>

### 本書の内容

Module-LLMは、Module-LLM MAniaX第1巻の発行以降、M5StackとAXERAがツールの整備に取り組んでおり、より一層使いやすい環境が整いました。本書では、新しくリリースされた開発ツールの解説を行います。
また、筆者がModule-LLMを使っていく中で見出したテクニックやM5Stackの新商品に導入が企画されているAIチップAX650の情報などを盛り込んでいます。<br>


### 本リポジトリについて

このリポジトリには、本書で解説されているサンプルコードやスクリプトが含まれています。各ディレクトリは、書籍の各章に対応しています。本書と合わせてご利用ください。



## 改定履歴
・v1.0.0版発行: 2025年6月1日 本文87ページ<br>


## 本書の特徴

本書は、以下の特徴を持つModule-LLMの実践的ガイドです：

- **ModuleLLM-OpenAI-Pluginの解説**：最新のStackFlowを用いて、LLM、VLM、音声合成、音声認識などの機能を簡単に利用する方法を解説
- **Pythonでの実装例**：OpenAI-PluginをPythonから呼び出すコード例を紹介
- **Linuxカーネルビルドガイド**：Module-LLMのLinuxカーネルをカスタマイズしてビルドする方法を紹介
- **M5Stack連携**：M5Stack CoreS3SEをディスプレイとして活用する方法を解説
- **最新AIチップAX650N評価**：次世代AIチップAX650Nを先取り検証し、AX630Cとのパフォーマンス比較結果を公開
- 
## 目次<br>

## 第1章 Module-LLMの使い方<br>
1.1 Module-LLMとは？<br>
1.2 AXERA社とは？<br>
1.3 Module-LLMとModule13.2 LLM Mateの接続方法<br>
1.4 Module-LLMへのログイン方法<br>
1.5 起動音の消し方<br>

## 第2章 OpenAI-Pluginを使ってみよう<br>
2.1 概要<br>
2.2 StackFlowをインストールする<br>
2.3 LLM-Modelをインストールする<br>
2.4 LLMを呼び出す<br>
2.5 VLMをインストールする<br>
2.6 VLMを呼び出す<br>
2.7 MeloTTSを呼び出す<br>
2.8 MeloTTSのインストール<br>
2.9 MeloTTSで音声ファイルを生成する<br>
2.10 Whisperを呼び出す<br>
2.11 Whisperのインストール<br>
2.12 StackFlowのモデル一覧情報<br>

## 第3章 OpenAI-PluginをPythonで使う<br>
3.1 LLMをPythonから呼び出す<br>
3.2 VLMをPythonから呼び出す<br>
3.2.1 処理する画像の例<br>
3.3 MeloTTSをPythonから呼び出す<br>
3.4 WhisperをPythonから呼び出す<br>

## 第4章 Linuxカーネルをビルドしよう<br>
4.1 必要なパッケージのインストール<br>
4.2 ビルド環境の準備<br>
4.3 ビルドスクリプトについて<br>
4.4 ビルドスクリプトの修正<br>
4.5 ALSAマイク16Bit問題について<br>
4.6 ファームウェアの書き込みツール<br>
4.6.1 Python版AXDLツールでのファームウェア書込み<br>
4.6.2 udevルールのセットアップ<br>
4.6.3 Python環境のセットアップ<br>
4.7 参考文献<br>

## 第5章 M5Stackをディスプレイにしよう<br>
5.1 UART通信速度の理論値計算<br>
5.2 CoreS3 SEの開発環境<br>
5.2.1 VSCodeのダウンロード<br>
5.2.2 Windowsでのインストール実行<br>
5.3 CoreS3 SEでUART受信<br>
5.4 Module-LLMの開発環境整備<br>
5.4.1 StackFlowの停止<br>
5.5 Module-LLMからUART送信<br>
5.6 結果<br>

## 第6章 AX650Nを先取り検証<br>
6.1 中国メーカーのAX650Nボード<br>
6.2 初めてのTaobao購入<br>
6.3 XJ-i10とは？<br>
6.4 XJ-i10をラズパイに取り付ける<br>
6.4.1 Raspberry Pi M.2 HAT+ボード<br>
6.4.2 失敗談1：Waveshare M.2 HATボード<br>
6.4.3 失敗談2：Geekworm M.2ボード<br>
6.4.4 Raspberry Piでの準備<br>
6.4.5 ドライバのインストール<br>
6.5 AX630CとAX650Nのスペック比較<br>
6.6 AX630CとAX650Nの推論時間比較<br>
6.6.1 評価に使ったYOLOモデルについて<br>
6.7 AX630CとAX650Nの消費電流比較<br>
6.8 最後に<br>

<br>
Copyright (c) 2025 aNoken<br>

