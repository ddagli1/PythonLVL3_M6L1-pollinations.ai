import requests

def gorsel_olustur(prompt, dosya_adi="olusturulan_resim.jpg"):
    # Prompt içindeki boşlukları URL uyumlu hale getiriyoruz
    formatted_prompt = prompt.replace(" ", "%20")
    
    # Pollinations.ai URL yapısı
    url = f"https://image.pollinations.ai/prompt/{formatted_prompt}?width=1024&height=1024&nologo=true"

    print(f"Görsel oluşturuluyor: {prompt}...")
    
    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            # Görseli yerel dosyaya kaydetme
            with open(dosya_adi, 'wb') as f:
                f.write(response.content)
            print(f"Başarılı! Görsel '{dosya_adi}' olarak kaydedildi.")
        else:
            print("Görsel alınamadı. Hata kodu:", response.status_code)
            
    except Exception as e:
        print("Bir hata oluştu:", e)

# Kullanım örneği
prompt_metni = "cyberpunk city with neon lights and flying cars"
gorsel_olustur(prompt_metni)
