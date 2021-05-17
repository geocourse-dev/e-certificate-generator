from PIL import Image, ImageDraw, ImageFont
import qrcode

img = Image.open('template/completion.png').convert('RGB')
back = Image.open('template/back.jpg').convert('RGB')

draw = ImageDraw.Draw(img)
font = ImageFont.truetype('font/font.ttf', size=150)
certfont = ImageFont.truetype('font/font.ttf', size=80)

message = "Rahmat Faisal"
certid = "GEE-IV-001"

x1, y1, x2, y2 = 1184, 1400, 2184, 1200
w, h = draw.textsize(message, font=font)

a1, b1, a2, b2 = 1384, 400, 1984, 2000
wa, ha = draw.textsize(certid, font=certfont)

x = (x2 - x1 - w)/2 + x1
y = (y2 - y1 - h)/2 + y1

a = (a2 - a1 - wa)/2 + a1
b = (b2 - b1 - ha)/2 + a1

draw.text((x, y), message, align='center',fill='black', font=font)
draw.text((a,b), certid, align='center', fill='black', font=certfont)

qr = qrcode.make('geocourse.id/verif/'+certid)
img.paste(qr, (1000, 1950))

im_list = [back]
filename = 'output/'+ str(certid) + '-' + str(message) + '.pdf'
img.save(filename, "PDF", resolution=100.0, save_all=True, append_images=im_list)
