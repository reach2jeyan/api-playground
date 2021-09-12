from os import write
import requests
import pytest
import unittest
import json
import sys

from requests.api import get
sys.path.insert(0,'..')
from helper.servicerequests import ServiceRequest


get_config = ServiceRequest()
service_endpoint = get_config.read_env("../fixtures/configs/envDetails.json","endpoints","services")
environment = get_config.read_env("../fixtures/configs/envDetails.json","baseUrl","localhost")
data_to_update_servicename = get_config.read_env("../fixtures/testdata/serviceName.json",None,None)


class Tests(unittest.TestCase):
    def test_it_should_be_ableto_update_servicebyId(self):
        requests_helper = ServiceRequest()
        response = requests_helper.perform_operation("updateservice",4,environment + service_endpoint )
        assert response[1] == 200
        assert response[0]["name"] == "automated service"
        assert "createdAt" in response[0]
        assert "timeout=5" in response[2]["keep-Alive"]

    
 






        
        
