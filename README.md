data ulasan pada kode2 ini berasal dari 2 sumber; yaitu kaggel dan juga LLM gemini
pada data kaggle diperlukan pre-proces yang lebih rumit yakni pembersihan karakter berlebih, emoji, dsb
sementara pada data sintesis ini lebih simple sebab ulasan yang dihasilkan sudah disesuaikan dengan prompt engineeringnya sehingga data tak perlu banyak preproces
2 data tadi kemudian dijadikan satu file csv. anda bisa mengunduhnya melalui link berikut : https://huggingface.co/datasets/siRendy/dataset-analisis-sentimen-review-produk
selain untuk indobert, data-data ulasan ini kemudian dikelompokan per 20 review yang nantinya akan digunakan untuk finetune indoT5. 
