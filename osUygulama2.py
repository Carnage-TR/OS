#masaüstündeki sadece word  dosyalarını ekrana yazdırınız
import os
for i in os.listdir("C:/Users/ogr10/Desktop/"):
    if i.endswith(('.docx')):
        print(i)
    else:
        print("Böyle bir dosya bulunmamakta")