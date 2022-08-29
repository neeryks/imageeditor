from tkinter import ANCHOR
from PIL import Image, ImageDraw, ImageFont, ImageOps



class chartmaker:
    def __init__(self,design,date,time,coords,title,place) -> None:
        self.design = design
        self.time = time
        self.title = title
        self.date = date
        self.place = place
        self.coords = coords
        self.samplepng = {
            "black_design_simple" : ["mediaasset/simpleblack.png","mediaasset/blackbg.png","white"],
            "white_design_simple" :["mediaasset/simplewhite.png","mediaasset/whitebg.png","black"],
            "black_design_art" : ["mediaasset/design.png","mediaasset/blackbg.png","white"],
            "white_design_art" : ["mediaasset/design.png","mediaasset/whitebg.png","black"],

        }
    
    def chart(self):
        ch_image = Image.open(self.samplepng[self.design][0])
        chart = Image.open('mediaasset/input/chart.png')
        ch_image.paste(chart,(400,1200),chart)
        return ch_image

    def imagemaker(self):

        placeline = f"STARS  OVER {self.place}, INDIA"
        datetimeline = f"{self.date} | {self.time}"
        coordsline = f"{self.coords}"

        image = Image.open(self.samplepng[self.design][1])
        img = ImageDraw.Draw(image)
        font_main = ImageFont.truetype("mediaasset/Mont.ttf",230)
        font_sub = ImageFont.truetype("mediaasset/Mont.ttf",150)
        font_micro = ImageFont.truetype("mediaasset/Mont.ttf",70)
        img.text((2480,800),self.title, fill=self.samplepng[self.design][2],font = font_main,anchor="ms")
        img.text((2480,6000),placeline, fill=self.samplepng[self.design][2],font = font_sub,anchor="ms")
        img.text((2480,6200),datetimeline, fill=self.samplepng[self.design][2],font = font_sub,anchor="ms")
        img.text((2480,6600),coordsline, fill=self.samplepng[self.design][2],font = font_sub,anchor="ms")
        img.text((4400,6850),"@astroprint.in", fill=self.samplepng[self.design][2],font = font_micro,anchor="ms")

        return image

    def clubber(self):
        body_ = self.imagemaker()
        chart_ = self.chart()
        f_img = Image.composite(body_,chart_,body_)
        f_img.show()
        f_img.save("saved/newimage.png")

if __name__ == "__main__":
    
    im = chartmaker("black_design_art","25-09-2021","5:30","26.8467° N, 80.9462° E","OUR DAY","LUCKNOW, UTTAR PRADESH")
    im.clubber()

