import whisper
import sounddevice as sd
import numpy as np
import librosa

def record_audio(duration=5, fs=16000):
    print(f"{duration} saniye konuşun, kayıt başlıyor...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    print("Kayıt tamamlandı.")
    return np.squeeze(recording)

def save_audio_to_wav(audio, filename, fs=16000):
    import soundfile as sf
    sf.write(filename, audio, fs)
    print(f"Ses {filename} dosyasına kaydedildi.")

if __name__ == "__main__":
    fs = 16000
    duration = 5

    audio = record_audio(duration=duration, fs=fs)

    # Whisper modelini yükle
    print("Whisper modeli yükleniyor...")
    model = whisper.load_model("base")  # base, small, medium, large seçenekleri var

    # Kayıtlı ses dosyasını kaydet
    wav_path = "recorded_audio.wav"
    save_audio_to_wav(audio, wav_path, fs)

    # Ses dosyasını çözümle ve metne çevir
    result = model.transcribe(wav_path, language='tr')  # Türkçe için 'tr' dili
    print("Algılanan metin:", result['text'])
