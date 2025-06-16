import pandas as pd
import re
import emoji

def clean_text(text):
    # 1. Menghapus emoji
    text = emoji.replace_emoji(text, replace='')
    
    # 2. Menghapus selain huruf, angka, dan tanda baca dasar (?!.,)
    # Menyimpan huruf (a-z, A-Z), angka (0-9), spasi, dan tanda baca dasar
    text = re.sub(r"[^\w\s?!.,]", '', text)
    
    # 3. Menghapus karakter berulang (lebih dari 2 kali)
    # Contoh: zzzzz menjadi zz, ..... menjadi ..
    text = re.sub(r'(.)\1{2,}', r'\1\1', text)
    
    # 4. Menghapus tanda baca berlebih (lebih dari 2 kali)
    # Contoh: !!!!! menjadi !!, ........ menjadi ..
    text = re.sub(r'([?!.,])\1{2,}', r'\1\1', text)
    
    return text

# Baca dataset
df = pd.read_csv('df_summarized_sintesis-pake-gemini-pro-v3.csv')

# Bersihkan teks di kolom original_text
df['original_text'] = df['original_text'].apply(lambda x: clean_text(str(x)))

# Simpan kembali ke CSV
df.to_csv('data_cleaned.csv', index=False)

print("Pembersihan teks selesai. Data telah disimpan ke data_cleaned.csv")