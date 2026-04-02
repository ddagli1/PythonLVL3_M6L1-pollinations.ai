import requests

# Ayarlar
prompt = "cyberpunk city with neon lights and flying cars"
dosya_adi = "olusturulan_resim.jpg"

# Prompt içindeki boşlukları URL uyumlu hale getirme
formatted_prompt = prompt.replace(" ", "%20")

# URL oluşturma
url = f"https://image.pollinations.ai/prompt/{formatted_prompt}?width=1024&height=1024&nologo=true"

print(f"Görsel oluşturuluyor: {prompt}...")

try:
    # İsteği gönderme
    response = requests.get(url)
    
    if response.status_code == 200:
        # Görseli dosyaya yazma
        with open(dosya_adi, 'wb') as f:
            f.write(response.content)
        print(f"Başarılı! Görsel '{dosya_adi}' olarak kaydedildi.")
    else:
        print(f"Görsel alınamadı. Hata kodu: {response.status_code}")

except Exception as e:
    print(f"Bir hata oluştu: {e}")
