import pyqrcode
qr = pyqrcode.create("https://www.tiktok.com/@sibergazete") #?We get the link you want to go to  # Gitmek istediğiniz bağlantıyı yapıştırın
qr.png('save.png', scale=8)
