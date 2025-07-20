from TTS.api import TTS

# Türkçe veya İngilizce bir TTS modeli seç
model_name = "tts_models/tr/common-voice/glow-tts"


# TTS modelini yükle
tts = TTS(model_name)

def text_to_speech(text, output_path="output.wav"):
    print("TTS başlatıldı...")
    tts.tts_to_file(text=text, file_path=output_path)
    print(f"TTS sonucu {output_path} olarak kaydedildi.")

if __name__ == "__main__":
    while True:
        user_input = input("Sesli okumak için metin girin (Çıkmak için 'q' yazın): ")
        if user_input.strip().lower() == 'q':
            print("Program sonlandırıldı.")
            break
        if user_input.strip() == "":
            print("Lütfen boş metin girmeyin.")
            continue
        text_to_speech(user_input)