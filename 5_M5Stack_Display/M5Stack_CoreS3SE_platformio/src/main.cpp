#include <M5Unified.h>

#include "driver/uart.h"

// =============================================================================
// 定数定義
// =============================================================================
static const uart_port_t UART_PORT = UART_NUM_2;  // 使用するUARTポート
static const int BUFFER_SIZE = 16384;             // バッファサイズ（16KB）
static const int BAUD_RATE = 2000000;             // ボーレート（2Mbps）

// =============================================================================
// UART初期化関数
// =============================================================================
void setup_uart() {
  // UART設定
  uart_config_t uart_config = {
      .baud_rate = BAUD_RATE,
      .data_bits = UART_DATA_8_BITS,
      .parity = UART_PARITY_DISABLE,
      .stop_bits = UART_STOP_BITS_1,
      .flow_ctrl = UART_HW_FLOWCTRL_DISABLE,
      .source_clk = UART_SCLK_APB,
  };

  // M5StackのPort-C（UART）ピンを取得
  int rx_pin = M5.getPin(m5::pin_name_t::port_c_rxd);
  int tx_pin = M5.getPin(m5::pin_name_t::port_c_txd);

  // UARTドライバの初期化（キューなし、DMAなし）
  ESP_ERROR_CHECK(
      uart_driver_install(UART_PORT, BUFFER_SIZE * 2, 0, 0, NULL, 0));
  ESP_ERROR_CHECK(uart_param_config(UART_PORT, &uart_config));
  ESP_ERROR_CHECK(uart_set_pin(UART_PORT, tx_pin, rx_pin, UART_PIN_NO_CHANGE,
                               UART_PIN_NO_CHANGE));
}

// =============================================================================
// 画像受信・表示処理
// =============================================================================
void process_image() {
  // パケット開始マーカー
  static const uint8_t PACKET_START[3] = {0xFF, 0xD8, 0xEA};
  uint8_t header[10];  // ヘッダー用バッファ

  // 受信データがあるかチェック
  size_t available_bytes = 0;
  uart_get_buffered_data_len(UART_PORT, &available_bytes);

  if (available_bytes < 10) {
    return;  // ヘッダー分のデータがない
  }

  // 1. ヘッダー（10バイト）を読み取り
  int header_read = uart_read_bytes(UART_PORT, header, 10, pdMS_TO_TICKS(100));
  if (header_read != 10) {
    M5_LOGW("Header read failed: %d bytes", header_read);
    return;
  }

  // ヘッダーの検証
  if (header[0] != PACKET_START[0] || header[1] != PACKET_START[1] ||
      header[2] != PACKET_START[2]) {
    M5_LOGW("Invalid packet header: 0x%02X 0x%02X 0x%02X", header[0], header[1],
            header[2]);
    return;
  }

  // ヘッダーからデータサイズとフレーム番号を取得
  uint32_t jpeg_size = (header[4] << 16) | (header[5] << 8) | header[6];
  uint32_t frame_num = (header[7] << 16) | (header[8] << 8) | header[9];

  M5_LOGI("Frame %u, Size %u bytes", frame_num, jpeg_size);

  // サイズチェック
  if (jpeg_size > BUFFER_SIZE || jpeg_size == 0) {
    M5_LOGW("Invalid image size: %u", jpeg_size);
    uart_flush_input(UART_PORT);  // 受信バッファをクリア
    return;
  }

  // 2. 画像データ用メモリを確保（通常のmalloc）
  uint8_t* image_buffer = (uint8_t*)malloc(jpeg_size);
  if (!image_buffer) {
    M5_LOGE("Memory allocation failed for %u bytes", jpeg_size);
    return;
  }

  // 3. 画像データを読み取り
  unsigned long start_time = millis();
  int bytes_read =
      uart_read_bytes(UART_PORT, image_buffer, jpeg_size, pdMS_TO_TICKS(1000));
  unsigned long read_time = millis() - start_time;

  // 4. 読み取り成功時は即座に画面に表示
  if (bytes_read == jpeg_size) {
    M5_LOGI("Read complete in %lu ms", read_time);

    // 画像を画面に描画
    unsigned long display_start = millis();
    M5.Lcd.drawJpg(image_buffer, jpeg_size);
    unsigned long display_time = millis() - display_start;

    M5_LOGI("Displayed in %lu ms (Total: %lu ms)", display_time,
            millis() - start_time);
  } else {
    M5_LOGW("Read failed: expected %u, got %d bytes in %lu ms", jpeg_size,
            bytes_read, read_time);
  }

  // メモリを解放
  free(image_buffer);
}

// =============================================================================
// セットアップ関数
// =============================================================================
void setup() {
  // M5Stack初期化
  M5.begin();
  M5.Display.setTextSize(1);
  M5.Display.setTextScroll(true);
  M5.Lcd.setTextFont(&fonts::efontJA_16);
  M5.Log.setLogLevel(m5::log_target_display, ESP_LOG_INFO);

  // UART初期化
  setup_uart();

  M5_LOGI("UART Image Display Started");
  M5.Display.printf(">> UART Image Display\n");
}

// =============================================================================
// メインループ
// =============================================================================
void loop() {
  M5.update();      // M5Stackの状態更新
  process_image();  // 画像処理
  delay(1);         // 1ms待機
}