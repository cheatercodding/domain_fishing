import tldextract
from fuzzywuzzy import fuzz

trusted_domains = ["paypal.com", "google.com", "spotify.com", "facebook.com", "microsoft.com", "hepsiburada.com", "trendyol.com", "youtube.com"]

# Alan adı karşılaştırma fonksiyonu
def is_phishing(url):
    # URL'den domain çıkar
    extracted = tldextract.extract(url)
    domain = f"{extracted.domain}.{extracted.suffix}"

    # Benzerlikleri bulan algoritma
    max_similarity = 0
    closest_match = None

    for trusted in trusted_domains:
        similarity = fuzz.ratio(domain, trusted)
        if similarity > max_similarity:
            max_similarity = similarity
            closest_match = trusted

    # Sonuçları döndür
    return domain, closest_match, max_similarity

# Örnek phishing ve gerçek siteleri test edelim
urls = ["paypa1.com", "faceboook.com", "microsft.com", "hepsiburada.com", "trendyol.com", "youtube.com", "google.com"]

for url in urls:
    domain, match, score = is_phishing(url)
    print(f"Test Edilen Domain: {domain}")
    print(f"En Yakın Eşleşme: {match} (%{score} benzerlik)")

    if score > 90:
        print("✅ Güvenli Site Olabilir.")
    else:
        print("🚨 Olası Phishing Saldırısı Olabilir.")
    
    print("-" * 40)
