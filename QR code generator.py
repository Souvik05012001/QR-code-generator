import pyqrcode
from pyqrcode import QRCode
s=("https://www.youtube.com/@Souvikdas8861/about")
url=pyqrcode.create(s)
url.png("MyfirstQRCode.png",scale=10,colour="red")
#getqrcode=pyqrcode.create(s)
#getqrcode.png('myfirstqrcode.png',scale=4,module_color='red')

