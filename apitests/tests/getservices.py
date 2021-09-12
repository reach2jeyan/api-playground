from os import write
import requests
import pytest
import unittest
import json
import sys
sys.path.insert(0,'..')
from helper.servicerequests import ServiceRequest


get_config = ServiceRequest()
service_endpoint = get_config.read_env("../fixtures/configs/envDetails.json","endpoints","services")
environment = get_config.read_env("../fixtures/configs/envDetails.json","baseUrl","localhost")


#Responses from the helper folder of service request class comes in an array of size 2. the first index would be the data the request returns, the second is the response status code,
        #the third is the headers. These are called accordingly with response index to validate.
class Tests(unittest.TestCase):
    
    def test_it_should_response_code_as_200(self):
        requests_helper = ServiceRequest()
        response = requests_helper.perform_operation("getservice",None,environment + service_endpoint)
        assert response[1] == 200
        

    def test_it_should_be_able_fetch_service_by_id(self):
        requests_helper = ServiceRequest()
        response = requests_helper.perform_operation("getservice",4,environment + service_endpoint )
        assert response[0]["id"] == 4

    
    def test_it_should_show_not_found_when_incorrect_serviceid_passed(self):
        requests_helper = ServiceRequest()
        response = requests_helper.perform_operation("getservice",891,environment + service_endpoint )
        assert response[0]["name"] == "NotFound"
        assert response[0]["message"] == "No record found for id '891'"
        assert response[1] == 404

    def test_it_should_validate_headers(self):
        requests_helper = ServiceRequest()
        response = requests_helper.perform_operation("getservice",4,environment + service_endpoint )
        assert "Access-Control-Allow-Origin" in response[2]
        assert "Content-Type" in response[2]
        assert "timeout=5" in response[2]["keep-Alive"]




 






        
        
