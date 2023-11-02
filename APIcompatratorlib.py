from urllib.request import urlopen, Request

class APIComparator:
    def __init__(self, file1, file2):
        self.file1 = file1
        self.file2 = file2

   
    def send_request(self, url):
        httprequest = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urlopen(httprequest) as response:
            if response.status == 200:
                return response.read().decode()
                 
            else:
                return None
            
        

