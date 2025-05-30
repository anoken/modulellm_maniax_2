# 第6章 AX650Nを先取り検証


## 概要
Pulsar2コンパイラは、ONNXフォーマットのYOLOモデルをAXERA AIチップ（AX630やAX650）で実行可能な最適化されたモデル（.axmodel）に変換するツールです。このプロセスでは、量子化とハードウェア固有の最適化を通じて、推論速度の向上とメモリ使用量の削減を実現します。


## 必要なファイル

設定には以下のファイルが必要です：

**設定ファイル（JSON形式）**
- `yolo11_config_u8.json` - 8ビット量子化用設定
- `yolo11_config_u16.json` - 16ビット量子化用設定

**キャリブレーションデータ**
- `dataset/calib_image.tar.gz` - モデル量子化に必要なキャリブレーション画像セット

## 量子化オプションの選択

モデル変換時には、精度と性能のバランスを考慮して量子化精度を選択する必要があります。

**8ビット量子化（U8）**
高速な推論速度と小さなモデルサイズを実現しますが、精度が若干低下する可能性があります。リアルタイム処理が重要なアプリケーションに適しています。

**16ビット量子化（U16）**
より高い精度を維持できますが、モデルサイズと計算コストが増加します。精度が最重要のアプリケーションに適しています。


## Config

### AX630C
- **NPU1モード**: 単一NPUコアを使用する基本構成
- **NPU2モード**: デュアルNPUコア構成
- 推論性能: 最大3.2TOPS (Int8)

### AX650N
- **NPU1モード**: 単一NPUコア使用
- **NPU2モード**: デュアルNPUコア使用
- **NPU3モード**: トリプルNPUコア使用
- 推論性能: 最大18TOPS (Int8)


## 環境構築手順

### 1. YOLOモデルの準備

まず、必要なPythonパッケージをインストールし、ONNXフォーマットのYOLOモデルを準備し、AXERA向けに前処理を行います。

```bash
# 必要なパッケージのインストール
UbuntuPC$ pip install ultralytics onnx

# YOLOモデルのエクスポートと前処理
UbuntuPC$ python yolo_export.py
UbuntuPC$ python yolo_onnx_cut.py
```

### 2. Pulsar2 Dockerコンテナの起動

Pulsar2コンパイラをDockerコンテナとして起動します。事前にイメージファイルをダウンロードしておく必要があります。

**イメージの読み込み**
```bash
UbuntuPC$ sudo docker load -i ax_pulsar2_4.0.tar.gz
```

**コンテナの起動**
```bash
UbuntuPC$ sudo docker run -it --net host --rm -v $PWD:/data pulsar2:4.0
```

## モデル変換の実行

Dockerコンテナ内でpulsar2コマンドを使用してモデルを変換します。ターゲットハードウェアとNPU構成に応じて、適切なパラメータを選択してください。

### AX630C向けの変換例

```bash
## 8ビット量子化版の生成

root@pulsar2:/data# pulsar2 build --config config/yolo11_config_u8.json --target_hardware AX620E --npu_mode NPU1 --input yolo11n-cut.onnx --output_name yolo11n_u8_AX620E_NPU1.axmodel
root@pulsar2:/data# pulsar2 build --config config/yolo11_config_u8.json --target_hardware AX620E --npu_mode NPU2 --input yolo11n-cut.onnx --output_name yolo11n_u8_AX620E_NPU2.axmodel

## 16ビット量子化版の生成
root@pulsar2:/data# pulsar2 build --config config/yolo11_config_u16.json --target_hardware AX620E --npu_mode NPU1 --input yolo11n-cut.onnx --output_name yolo11n_u16_AX620E_NPU1.axmodel
root@pulsar2:/data# pulsar2 build --config config/yolo11_config_u16.json --target_hardware AX620E --npu_mode NPU2 --input yolo11n-cut.onnx --output_name yolo11n_u16_AX620E_NPU2.axmodel
```

### AX650N向けの変換例


```bash
## 8ビット量子化版の生成
root@pulsar2:/data# pulsar2 build --config config/yolo11_config_u8.json --target_hardware AX650 --npu_mode NPU1 --input yolo11n-cut.onnx --output_name yolo11n_u8_AX650_NPU1.axmodel
root@pulsar2:/data# pulsar2 build --config config/yolo11_config_u8.json --target_hardware AX650 --npu_mode NPU2 --input yolo11n-cut.onnx --output_name yolo11n_u8_AX650_NPU2.axmodel
root@pulsar2:/data# pulsar2 build --config config/yolo11_config_u8.json --target_hardware AX650 --npu_mode NPU3 --input yolo11n-cut.onnx --output_name yolo11n_u8_AX650_NPU3.axmodel```

## 16ビット量子化版の生成
root@pulsar2:/data# pulsar2 build --config config/yolo11_config_u16.json --target_hardware AX650 --npu_mode NPU1 --input yolo11n-cut.onnx --output_name yolo11n_u16_AX650_NPU1.axmodel
root@pulsar2:/data# pulsar2 build --config config/yolo11_config_u16.json --target_hardware AX650 --npu_mode NPU2 --input yolo11n-cut.onnx --output_name yolo11n_u16_AX650_NPU2.axmodel
root@pulsar2:/data# pulsar2 build --config config/yolo11_config_u16.json --target_hardware AX650 --npu_mode NPU3 --input yolo11n-cut.onnx --output_name yolo11n_u16_AX650_NPU3.axmodel
```

## 参考リンク

Pulsar2コンパイラの詳細情報とダウンロードについては、以下のリンクをご参照ください：
- Pulsar2 docs:https://pulsar2-docs.readthedocs.io/zh-cn/latest/index.html
- Pulsar2huggingfaceリポジトリ：https://huggingface.co/AXERA-TECH/Pulsar2/


