import requests

def text_to_speech(text, model="melotts-en-us", voice="alloy", output_file="test_voice.mp3"):

    url = "http://localhost:8000/v1/audio/speech"
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer YOUR_KEY"
    }
    
    data = {
        "model": model,
        "input": text,
        "voice": voice
    }
    
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()  # エラーがあれば例外を発生
        
        # 音声データをファイルに保存
        with open(output_file, 'wb') as f:
            f.write(response.content)
        
        print(f"音声ファイルが {output_file} に保存されました")
        return True
        
    except requests.exceptions.RequestException as e:
        print(f"エラーが発生しました: {e}")
        return False

# 使用例
if __name__ == "__main__":
    text_to_speech("hello world", model="melotts-en-us", voice="alloy",output_file="test_voice.mp3")


