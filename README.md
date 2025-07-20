# 🗣️ Türkçe Destekli TTS & ASR Projesi

Bu depo, **Türkçe destekli** iki temel ses işleme görevini içerir:  
- 🎤 **ASR (Automatic Speech Recognition)** — Ses kaydını metne dönüştürme  
- 🔊 **TTS (Text-to-Speech)** — Metni ses dosyasına dönüştürme

---

## 📂 Proje İçeriği

- `asr.py` : Mikrofon ile 5 saniyelik ses kaydı yapar, Whisper modeli ile metne çevirir.  
- `tts.py` : Kullanıcıdan alınan metni Glow-TTS modeli ile ses dosyasına dönüştürür.

---

## 🚀 Özellikler

- 🇹🇷 **Türkçe dil desteği**  
- Whisper'ın `base` modeli ile etkili konuşma tanıma  
- Glow-TTS tabanlı doğal ve akıcı ses sentezi  
- Kolayca çalıştırılabilir, minimal kod ve bağımlılıklar  

---

## ⚙️ Gereksinimler

Python 3.8+ ortamında aşağıdaki kütüphaneler gereklidir:

```bash
pip install -r requirements.txt
```
## 💡 Notlar

 - Mikrofon erişiminiz açık olmalıdır.

 - Whisper modeli farklı boyutlarda kullanılabilir (base, small, medium, large). İhtiyaca göre değiştirebilirsiniz.

 - TTS modeli, Glow-TTS tabanlı olup Türkçe için optimize edilmiştir.

 - Disk alanı ve internet bağlantınızın yeterli olduğundan emin olun.

## 📄 Lisans & İletişim

 - Proje kişisel kullanım ve öğrenme amaçlıdır.
