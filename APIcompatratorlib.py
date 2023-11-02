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
            
    def compare_and_print(self, url1, url2):
        try:
            response1 = self.send_request(url1)
            response2 = self.send_request(url2)
            
            if response1 == response2:
                print(f"{url1} equals {url2}")
            else:
                print(f"{url1} not equals {url2}")

        except Exception as e:
            print(f"Error comparing {url1} and {url2}: {str(e)}")
            

    def compare_responses(self):
        with open(self.file1, 'r') as f1, open(self.file2, 'r') as f2:
            for line1, line2 in zip(f1, f2):
                url1 = line1.strip()
                url2 = line2.strip()
                self.compare_and_print(url1, url2)
        

