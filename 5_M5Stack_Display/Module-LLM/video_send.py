import serial
import time
import cv2

def send_video_serial(video_path, serial_port='/dev/ttyS1', baudrate=2000000, quality=90):
    ser = serial.Serial(serial_port, baudrate, timeout=1)  # シリアルポートを開く
    cap = cv2.VideoCapture(video_path)                     # 動画を開く
    frame_count = 0
    
    while True:
        ret, frame = cap.read()                            # フレーム読み取り
        if not ret:
            break
        
        resized_frame = cv2.resize(frame, (320, 240))      # 320x240にリサイズ
        
        _, frame_data = cv2.imencode('.jpg', resized_frame, 
                                   [cv2.IMWRITE_JPEG_QUALITY, quality])  # JPEG圧縮
        image_data = frame_data.tobytes()
        total_size = len(image_data)
        
        size1 = (total_size >> 16) & 0xFF                 # サイズを3バイトに分割
        size2 = (total_size >> 8) & 0xFF
        size3 = total_size & 0xFF
        
        header = bytearray([                               # ヘッダーパケット作成
            0xFF, 0xD8, 0xEA, 0x01,                        # 識別子
            size1, size2, size3,                           # データサイズ
            (frame_count >> 16) & 0xFF,                    # フレーム番号
            (frame_count >> 8) & 0xFF,
            frame_count & 0xFF
        ])
        
        ser.write(header)                                  # ヘッダー送信
        print(f"フレーム {frame_count}: {total_size} バイト")
        
        time.sleep(0.01)                                   # 少し遅延
        ser.write(image_data)                              # データ送信
        frame_count += 1
        time.sleep(0.03)                                   # フレーム間遅延
    
    ser.close()                                            # 終了処理
    cap.release()
    print(f"送信完了: {frame_count} フレーム")

if __name__ == "__main__":                                 # 実行
    send_video_serial("test_movie.mp4", "/dev/ttyS1", 2000000, 90)

