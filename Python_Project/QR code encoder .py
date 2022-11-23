import qrcode
qr=qrcode.QRCode(version=1,border=4,box_size=10)
d=input("enter url")
data='https://www.youtube.com/watch?v=2C_YaOQ2yGg&list=PLpp8-k7G_6Y3Wj1suZQ-9lATFzFuGw93x&index=2'
qr.add_data(d)
qr.make(fit=True)
img=qr.make_image(fill_color='black',back_color='white')
img.save('qrmyimage.png')