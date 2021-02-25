import requests
from common import config
from .handle.mongo import Mongo

class Site():
    def __init__(self, parametro):
        self._config = config()['sites'][parametro]
        self.url = self._config['url']
        self.currentSession = requests.session()
        self.mongo = Mongo()
        self.run_script()

    def run_script(self):
        print(self.url)
        response = self.get_url(self.url)
        print(response.status_code)

        product = {
            "Site": "MiSite",
            "Sku": "1",
            "Name": "Chocolate"
        }
        self.mongo.insert(product)

        print("Insert")

    def get_url(self, url):
        '''
        Requests method
        '''
        requestsTimeout = 5
        while True:
            try:
                response = self.currentSession.get(url, timeout=requestsTimeout)
                return response
            except requests.exceptions.ConnectionError:
                print("Connection Error, Retrying")
                time.sleep(requestsTimeout)
                continue
            except requests.exceptions.RequestException:
                print('Waiting...')
                time.sleep(requestsTimeout)
                continue
            break