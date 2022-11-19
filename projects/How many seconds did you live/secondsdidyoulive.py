from datetime import *

doğumgünü = datetime.strptime(input("Doğum Günün (Gün.Ay.Yıl): "), "%d.%m.%Y") #day month year
yaş = datetime.now() - doğumgünü

print ("Sen {} saniyedir yaşıyorsun büyük başarı .".format(yaş.total_seconds()))