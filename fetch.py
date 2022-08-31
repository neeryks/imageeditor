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
        orders = []
        for num_order in range(4):
            print(num_order)
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
            "amount":data["orders"][num_order]["line_items"][0]['properties'][4]["value"],
            "variant":data["orders"][num_order]["shipping_address"]["variant_title"]

            })
        
        return orders
    
    def order_data(self):
        pass   
    

if __name__ == "__main__":
    f = fetcher()
    print(f.shipping_data())


