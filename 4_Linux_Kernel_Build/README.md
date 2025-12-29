# Module-LLM/LLM630 Compute Kit Linuxカーネルカスタマイズ手順

## 概要

Module-LLM/LLM630 Compute KitのLinuxカーネルを含むファームウェアのソースコードが、M5StackのGitHubのリポジトリでオープンソースで公開されています。Module-LLMのLinuxカーネルをカスタマイズする手順を説明します。

**リポジトリ：** [https://github.com/m5stack/LLM_buildroot-external-m5stack](https://github.com/m5stack/LLM_buildroot-external-m5stack)

## 必要なパッケージのインストール

UbuntuがインストールされたPCを準備し、Buildrootのビルドに必要な基本的な開発ツールをインストールします。Buildrootとは、組み込みLinuxシステムの構築を行うシステムです。

```bash
Ubuntu-PC$ sudo apt install debianutils sed make binutils
Ubuntu-PC$ sudo apt install build-essential gcc g++ bash patch gzip bzip2
Ubuntu-PC$ sudo apt install perl tar cpio unzip rsync file bc git
Ubuntu-PC$ sudo apt install libpcre3
```

| カテゴリ | パッケージ |
|---------|-----------|
| コンパイラ関連 | gcc, g++, binutils |
| ビルドツール | make, build-essential |
| アーカイブツール | gzip, bzip2, tar, cpio, unzip |
| 基本ユーティリティ | sed, bash, perl, rsync, file |
| バージョン管理 | git |
| テキスト検索・置換処理 | libpcre3 |

**Buildrootのドキュメント:** [https://buildroot.org/docs.html](https://buildroot.org/docs.html)

## ビルド環境の準備

GitHubのLLM_buildroot-external-m5stackリポジトリからソースコードをgitコマンドでダウンロードします。そして、toolsというフォルダに移動します。

```bash
Ubuntu-PC$ git clone https://github.com/m5stack/LLM_buildroot-external-m5stack.git
Ubuntu-PC$ cd LLM_buildroot-external-m5stack/tools/
```

## ビルドスクリプトについて

toolsフォルダにはModule-LLM向けに4種類、LLM630 Compute Kit向けに7種類の組み込みLinuxシステムを構築するシェルスクリプトが用意されています。

例えば、Module-LLM向けの`creat_Module_LLM_buildroot_image.sh`は、Module-LLMデバイス用のbuildrootイメージを作成するスクリプトです。`creat_Module_LLM_ubuntu22_04_image.sh`は、Module-LLM向けのUbuntu 22.04イメージを作成するスクリプトです。Ubuntu 22.04イメージを作成するスクリプトは、Buildrootイメージを作成するスクリプトを呼び出した後に、Ubuntu 22.04イメージを作成する仕組みになっています。

使用する環境に応じて適切なスクリプトを選択し実行します：

```bash
Ubuntu-PC$ ls ./tools                                                      
creat_Module_LLM_buildroot_image.sh
creat_Module_LLM_buildroot_image_4_8.sh
creat_Module_LLM_ubuntu22_04_image-mini.sh
creat_Module_LLM_ubuntu22_04_image.sh

creat_AX630C_LITE_buildroot_image.sh
creat_AX630C_LITE_buildroot_image_V3.0.0_20241120230136.sh    
creat_AX630C_LITE_ubuntu22_04_image.sh
creat_AX630C_LITE_ubuntu22_04_desktop_image.sh                
creat_AX630C_LITE_ubuntu22_04_image.sh                        
creat_AX630C_LITE_ubuntu22_04_image_V3.0.0_20241120230136.sh
creat_AX630C_LITE_ubuntu22_04_image_full.sh
```

## ビルドスクリプトの修正

`creat_Module_LLM_buildroot_image.sh`のスクリプトでは、特定のホスト名が合致するときのみライブラリをインストールする処理が入っているのですが、自分のPCのホスト名でもこの処理を実行するように、ビルドスクリプトを修正します。特定のホスト名が合致するときの条件分岐をコメントアウトします。

**creat_Module_LLM_buildroot_image.sh**

```bash
clone_buildroot() {
    if [ -d '../buildroot' ] ; then
        [ -d 'buildroot' ] || cp -r ../buildroot buildroot 
    else
        [ -d 'buildroot' ]||
        git clone https://github.com/bootlin/buildroot.git -b st/2023.02.10
    fi
        [ -d 'buildroot' ] || { echo "not found buildroot" && exit -1; }
        pushd buildroot
        hostname=$(hostname)

        # ↓以下の条件分岐をコメントアウトして実行されるようにします
        #if [ "$hostname" = "nihao-z690" ]; then
            [ -f 'dl.7z' ] ||
   wget https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/linux/llm/dl.7z
            [ -d 'dl' ] || 7z x dl.7z -odl
            [ -d 'dl' ] || { echo "not found dl" && exit -1; }
        #fi
        [ -f '../../../board/m5stack/module_LLM/image_support/opt.tar.gz' ]
        || wget https://github.com/m5stack/LLM_buildroot-external-m5stack/
        releases/download/v0.0.0/opt.tar.gz -O
        ../../../board/m5stack/module_LLM/image_support/opt.tar.gz
        popd
}
```

Module-LLMデバイス用のUbuntu 22.04イメージをビルドしてみましょう。

```bash
Ubuntu-PC$ cd LLM_buildroot-external-m5stack/tools/
Ubuntu-PC$ ./creat_Module_LLM_ubuntu22_04_image.sh
```

ビルドが完了すると、`build_Module_LLM_ubuntu22_04`のディレクトリに拡張子axpのファームウェアが生成されています。これがModule-LLMのファームウェアになります。

```bash
Ubuntu-PC$ cd LLM_buildroot-external-m5stack/tools/build_Module_LLM_ubuntu22_04/
Ubuntu-PC$ ls 
M5_LLM_ubuntu22.04_20250521.axp 
```


## カスタム設定の適用

ビルド設定をカスタマイズする場合は、以下の手順で行います：
creat_Module_LLM_buidlroot_image.shに make menuconfigを追加します。

参考：
https://github.com/nnn112358/LLM_buildroot-external-m5stack/blob/main/tools/creat_Module_LLM_buidlroot_image.sh

```bash
$ vi ./creat_Module_LLM_buidlroot_image.sh
```

```
make_buildroot() {
    cd buildroot
    make BR2_EXTERNAL=../../.. m5stack_module_llm_4_19_defconfig
    
    # menuconfigを実行
    make menuconfig
    
    [[ -v ROOTFS_SIZE ]] && sed -i 's/^\(BR2_TARGET_ROOTFS_EXT2_SIZE=\).*$/\1"'"${ROOTFS_SIZE}"'"/' .config
    make -j `nproc`
}
```

menuconfig画面では、以下のような項目を設定できます：

- Target options：ターゲットアーキテクチャの設定
- Build options：ビルドオプションの設定
- Toolchain：ツールチェーンの設定
- System configuration：システム設定
- Target packages：必要なパッケージの選択
- Filesystem images：ファイルシステムイメージの設定

outputディレクトリにaxpファイルが生成されます。


## ALSAマイクの問題について

M5StackがリリースしているModule-LLMのファームウェアでは、ALSAドライバー経由でマイクからの音声を録音すると、量子化ビット数が16bitの設定のときのみ、音声データにノイズが載る現象が発生しました。

スマートフォンから、toneジェネレーターのアプリを使って、1kHzの音をModule-LLMの近くで鳴らしてマイクから録音してみました。テキスト化したwavファイルのデータをグラフ化したものが以下になります。

![16bit録音時のノイズ問題1](https://storage.googleapis.com/zenn-user-upload/6bb7e6faf9ab-20250527.png)

![16bit録音時のノイズ問題2](https://storage.googleapis.com/zenn-user-upload/00ac754a4143-20250527.png)

量子化ビット数が16bitの設定のときに、1kHzの音が、500Hzの音に変化しています。1個のデータを採取するごとに振幅0のデータが挿入されています。32bitと24bitのwavはそのような異常が見られないので、16bit特有の現象です。

@ciniml氏により、原因が特定されました。AX630C向けの音声システム用のドライバー内に16bitのときのみ行われる、不要と思われる処理があり、これらを削除すると直るとのことです。

**参考:** [Module-LLMの音声入力まわり](https://zenn.dev/ciniml/articles/module_llm_audio_system)

本書執筆時点（2025年5月）では、M5StackがリリースしているModule-LLMのファームウェアには対策が導入されていないため、自分でビルドを行う必要があります。

LLM_buildroot-external-m5stackを使って、ALSAドライバー経由のマイク処理に修正を加えたModule-LLMのファームウェアの作成の仕方を説明します。

### 手順1: 初回ビルド

まず、最初にModule-LLMデバイス用のUbuntu 22.04イメージを作成するスクリプトを実行します。

```bash
Ubuntu-PC$ git clone https://github.com/m5stack/LLM_buildroot-external-m5stack.git
Ubuntu-PC$ cd LLM_buildroot-external-m5stack/tools/
Ubuntu-PC$ ./creat_Module_LLM_ubuntu22_04_image.sh
```

### 手順2: ドライバーソースコードの修正

次に、スクリプトが生成した`build_Module_LLM_buildroot`のフォルダの中で、`dwc-i2s.c`のソースコードを修正します。

@ciniml氏が提案する修正手順に従って、`dwc-i2s.c`のソースコードを修正します。
具体的には、`dw_i2s_config`関数の中の16bit時の条件分岐の処理をコメントアウトします。

**参考:** [Module-LLMの音声入力まわり](https://zenn.dev/ciniml/articles/module_llm_audio_system)

```bash
Ubuntu-PC$ vim \
./tools/build_Module_LLM_buildroot/buildroot/output/build/ \
linux-custom/build/linux-4.19.125/sound/soc/axera/dwc-i2s.c
```

```c
static void dw_i2s_config(struct dw_i2s_dev *dev, int stream){
	u32 ch_reg;
	struct i2s_clk_config_data *config = &dev->config;
	i2s_disable_channels(dev, stream);

	for (ch_reg = 0; ch_reg < (config->chan_nr / 2); ch_reg++) {
		if (stream == SNDRV_PCM_STREAM_PLAYBACK) {
			i2s_write_reg(dev->i2s_base, TCR(ch_reg),
				      dev->xfer_resolution);
			i2s_write_reg(dev->i2s_base, TFCR(ch_reg),
				      dev->fifo_th - 1);
			i2s_write_reg(dev->i2s_base, TER(ch_reg), 1);
		} else {
			i2s_write_reg(dev->i2s_base, RCR(ch_reg),
				      dev->xfer_resolution);
			i2s_write_reg(dev->i2s_base, RFCR(ch_reg),
				      dev->fifo_th - 1);
			i2s_write_reg(dev->i2s_base, RER(ch_reg), 1);

			// 以下の16bit時の処理をコメントアウトする
			//if (16 == config->data_width) {
			//	i2s_write_reg(dev->i2s_base, RCR(1),
			//	dev->xfer_resolution);
			//	i2s_write_reg(dev->i2s_base, RFCR(1),
			//	dev->fifo_th - 1);
			//	i2s_write_reg(dev->i2s_base, RER(1), 1);
			//}
		}
	}
}
```

### 手順3: カーネルの再ビルド

LLM_buildroot-external-m5stackのbuildrootディレクトリでBuildrootの再ビルドを行います。

```bash
Ubuntu-PC$ cd LLM_buildroot-external-m5stack/tools/
Ubuntu-PC$ cd ./build_Module_LLM_buildroot/buildroot/
Ubuntu-PC$ make linux-rebuild
```

### 手順4: ファームウェアの生成

最後に、Module-LLMデバイス用のUbuntu 22.04イメージをビルドするスクリプトを実行します。

```bash
Ubuntu-PC$ cd LLM_buildroot-external-m5stack/tools/
Ubuntu-PC$ ./creat_Module_LLM_ubuntu22_04_image.sh
```

## ファームウェアの書き込みツール

本書執筆時点（2025年5月）、Module-LLMのファームウェア書き込みツールは3種類あります。

| ツール | 対応OS | リンク |
|--------|--------|--------|
| AXDL_V1.24.13.1 | Windows | [ダウンロード](https://docs.m5stack.com/en/guide/llm/llm630_compute_kit/image) |
| M5Stack作成 Python版 AXDLツール | Windows/Linux/Mac | [GitHub](https://github.com/m5stack/LLM_buildroot-external-m5stack) |
| cinimlさん作成 Rust版 AXDLツール | Windows/Linux/Mac | [GitHub](https://github.com/ciniml/axdl-rs) / [Web GUI](https://www.fugafuga.org/axdl-rs/axdl-gui/latest/) |

## 参考文献

- Kenta IDA / [Module-LLMの音声入力まわり](https://zenn.dev/ciniml/articles/module_llm_audio_system)
- Kenta IDA / [Module-LLMのダウンロード処理解析](https://drive.google.com/file/d/1cH9iMvV7b69wZa44sIDuulfTB8Qc0HAu/view)
- @kinneko / [buildrootとかニーズないかな](https://www.docswell.com/s/kinneko/582RMW-M5StackLLM)
- @mongonta / [M5Stack Module-LLMのカスタムカーネル化手順](https://zenn.dev/mongonta/articles/92c442f19c792a)
