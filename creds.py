
from lib2to3.pgen2 import token


class ShopifyUrls:

    def token(self):
        token = "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"
        return token

    def url(self,type):
        access_dict = {
            "base_url":"https://astroprinting.myshopify.com",
            "order_place":"https://astroprinting.myshopify.com/admin/api/2022-10/orders.json",
            "get_products":"https://astroprinting.myshopify.com/admin/api/2022-10/products.json",
            "get_orders":"https://astroprinting.myshopify.com/admin/api/2022-10/orders.json?status=unfulfilled" 
            }
        return access_dict[type]

if __name__ == "__main__" :
    ur = ShopifyUrls()
    print(ur.url("base_url"),ur.token())
