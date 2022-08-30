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

    def main(self):
        sess = self.create_session()
        response = sess.get(self.url("get_orders"))
        data = response.json()
        shipping_data = {"costumer_name":data["orders"][0]["shipping_address"]["first_name"]+data["orders"][0]["shipping_address"]["last_name"],
        "city":data["orders"][0]["shipping_address"]["city"],
        "state":data["orders"][0]["shipping_address"]["province"],
        "country":data["orders"][0]["shipping_address"]["country"],
        "address1":data["orders"][0]["shipping_address"]["address1"],
        "address2":data["orders"][0]["shipping_address"]["first_name"],
        "pincode":data["orders"][0]["shipping_address"]["zip"],
        "phone":data["orders"][0]["shipping_address"]["phone"],
        "email":data["orders"][0]["contact_email"],
        "ref_number":"pass"
        }

        return shipping_data
    
    

if __name__ == "__main__":
    f = fetcher()
    print(f.main())


