import requests
import json
from creds import ShopifyUrls

class fetcher(ShopifyUrls):

    def create_session(self):
        session = requests.Session()
        session.headers.update({
        "X-Shopify-Access-Token":self.token(),
        "Content-Type":"application/json"
    })
        return session

    def shipping_data(self):
        sess = self.create_session()
        response = sess.get(self.url("get_orders"))
        data = response.json()
        data = {"costumer_name":data["orders"][0]["shipping_address"]["first_name"]+data["orders"][0]["shipping_address"]["last_name"],
        "city":data["orders"][0]["shipping_address"]["city"],
        "state":data["orders"][0]["shipping_address"]["province"],
        "country":data["orders"][0]["shipping_address"]["country"],
        "address1":data["orders"][0]["shipping_address"]["address1"],
        "address2":data["orders"][0]["shipping_address"]["address2"],
        "pincode":data["orders"][0]["shipping_address"]["zip"],
        "phone":data["orders"][0]["shipping_address"]["phone"],
        "email":data["orders"][0]["contact_email"],
        "order_id":data["orders"][0]["name"],
        "order_id":data["orders"][0]["line_items"][0]["title"],
        "design":data["orders"][0]["line_items"][0]['properties'][0]["value"],
        "title":data["orders"][0]["line_items"][0]['properties'][1]["value"],
        "datetime":data["orders"][0]["line_items"][0]['properties'][2]["value"],
        "place":data["orders"][0]["line_items"][0]['properties'][3]["value"],
        "coords":data["orders"][0]["line_items"][0]['properties'][4]["value"]

        }
        return data
    
    def order_data(self):
        pass   
    

if __name__ == "__main__":
    f = fetcher()
    print(f.shipping_data())


