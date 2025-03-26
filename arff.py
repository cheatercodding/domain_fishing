from scipy.io import arff
import pandas as pd

# ARFF dosyasının yolu
arff_path = 'C:/Users/merge/Downloads/phishing+websites/phishing_data.old.arff'

# ARFF dosyasını oku
data, meta = arff.loadarff(arff_path)

# Veriyi pandas DataFrame olarak dönüştür
df = pd.DataFrame(data)

# Veriyi CSV olarak kaydet
csv_path = 'C:/Users/merge/Downloads/phishing+websites/phishing_data.csv'
df.to_csv(csv_path, index=False)

print(f"CSV dosyası başarıyla oluşturuldu: {csv_path}")