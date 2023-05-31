import requests

def get_data_from_api(url, is_json=True):
    response = requests.get(url)
    if (is_json):
        recv_res = response.json()
    else:
        recv_res = response.content
    return recv_res

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