import pyqrcode
qr = pyqrcode.create("https://www.tiktok.com/@sibergazete") #?We get the link you want to go to  # Buraya Gitmek İstediğin Linki Alıyoruz
qr.png('save.png', scale=8)