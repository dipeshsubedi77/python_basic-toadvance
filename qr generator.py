import qrcode
data = "https://www.dipeshsubedi.info.np"
image = qrcode.make(data)
image.save("abc.png")
print("QR code generated and sucessfully on the abc.png file")