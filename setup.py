
from datetime import datetime
from this import d
from PIL import Image, ImageDraw, ImageFont, ImageOps
import cairosvg
import os
from creds import ShopifyUrls
import time


class fetcher(ShopifyUrls):

    def shipping_data(self):
        sess = self.create_session()
        response = sess.get(self.url("get_orders"))
        data = response.json()
        orders = []
        for num_order in range(len(data["orders"])):
            try:
                orders.append({"costumer_name":data["orders"][num_order]["shipping_address"]["first_name"]+data["orders"][num_order]["shipping_address"]["last_name"],
                "city":data["orders"][num_order]["shipping_address"]["city"],
                "state":data["orders"][num_order]["shipping_address"]["province"],
                "country":data["orders"][num_order]["shipping_address"]["country"],
                "address1":data["orders"][num_order]["shipping_address"]["address1"],
                "address2":data["orders"][num_order]["shipping_address"]["address2"],
                "pincode":data["orders"][num_order]["shipping_address"]["zip"],
                "phone":data["orders"][num_order]["shipping_address"]["phone"],
                "email":data["orders"][num_order]["contact_email"],
                "order_id":data["orders"][num_order]["name"],
                "order_name":data["orders"][num_order]["line_items"][0]["title"],
                "design":data["orders"][num_order]["line_items"][0]['properties'][0]["value"],
                "title":data["orders"][num_order]["line_items"][0]['properties'][1]["value"],
                "datetime":data["orders"][num_order]["line_items"][0]['properties'][2]["value"],
                "place":data["orders"][num_order]["line_items"][0]['properties'][3]["value"],
                "coords":data["orders"][num_order]["line_items"][0]['properties'][4]["value"],
                "amount":data["orders"][num_order]["line_items"][0]['properties'][5]["value"],

                })
            except:
                orders.append({"costumer_name":data["orders"][num_order]["billing_address"]["first_name"]+data["orders"][num_order]["billing_address"]["last_name"],
                "city":data["orders"][num_order]["billing_address"]["city"],
                "state":data["orders"][num_order]["billing_address"]["province"],
                "country":data["orders"][num_order]["billing_address"]["country"],
                "address1":data["orders"][num_order]["billing_address"]["address1"],
                "address2":data["orders"][num_order]["billing_address"]["address2"],
                "pincode":data["orders"][num_order]["billing_address"]["zip"],
                "phone":data["orders"][num_order]["billing_address"]["phone"],
                "email":data["orders"][num_order]["contact_email"],
                "order_id":data["orders"][num_order]["name"],
                "order_name":data["orders"][num_order]["line_items"][0]["title"],
                "design":data["orders"][num_order]["line_items"][0]['properties'][0]["value"],
                "title":data["orders"][num_order]["line_items"][0]['properties'][1]["value"],
                "datetime":data["orders"][num_order]["line_items"][0]['properties'][2]["value"],
                "place":data["orders"][num_order]["line_items"][0]['properties'][3]["value"],
                "coords":data["orders"][num_order]["line_items"][0]['properties'][4]["value"],
                "amount":data["orders"][num_order]["line_items"][0]['properties'][4]["value"],


                })
        print(orders)
        return orders

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
        cairosvg.svg2png(url=f"output/img.svg", write_to="mediaasset/input/chart.png",dpi=150,parent_height=1000,parent_width=1000,scale=2.3)
        chart = Image.open('mediaasset/input/chart.png')
        ch_image.paste(chart,(228,1162),chart)
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
        img.text((4400,6850),f"{d['order_id']}@astroprint.in", fill=self.samplepng[self.design][2],font = font_micro,anchor="ms")

        return image

    def clubber(self):
        os.system('../starchart/bin/starchart.bin newmapi.sch')
        body_ = self.imagemaker()
        chart_ = self.chart()
        f_img = Image.composite(body_,chart_,body_)
        f_img.save(f"../output_data/{d['order_id']}.png")

    def data_in(self):
        with open(f"newmapi.sch",'w+') as nimg:
            nimg.write(self.option(self.ra,self.dec))
        self.clubber()
        return 0

    def option(self,ra,dec):
        if d['design']=="White Simple":
            config =f'''
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
                    angular_width=160
                    plot_dso=0
                    coords=ra_dec
                    aspect=1
                    star_mag_labels=0
                    copyright=
                    copyright_gap_2=0
                    copyright_gap=0
                    magnitude_key=0
                    label_font_size_scaling=1.5



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
                angular_width=160
                plot_dso=0
                coords=ra_dec
                aspect=1
                star_mag_labels=0
                copyright=
                copyright_gap_2=0
                copyright_gap=0
                magnitude_key=0
                label_font_size_scaling=1.5



                CHART 
                output_filename=output/img.svg
                star_col=1,1,1
                constellation_stick_col=1,1,1
                constellation_label_col=1,1,1       
                '''

        return config

         

if __name__ == "__main__":
    fet = fetcher()
    dat = fet.shipping_data()
    for d in dat:
        def ra_dec():
            pass
        im = chartmaker(d['design'],d['datetime'].split()[0],d['datetime'].split()[1],d['coords'],7.274,32.73,d['title'],d['place'])
        im.data_in()
        
