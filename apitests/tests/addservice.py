from os import write
import requests
import pytest
import unittest
import json
import sys
sys.path.insert(0,'..')
from helper.servicerequests import ServiceRequest


# Servicerequest is within the helper class that initiates requests for various methods.
get_config = ServiceRequest()
#Endpoints stored as within configs as json so it could be easily changed and run on CI for variosu env
service_endpoint = get_config.read_env("../fixtures/configs/envDetails.json","endpoints","services") 
environment = get_config.read_env("../fixtures/configs/envDetails.json","baseUrl","localhost") 


class Tests(unittest.TestCase):
    @classmethod
    def test_it_should_be_ableto_add_service(self):
        #Intiate the helper class that contains the api actions
        requests_helper = ServiceRequest()
        #if service id does not make any difference, we can pass it as None, the parameters help with passing various test data and asserting output
        response = requests_helper.perform_operation("addservice",None,environment + service_endpoint)
        dummyservicename = ServiceRequest.read_env(self,"../fixtures/testdata/newservicenames.json",None,None)
        assert response[0]["name"] == dummyservicename["name"]


  



 






        
        
