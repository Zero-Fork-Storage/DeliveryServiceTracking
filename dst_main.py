import requests


class Delivery_Service_Tracking:
    def __init__(self):
        self.url = "https://m.search.naver.com/p/csearch/ocontent/util/headerjson.nhn"
        self.Token: str = "6a4f5c129b07c9e96b21129a4d4ec404830a7ac0"

    """  Collect basic information about using the Courier Delivery Tracking API
    
    Parameters :
        | 1 | dst_company_code (str) : courier company code
        | 2 | dst_waybill_number (str) : Waybill code
    info :
        The values entered in 1 and 2 are numeric, but are taken as string values to avoid errors.
    """
    def lookup(self, dst_company_code: str, dst_waybill_number: str):
        s = requests.session()
        dcc = dst_company_code
        dwn = dst_waybill_number
        headers = {
            "Host": "m.search.naver.com",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0",
            "Accept": "*/*",
            "Accept-Language": "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3",
            "Accept-Encoding": "gzip, deflate, br",
            "Referer": f"https://search.naver.com/search.naver?sm=top_sly.hst&fbm=0&ie=utf8&query={dwn}",
            "DNT": "1",
            "Connection": "keep-alive",
            "TE": "Trailers"
        }
        params = {
            "callapi": "parceltracking",
            "t_code": dcc,
            "t_invoice": dwn,
            "passportKey": self.Token
        }
        look = s.get(url=self.url, params=params, headers=headers)
        data = look.json()
        return data


Get = Delivery_Service_Tracking()