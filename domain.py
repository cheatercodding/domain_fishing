import tldextract
from fuzzywuzzy import fuzz

trusted_domains = ["paypal.com", "google.com", "spotify.com", "facebook.com", "microsoft.com", "hepsiburada.com", "trendyol.com", "youtube.com"]

# Alan adı karşılaştırma fonksiyonu
def is_phishing(url):
    extracted = tldextract.extract(url)
    domain = f"{extracted.domain}.{extracted.suffix}"

    max_similarity = 0
    closest_match = None

    for trusted in trusted_domains:
        similarity = fuzz.ratio(domain, trusted)
        if similarity > max_similarity:
            max_similarity = similarity
            closest_match = trusted

    return domain, closest_match, max_similarity

# Örnek test domainleri
urls = ["paypa1.com", "faceboook.com", "microssft.com", "hepsiburada.com", "trendyol.com", "youtube.com", "google.com"]

for url in urls:
    domain, match, score = is_phishing(url)
    print(f"Test Edilen Domain: {domain}")
    print(f"En Yakın Eşleşme: {match} (%{score} benzerlik)")

    if score >= 95:
        print("✅ Güvenli Site Olabilir.")
    elif score >= 85:
        print("⚠️ Şüpheli Site, Dikkat Edin!")
    else:
        print("🚨 Olası Phishing Saldırısı Olabilir.")
    
    print("-" * 40)
