import requests

def speech_to_text(file_path, model="whisper-tiny", language="ja"):
    url = "http://localhost:8000/v1/audio/transcriptions"
    
    headers = {
        "Authorization": "Bearer YOUR_KEY"
    }
    
    try:
        # ファイルを開いてマルチパートフォームデータとして送信
        with open(file_path, 'rb') as audio_file:
            files = {
                'file': audio_file
            }
            data = {
                'model': model,
                'language': language
            }
            
            response = requests.post(url, headers=headers, files=files, data=data)
            response.raise_for_status()  # エラーがあれば例外を発生
            
            result = response.json()
            
            # 文字起こし結果を表示
            if 'text' in result:
                print(f"文字起こし結果: {result['text']}")
                return result['text']
            elif 'transcript' in result:
                print(f"文字起こし結果: {result['transcript']}")
                return result['transcript']
            else:
                print(f"レスポンス: {result}")
                return result
                
    except requests.exceptions.RequestException as e:
        print(f"エラーが発生しました: {e}")
        return None
    except FileNotFoundError:
        print(f"ファイルが見つかりません: {file_path}")
        return None
    except Exception as e:
        print(f"予期しないエラー: {e}")
        return None

# 使用例
if __name__ == "__main__":
    speech_to_text("test_whisper.wav", model="whisper-tiny", language="en")


