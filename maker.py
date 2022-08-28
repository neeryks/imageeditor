from PIL import Image,ImageDraw,ImageFont
compass = Image.open('mediaasset/bbs-01.png')
image = Image.new('RGB',compass.size,'black')
img = ImageDraw.Draw(image)
img.text((1000,800),"Your Title Here", fill='white',font = ImageFont.truetype("mediaasset/Mont.ttf",230),anchor="ms")
image.paste(compass)
image.show()
