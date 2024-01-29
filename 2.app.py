import tkinter as tk
import joblib

root = tk.Tk()

canvas1 = tk.Canvas(root, width = 400, height = 400)
root.title("Ev Fiyatı Hesaplama")
canvas1.pack()

label1 = tk.Label(root, text="Oda Sayısı: ")
canvas1.create_window(100, 100, window=label1)
entry1 = tk.Entry(root)
canvas1.create_window(200, 100, window=entry1)

label2 = tk.Label(root, text="Net m2: ")
canvas1.create_window(90, 120, window=label2)
entry2 = tk.Entry(root)
canvas1.create_window(200, 120, window=entry2)

label3 = tk.Label(root, text="Bulunduğu Kat: ")
canvas1.create_window(80, 140, window=label3)
entry3 = tk.Entry(root)
canvas1.create_window(200, 140, window=entry3)

label4 = tk.Label(root, text="Yapının Yaşı: ")
canvas1.create_window(80, 160, window=label4)
entry4 = tk.Entry(root)
canvas1.create_window(200, 160, window=entry4)

def values():
    Oda_sayisi = float(entry1.get()) 
    Net_m2 = float(entry2.get()) 
    Kat = float(entry3.get()) 
    Yas = float(entry4.get()) 

    # Kaydettiğimiz modeli ve polinom derecesini çağrıyoruz.
    loaded_model = joblib.load("model")
    loaded_features = joblib.load("pol_features")

    # Girilen verileri, çağırdığım makine öğrenmesi modeli ile dönüşümünü sağlayarak eğtiyorum.
    ev1 = [[Oda_sayisi, Net_m2, Kat, Yas]]
    ev1_t = loaded_features.transform(ev1)
    fiyat = loaded_model.predict(ev1_t)

    # Tahmin değeri ekrana yazdırma.
    label_pred = tk.Label(root, text=(f"Evin fiyatı: {round(fiyat[0],3)} bin TL"), bg = "lawngreen")
    canvas1.create_window(200, 220, window=label_pred)

button = tk.Button(root, text="Evin Tahmin Fiyatını Hesapla",
                font=("Ariel", 9, "bold"), bg="orange", command=values)
canvas1.create_window(200, 190, window=button)

root.mainloop()