from urllib import response
import requests
import json
url = "https://api.printrove.com/api/external/designs/834299"

#payload = {
    #"url":"https://static.remove.bg/remove-bg-web/3d75df900686714aa0c3f2ac38a019cdc089943e/assets/start_remove-c851bdf8d3127a24e2d137a55b1b427378cd17385b01aec6e59d5d4b5f39d2ec.png",
    #"name":"231478"}


#response = requests.request("DELETE",url,headers=head)
print(response.json())
class Printrove:
    def __init__(self) -> None:
        self.head = {
            'Authorization':'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIzIiwianRpIjoiOTViOGIwZGIxZTJiNmU5YjkyY2MwNWE1NTUxYzA4NGRkNTc4OWRjZDRkZjE1MDhiOTYyYTk3NGU1OGU3Y2YzYTQ3NDQ1MDVmOWEzMDQyYjIiLCJpYXQiOjE2NjE2Mjc0MzguNDA3MDYzLCJuYmYiOjE2NjE2Mjc0MzguNDA3MDY2LCJleHAiOjE2OTMxNjM0MzguMzk5NDA0LCJzdWIiOiI0Nzc0NSIsInNjb3BlcyI6W119.FsEozyzi1pn-4zMR2KMRUvGqkYKm9k-fXeMDAaiUoYqM2_589zM3DC8g9fEcycoF7hLATLuCI3PGaiJfs3YerKEZuXD7PqemG82QWqq-ImPaSIdqEb6oXYLz1SZr_Pq_jMfW8qw3QitnGUn3pt9Ia5fskTCxtABhFHfApKp8VIUCdDufDsvMoJRtZD-LmYsmDisgZp54TM_41d5cjO9OO_9BJlTxLBChfIWYicIEvcx1KniRAxvkBxV1zpbAVCySJRr-_Tg9_ivmTJLIu-9oCYUHD_AR4Yt3A4ioO6Hak2ucL6bvykKLUVNwxx8Exyc_eOmS1cq-9soClIBs9h3FokdNVMoTf98wK7UYUQXR9gNUSl2xYxXtOYlv4rer7pNFJ8TblP4K6m_yHp1tZGko-WmsRuxC_k824o4ZWTrfq2umk5Mh3sLtoFXNztikhykb3cazXPLtAOC36GGYB1Y3_caHNmijYWW9aHVXM_8jFHOaEPM2Z_kD-2i3X7k2AhN0YeFnEO6G__ZRnsYrhDwn-yxdyqxq9zvrhQkMX7ES_D5_gDLG5COf3St08Pu1jy1DM80R4L6ikcwZqs7ZCZzeyK9YSFetUKFsi7VzXuA9OljATs8qjHSmM0rKDQRwIg_qO9lvsSMbRXiwWlgl1-1esWPGqqq-M9UdSdCp43J1Odg',
            'Content-Type':'application/json',
            'Accept':'application/json'}
        
    def create_order():
        pass

    def costumer_data(self,data):
        pass

   





        