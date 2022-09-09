
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont, ImageOps
import cairosvg
from fetch import fetcher
import os



class chartmaker(fetcher):
    def __init__(self,design,date,time,coords,ra,dec,title,place) -> None:
        self.design = design
        self.time = time
        self.title = title
        self.ra = ra
        self.dec = dec
        self.date = date
        self.place = place
        self.coords = coords
        self.samplepng = {
            "Black Simple" : ["mediaasset/simpleblack.png","mediaasset/blackbg.png","white"],
            "White Simple" :["mediaasset/simplewhite.png","mediaasset/whitebg.png","black"],
            "Black Art" : ["mediaasset/design.png","mediaasset/blackbg.png","white"],
            "White Art" : ["mediaasset/design.png","mediaasset/whitebg.png","black"],

        }
    
    def chart(self):
        ch_image = Image.open(self.samplepng[self.design][0])
        cairosvg.svg2png(url='../starchart/examples/output/img.svg', write_to="mediaasset/input/chart.png",dpi=350,parent_height=1024,parent_width=1024)
        chart = Image.open('mediaasset/input/chart.png')
        ch_image.paste(chart,(250,1200),chart)
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
        #f_img.show()
        f_img.save("../output_data/newimage.png")

    def data_in(self):
        #data_list = self.shipping_data()
        with open("../starchart/examples/newmapi.sch",'w') as wrt:
            wrt.write(self.option(self.ra,self.dec))
            os.system('../starchart/bin starchart.bin ../starchart/examples/newmapi.sch')
            self.clubber()


        return 0

    def option(self,ra,dec):
        if 1<2:
            config=f'''
                        DEFAULTS

                        plot_equator=0
                        plot_galactic_plane=0
                        plot_ecliptic=0
                        plot_galaxy_map=0
                        ra_central={ra}
                        dec_central={dec}
                        position_angle=15
                        constellation_sticks=1
                        coords=ra_dec
                        star_names=0
                        star_label_mag_min=1.5
                        ra_dec_lines=0
                        projection=sphere
                        star_catalogue_numbers=0
                        constellation_boundaries=0
                        dso_symbol_key=0
                        width = 30
                        dso_names=0
                        angular_width=140
                        plot_dso=0
                        coords=ra_dec
                        aspect=1
                        star_mag_labels=0
                        copyright=
                        copyright_gap_2=0
                        copyright_gap=0
                        magnitude_key=0

                        CHART 
                        output_filename=output/img.svg
                        star_col=0,0,0
                        constellation_stick_col=0,0,0
                        constellation_label_col=0,0,0         
                '''
        else:
                config=f'''
                    DEFAULTS

                    plot_equator=0
                    plot_galactic_plane=0
                    plot_ecliptic=0
                    plot_galaxy_map=0
                    ra_central={ra}
                    dec_central={dec}
                    position_angle=15
                    constellation_sticks=1
                    coords=ra_dec
                    star_names=0
                    star_label_mag_min=1.5
                    ra_dec_lines=0
                    projection=sphere
                    star_catalogue_numbers=0
                    constellation_boundaries=0
                    dso_symbol_key=0
                    width = 30
                    dso_names=0
                    angular_width=140
                    plot_dso=0
                    coords=ra_dec
                    aspect=1
                    star_mag_labels=0
                    copyright=
                    copyright_gap_2=0
                    copyright_gap=0
                    magnitude_key=0

                    CHART 
                    output_filename=output/img.svg
                    star_col=0,0,0
                    constellation_stick_col=0,0,0
                    constellation_label_col=0,0,0
               '''
        return config

         

if __name__ == "__main__":
    fet = fetcher()
    dat = fet.shipping_data()
    for d in dat:
        im = chartmaker(d['design'],d['datetime'].split()[0],d['datetime'].split()[1],d['coords'],5,6,d['title'],d['place'])
        #im.clubber()
        im.data_in()
