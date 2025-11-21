import qrcode
import time

def slow_print(a, delay=0.05):
    for char in a:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()
slow_print("Enter your website: ")
wb = input()
while True:
    try:
        slow_print("Enter your fill color: ")
        fill = input()
        slow_print("Enter your background color: ")
        bg = input()
        features = qrcode.QRCode(version=1, box_size=75, border=2)
        features.add_data(wb)
        features.make(fit=True)
        generate_image = features.make_image(fill_color=fill, back_color=bg)
        generate_image.save("image1.png")
         
        print("Generating", end='', flush=True)
        for _ in range(6):
            print('.', end='', flush=True)
            time.sleep(0.3)
        print()  
        print("QR Code generated and saved as image1.png")
        break
    except Exception as e:
        print("Invalid Colors; Please Try Again")
        print()
