
import requests


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

    def create_session(self):
        session = requests.Session()
        session.headers.update({
        "X-Shopify-Access-Token":self.token(),
        "Content-Type":"application/json"
    })
        return session

class Printrove:
    def __init__(self) -> None:
        self.url = "https://api.printrove.com/api/external/designs/834299"

    def __init__(self) -> None:
        self.head = {
            'Authorization':'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIzIiwianRpIjoiOTViOGIwZGIxZTJiNmU5YjkyY2MwNWE1NTUxYzA4NGRkNTc4OWRjZDRkZjE1MDhiOTYyYTk3NGU1OGU3Y2YzYTQ3NDQ1MDVmOWEzMDQyYjIiLCJpYXQiOjE2NjE2Mjc0MzguNDA3MDYzLCJuYmYiOjE2NjE2Mjc0MzguNDA3MDY2LCJleHAiOjE2OTMxNjM0MzguMzk5NDA0LCJzdWIiOiI0Nzc0NSIsInNjb3BlcyI6W119.FsEozyzi1pn-4zMR2KMRUvGqkYKm9k-fXeMDAaiUoYqM2_589zM3DC8g9fEcycoF7hLATLuCI3PGaiJfs3YerKEZuXD7PqemG82QWqq-ImPaSIdqEb6oXYLz1SZr_Pq_jMfW8qw3QitnGUn3pt9Ia5fskTCxtABhFHfApKp8VIUCdDufDsvMoJRtZD-LmYsmDisgZp54TM_41d5cjO9OO_9BJlTxLBChfIWYicIEvcx1KniRAxvkBxV1zpbAVCySJRr-_Tg9_ivmTJLIu-9oCYUHD_AR4Yt3A4ioO6Hak2ucL6bvykKLUVNwxx8Exyc_eOmS1cq-9soClIBs9h3FokdNVMoTf98wK7UYUQXR9gNUSl2xYxXtOYlv4rer7pNFJ8TblP4K6m_yHp1tZGko-WmsRuxC_k824o4ZWTrfq2umk5Mh3sLtoFXNztikhykb3cazXPLtAOC36GGYB1Y3_caHNmijYWW9aHVXM_8jFHOaEPM2Z_kD-2i3X7k2AhN0YeFnEO6G__ZRnsYrhDwn-yxdyqxq9zvrhQkMX7ES_D5_gDLG5COf3St08Pu1jy1DM80R4L6ikcwZqs7ZCZzeyK9YSFetUKFsi7VzXuA9OljATs8qjHSmM0rKDQRwIg_qO9lvsSMbRXiwWlgl1-1esWPGqqq-M9UdSdCp43J1Odg',
            'Content-Type':'application/json',
            'Accept':'application/json'}
        
    def create_order():
        pass

    def costumer_data(self,data):
        pass


if __name__ == "__main__" :
    ur = ShopifyUrls()
    print(ur.url("base_url"),ur.token())
