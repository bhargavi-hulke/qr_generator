import qrcode
wb = (input("enter your website:"))
features= qrcode.QRCode(version=1,box_size=75, border= 2)
features.add_data(wb)
features.make(fit=True)
generate_image= features.make_image(fill_color="turquoise",back_color="black")
generate_image.save("image1.png")