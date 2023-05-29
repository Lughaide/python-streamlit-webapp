import requests

def load_img_from_api(url):
    response = requests.get(url)
    recv_res = response.json()
    return recv_res["message"]

def load_fact_from_api(url):
    response = requests.get(url)
    recv_res = response.json()
    return recv_res["data"][0]["attributes"]["body"]

def load_img_arr_from_api(url):
    response = requests.get(url)
    img_data = response.content
    return img_data

class HiliteMeFormatter:
    def __init__(self, code="", lexer="python", style="colorful", divstyles=""):
        self.url = "http://hilite.me/api"
        self.keys = ['code', 'lexer', 'style', 'divstyles']
        self.params = {}
        self.set(code=code, lexer=lexer, style=style, divstyles=divstyles)

    def set(self, **kwargs):
        for key in self.keys:
            if key in kwargs:
                self.params[key] = kwargs[key]

    def formatCode(self):
        r = requests.post(url=self.url, data=self.params)
        formattedCode = r.text
        r.close()
        return formattedCode
    
class QRCodeMaker:
    def __init__ (self, data="", size="150x150"):
        self.url = "http://api.qrserver.com/v1/create-qr-code/"
        self.keys = ['data', 'size']
        self.params = {}
        self.set(data=data, size=size)

    def set(self, **kwargs):
        for key in self.keys:
            if key in kwargs:
                self.params[key] = kwargs[key]

    def getQRCode(self):
        r = requests.get(url=self.url, params=self.params)
        return r.content
    
class ProfanityCheck:
    def __init__(self, text="", add="", fill_text=""):
        self.url = "https://www.purgomalum.com/service/json"
        self.keys = ['text', 'add', 'fill_text']
        self.params = {}
        self.set(text=text, add=add, fill_text=fill_text)

    def set(self, **kwargs):
        for key in self.keys:
            if key in kwargs:
                self.params[key] = kwargs[key]

    def getFilteredResults(self):
        r = requests.get(url=self.url, params=self.params)
        return r.json()