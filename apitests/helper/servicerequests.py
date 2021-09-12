
from re import match
from typing import Match
import requests
from faker import Faker
import json
from requests import status_codes

from requests.models import Response
class ServiceRequest():
    #We want to read the params from an external source, in order to control with various environments and data. This enables us to run better on CI
    # config_value is the key and the config_item is what is nested within the key, if there are none, we pass as None and return entire response
    def read_env(self,file,config_item,config_value):
        with open(file) as f:
            data = json.load(f)
            if config_value ==None and config_item == None:
                return data
            else:
                return data[config_item][config_value]


    def get_service_list(self,id,url):
        if id == "None":
            self.response = requests.get(url)
            return [self.response.json(),self.response.status_code,self.response.headers]
        else:
            self.response = requests.get(url + "/" +id , params=ServiceRequest().read_env("../fixtures/testdata/limitresponse.json",None,None))
            return [self.response.json(),self.response.status_code,self.response.headers]

    def update_service(self,id,url,payload):
        self.response = requests.patch(url + "/" + id,data=payload)
        return [self.response.json(),self.response.status_code,self.response.headers]

    def create_service(self,url,payload):
        self.response = requests.post(url,data=payload)
        return [self.response.json(),self.response.status_code,self.response.headers]

    def perform_operation(self,method,id,url):
        #This is the entrance to the other functions, this function is called from the pytests with various parameters, based on the method, the other functions are called
        if method == "getservice":
            return self.get_service_list(str(id),url)

        if method == "updateservice":
            payload =  ServiceRequest.read_env(self,"../fixtures/testdata/servicename.json",None,None)
            return self.update_service(str(id),url,payload)

        if method == "addservice":
            fake = Faker()
            payload = {
                "name" : fake.name()
            }
            with open("../fixtures/testdata/newservicenames.json", 'w') as f:
                json.dump(payload, f)
            return self.create_service(url,payload)
        else:
            print ("TBD")

    

        